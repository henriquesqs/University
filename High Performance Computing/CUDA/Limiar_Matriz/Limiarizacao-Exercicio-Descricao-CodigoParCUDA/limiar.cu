#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <cuda.h>

__global__ void calculaLimiar(int *mat, int lin, int col, int limiar) {

	int i = blockDim.x * blockIdx.x + threadIdx.x; 
	int j = blockDim.y * blockIdx.y + threadIdx.y;

	if(i < lin && j < col){
		if(mat[i * col + j] > limiar){
			mat[i * col + j] = 1;
		}
		else{
			mat[i * col + j] = 0;
		}
	}

}

int main(int argc, char **argv) {

	// Verificando se o usuário inseriu os argumentos corretamente
	if (argc < 2) {
		printf("Missing filename argument.\n");
		return 0;
	}
	
	// Lendo arquivo de entrada
	FILE *pFile;
	pFile = fopen(argv[1], "r");

	if(pFile == NULL) {
		printf("Error opening file.\n");
		return 0;
	}
	
	int *mat; // matriz
	int limiar; // limiar da matriz
	int lin, col; // dimensoes da matriz
	int blockSize = 32; // tamanho do bloco dentro do grid

	// Lendo tamanho e limiar da matriz
	fscanf(pFile, "%d %d\n%d\n", &lin, &col, &limiar);

	// Alocação da matriz (pinned memory, pois é mais rápida)
	// A matriz já está sendo alocada no host e no device
	cudaHostAlloc((void **)&mat, lin * col * (sizeof(int)), cudaHostAllocMapped);

	// Leitura dos dados da matriz
	for(int i = 0; i < lin; i++){
		for(int j = 0; j < col; j++){
			fscanf(pFile, "%d ", &mat[i * col + j]);
		}
	}

	// Exibição dos dados da matriz
	printf("Matriz lida:\n");
	for(int i = 0; i < lin; i++){
		for(int j = 0; j < col; j++){
			printf("%d ", mat[i * col + j]);
		}
		printf("\n");
	}

	dim3 threadsPerBlock(blockSize, blockSize);
	dim3 numBlocks(ceil(col/(float)threadsPerBlock.x), ceil(lin/(float)threadsPerBlock.y));

  	calculaLimiar<<<numBlocks, threadsPerBlock>>>(mat, lin, col, limiar);

	// Sincroniza pois não tem o cudaMemcpy que tem a sincronização implicita
	cudaDeviceSynchronize();

	// Exibição dos dados da matriz após aplicação do limiar
	printf("\nMatriz resultante:\n");
	for(int i = 0; i < lin; i++){
		for(int j = 0; j < col; j++){
			printf("%d ", mat[i * col + j]);
		}
		printf("\n");
	}

  	cudaFreeHost(mat);

	return 0;
}