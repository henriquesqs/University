/*	
	
	Grupo 13 - Turma B
	
	Gustavo T. Mastrobuono, 			NUSP 10734411;
	Henrique de S. Q. dos Santos, NUSP 10819029;
	Jhordan P. V. Pesantes, 			NUSP 11733353;
	Witor M. A. de Oliveira, 			NUSP 10692190;
	Yorvin A. R. Carrion, 				NUSP 11733332;

*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <cuda.h>

#define THREADS 4

// Função original por Paulo S L de Souza
// Modificada pelo grupo
__global__ void calc_diferenca(int *matriz, int *max_diff, int *maior, int *menor, int n){

	int i, j;
	int dif = INT_MIN, aux_dif = INT_MIN; // maior local, diferenca atual

	int linha = blockIdx.x * blockDim.x + threadIdx.x;
	int coluna = blockIdx.y * blockDim.y + threadIdx.y;
	
	for (i = (linha - 1); i < (linha + 2); i++){
		for (j = (coluna - 1); j < (coluna + 2); j++){

			if( (i < n && i >= 0) && (j < n && j >= 0) && (linha < n && linha >= 0) && (coluna < n && coluna >= 0) ){
			
				aux_dif = abs(matriz[linha * n + coluna] - matriz[i * n + j]);

				if(aux_dif > dif){

					dif = aux_dif;
					
					atomicMax(max_diff, dif);
					
					if(dif == *max_diff){
						
						if (matriz[linha * n + coluna] > matriz[i * n + j]){
							atomicExch(maior, matriz[linha * n + coluna]);
							atomicExch(menor, matriz[i * n + j]);
						}
						
						else {
							atomicExch(maior, matriz[i * n + j]);
							atomicExch(menor, matriz[linha * n + coluna]);
						}
					}
				}
			}
		}
	}
}

int main(int argc, char **argv){

	int n; // tamanho da matriz
	int *a; // matriz
	int *max_diff, *maior, *menor; // variaveis de resultado

	// Lendo tamanho das matrizes
	scanf("%d\n", &n);

	// Aloca a matriz 'a' no host e no device
	// (memória mapeada (pinned memory) em endereço virtual unificado)
	// É mais rapido do que usar malloc convencional.
	cudaHostAlloc((void **)&a, n * n * (sizeof(int)), cudaHostAllocMapped);

	// Aloca as variáveis de resultado no host e no device
	cudaHostAlloc((void **)&max_diff, sizeof(int), cudaHostAllocMapped);
	cudaHostAlloc((void **)&maior, sizeof(int), cudaHostAllocMapped);
	cudaHostAlloc((void **)&menor, sizeof(int), cudaHostAllocMapped);

	// Lendo matriz 'a'
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			scanf("%d ", &a[i * n + j]);
		}
	}

	// for (int i = 0; i < n; i++){
	// 	for (int j = 0; j < n; j++){
	// 		printf("%d ", a[i * n + j]);
	// 	}
	// 	printf("\n");
	// }

	*max_diff = INT_MIN; // inicializa max global

	// Define a quantidade de threads por bloco
	dim3 threadsPerBlock(THREADS,THREADS);

	// Define a quantidade de blocos por grade
	dim3 blocksPerGrid(((n+(threadsPerBlock.x-1)) / threadsPerBlock.x), (n+(threadsPerBlock.y-1)) / threadsPerBlock.y);

	calc_diferenca<<<blocksPerGrid, threadsPerBlock>>>(a, max_diff, maior, menor, n);

	// Sincroniza pois não teremos a função cudaMemcpy
	// que tem a sincronização implicita
	cudaDeviceSynchronize();

	// Exibindo resultados
	printf("%d %d \n", *maior, *menor);

	cudaFreeHost(a);
	cudaFreeHost(max_diff);
	cudaFreeHost(maior);
	cudaFreeHost(menor);

	return 0;
}
