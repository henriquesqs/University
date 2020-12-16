#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <cuda.h>

__global__ void dotProduct(int *a, int *b, int *dot_global, int n) {
	
	int tid = threadIdx.x; // identificador local da thread
	int localDot = 0, aux = 0;
	int id = blockIdx.x * blockDim.x + threadIdx.x;

	if (id < n) {
		for(int i = 0; i < n; i++) {
			aux = a[tid * n + i] * b[tid * n + i];
			localDot += aux;
		}
	}

	atomicAdd(dot_global, localDot);
}

__global__ void minValue(int *a, int *b, int *min_global, int n) {
	
	int tid = threadIdx.x; // identificador local da thread
	int localMin = INT_MAX, aux = 0;
	int id = blockIdx.x * blockDim.x + threadIdx.x;

	if(id < n) {
		for (int i = 0; i < n; i++) {
			aux = min(a[tid * n + i], b[tid * n + i]);
			localMin = min(localMin, aux);
		}
	}
	
	atomicMin(min_global, localMin);
}

__global__ void maxValue(int *a, int *b, int *max_global, int n) {

	int tid = threadIdx.x; // identificador local da thread
	int localMax = INT_MIN, aux = 0;
	int id = blockIdx.x * blockDim.x + threadIdx.x;

	if(id < n) {
		for (int i = 0; i < n; i++) {
			aux = max(a[tid * n + i], b[tid * n + i]);
			localMax = max(localMax, aux);
		}
	}

	atomicMax(max_global, localMax);
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

	if (pFile == NULL) {
		printf("Error opening file.\n");
		return 0;
	}

	int n; // Tamanho das matrizes
	int *a, *b; // Matrizes
	int numBlocks; // Numero de blocos por grid
	int threadsPerBlock; // Numero de threads por bloco
	int *min, *max, *dot; // Variaveis de resultado
	cudaStream_t stream1, stream2, stream3; // Variáveis pra criação de streams

	// Criação das streams.
	// Cada uma ficará responsável por uma operação solicitada:
	// Stream1: produto escalar; Stream2: maior valor; Stream3: menor valor
	cudaStreamCreate(&stream1);
	cudaStreamCreate(&stream2);
	cudaStreamCreate(&stream3);

	// Lendo tamanho das matrizes
	// scanf("%d\n", &n);
	fscanf(pFile, "%d\n", &n);

	// Aloca as matrizes 'a', 'b' no host e no device
	// (memória mapeada (pinned memory) em endereço virtual unificado)
	// É mais rapido do que usar malloc convencional
	cudaHostAlloc((void **)&a, n * n * (sizeof(int)), cudaHostAllocMapped);
	cudaHostAlloc((void **)&b, n * n * (sizeof(int)), cudaHostAllocMapped);

	// Aloca as variáveis de resultado no host e no device
	cudaHostAlloc((void **)&min, sizeof(int), cudaHostAllocMapped);
	cudaHostAlloc((void **)&max, sizeof(int), cudaHostAllocMapped);
	cudaHostAlloc((void **)&dot, sizeof(int), cudaHostAllocMapped);

	// Lendo matriz 'a'
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			// scanf("%d ", &a[i * n + j]);
			fscanf(pFile, "%d ", &a[i * n + j]);
		}
	}

	// Exibindo a matriz 'a'
	// printf("Matriz a:\n");
	// for (int i = 0; i < n; i++){
	// 	for (int j = 0; j < n; j++){
	// 		printf("%d ", a[i * n + j]);
	// 	}
	// 	printf("\n");
	// }

	// Lendo a matriz 'b'
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			// scanf("%d ", &b[i * n + j]);
			fscanf(pFile, "%d ", &b[i * n + j]);
		}
	}

	// Exibindo a matriz 'b'
	// printf("\nMatriz b:\n");
	// for (int i = 0; i < n; i++){
	// 	for (int j = 0; j < n; j++){
	// 		printf("%d ", b[i * n + j]);
	// 	}
	// 	printf("\n");
	// }

	numBlocks = 256;
	threadsPerBlock = (numBlocks/n)+1;
	
	*min = INT_MAX; // inicializa min global
	*max = INT_MIN; // inicializa max global

	dotProduct<<<numBlocks, threadsPerBlock, 0, stream1>>>(a, b, dot, n);
	minValue<<<numBlocks, threadsPerBlock, 0, stream2>>>(a, b, min, n);
	maxValue<<<numBlocks, threadsPerBlock, 0, stream3>>>(a, b, max, n);
	
	// Sincroniza pois não teremos a função cudaMemcpy
	// que tem a sincronização implicita
	cudaDeviceSynchronize();
	
	// Exibindo resultados
	printf("%d %d %d\n", *dot, *min, *max);

	// Liberando memória das matrizes e das variáveis de resultado
	cudaFreeHost(a);
	cudaFreeHost(b);
	cudaFreeHost(min);
	cudaFreeHost(max);
	cudaFreeHost(dot);

	// Destroi as streams
	cudaStreamDestroy(stream1);
	cudaStreamDestroy(stream2);
	cudaStreamDestroy(stream3);

	return 0;
}