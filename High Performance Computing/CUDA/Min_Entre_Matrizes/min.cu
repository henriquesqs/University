#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <cuda.h>

__global__ void min(int* mat, int lin, int col, int* min_global){
	
	int min_local = INT_MAX;
	
	int i = blockDim.x * blockIdx.x + threadIdx.x; 
	int j = blockDim.y * blockIdx.y + threadIdx.y;
	
	if(i < lin && j < col) {
		if(mat[i * col + j] < *min_global){
			min_local = mat[i * col + j];
			atomicMin(min_global, min_local);
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
	
	int *a, *b; // matrizes
	int blockSize = 16; // tamanho do bloco dentro do grid
	int *min_a, *min_b; // variavel de resultado
	int lin_a, col_a, lin_b, col_b; // dimensoes das matrizes
    cudaStream_t stream1,stream2; // variaveis de stream

    //Criação das streams
    cudaStreamCreate(&stream1);
    cudaStreamCreate(&stream2);

	// Lendo tamanho das matrizes
	fscanf(pFile, "%d %d\n%d %d\n", &lin_a, &col_a, &lin_b, &col_b);

	// Alocação da matriz 'a' e 'b' (pinned memory, pois é mais rápida)
	// A matriz já está sendo alocada no host e no device
	cudaHostAlloc((void **)&a, lin_a * col_a * (sizeof(int)), cudaHostAllocMapped);
	cudaHostAlloc((void **)&b, lin_b * col_b * (sizeof(int)), cudaHostAllocMapped);

	// Alocação das variaveis de resultado no host e no device
	cudaHostAlloc((void **)&min_a, (sizeof(int)), cudaHostAllocMapped);
	cudaHostAlloc((void **)&min_b, (sizeof(int)), cudaHostAllocMapped);

	// Lendo elementos da matriz 'a'
	for(int i = 0; i < lin_a; i++){
		for(int j = 0; j < col_a; j++){
			fscanf(pFile, "%d ", &a[i * col_a + j]);
		}
	}

	// Exibindo elementos da matriz 'a'
	printf("Matriz a:\n");
	for(int i = 0; i < lin_a; i++){
		for(int j = 0; j < col_a; j++){
			printf("%d ", a[i * col_a + j]);
		}
		printf("\n");
	}

	// Lendo elementos da matriz 'b'
	for(int i = 0; i < lin_b; i++){
		for(int j = 0; j < col_b; j++){
			fscanf(pFile, "%d ", &b[i * col_b + j]);
		}
	}

	// Exibindo elementos da matriz 'b'
	printf("\nMatriz b:\n");
	for(int i = 0; i < lin_b; i++){
		for(int j = 0; j < col_b; j++){
			printf("%d ", b[i * col_b + j]);
		}
		printf("\n");
	}

	dim3 numBlocksA(ceil(lin_a/(float)blockSize), ceil(col_a/(float)blockSize));
	dim3 threadsPerBlockA(blockSize, blockSize);

	dim3 numBlocksB(ceil(lin_b/(float)blockSize), ceil(col_b/(float)blockSize));
	dim3 threadsPerBlockB(blockSize, blockSize);

	// Inicializando variaveis de min_global
	*min_a = INT_MAX;
	*min_b = INT_MAX;

	min<<<numBlocksA, threadsPerBlockA,0,stream1>>>(a, lin_a, col_a, min_a);
	min<<<numBlocksB, threadsPerBlockB,0,stream2>>>(b, lin_b, col_b, min_b);

	// Sincroniza pois não teremos a função cudaMemcpy
	// que tem a sincronização implicita
	cudaDeviceSynchronize();

	printf("\nResultado:\n%d\n%d\n", *min_a, *min_b);

	// Libera memória das matrizes e das variaveis de resultado
	cudaFreeHost(a);
	cudaFreeHost(b);
	cudaFreeHost(min_a);
	cudaFreeHost(min_b);

	// Destroi as streams
    cudaStreamDestroy(stream1);
    cudaStreamDestroy(stream2);

	return 0;
}