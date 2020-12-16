/********************************************************************/
/* Naive NxM matriz multiplication using CUDA without shared memory */
/********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

#define BLOCK_SIZE 16

__device__ void variables(){

	int indice_local = threadIdx.x;
	int indice_global = blockDim.x * blockIdx.x + threadIdx.x;
	int indice_bloco = blockIdx.x;
	int tamanho_grid = gridDim.x;

	printf("Hello from thread: índice global %d, índice local: %d, bloco: %d, tamanho do grid: %d\n\n", indice_global, indice_local, indice_bloco, tamanho_grid);
}

// 
// Found this function here:
// https://medium.com/analytics-vidhya/matrix-multiplication-in-cuda-a-simple-guide-bab44bc1f8ab
// 
// Probably it is based on chapter 3.2.4.Shared Memory from
// https://docs.nvidia.com/cuda/pdf/CUDA_C_Programming_Guide.pdf
// 
__global__ void mul(int *a, int *b, int *c, int n, int m, int width) {

	// Each thread computes one element of C
	// by accumulating results into 'sum'
  int col = blockIdx.x * blockDim.x + threadIdx.x;
	int row = blockIdx.y * blockDim.y + threadIdx.y;   
	
	// check boundry conditions
  if(row < n && col < m){
		
		// variables();		

		int sum = 0;

    // do the multiplication for one row and col
    for(int k = 0; k < width; k++){
			sum += a[row * width + k] * b[k * m + col];
		}

    // store the result
    c[row * m + col] = sum;
  }
	
}

int main(int argc, char **argv){	

	int lin_a, col_a, col_b; // qntd de linhas e colunas das matrizes
	int *a, *b, *c; // matrizes do host
	int *dev_a, *dev_b, *dev_c; // matrize do device

	// Lendo numero de linhas e colunas da matriz A e B
	scanf("%d %d %d\n", &lin_a, &col_a, &col_b);

	// Alocando as cópias das matrizes no host
	a = (int*) malloc(lin_a * col_a * sizeof(int));
	b = (int*) malloc(col_a * col_b * sizeof(int));
	c = (int*) malloc(lin_a * col_b * sizeof(int));

	// Alocando as cópias das matrizes no device
	cudaMalloc((void**)&dev_a, lin_a * col_a * sizeof(int));
	cudaMalloc((void**)&dev_b, col_a * col_b * sizeof(int));
	cudaMalloc((void**)&dev_c, lin_a * col_b * sizeof(int));
	
	// Lendo valores da matriz "a"
	for(int i = 0; i < lin_a; i++){
		for(int j = 0; j < col_a; j++){
			scanf("%d ", &a[i * col_a + j]);
		}
	}

	// Exibindo valores da matriz "a"
	printf("\nMatriz a:\n");
	for(int i = 0; i < lin_a; i++){
		for(int j = 0; j < col_a; j++){
			printf("%d ", a[i * col_a + j]);
		}
		printf("\n");
	}

	// Lendo valores da matriz "b"
	for(int i = 0; i < col_a; i++){
		for(int j = 0; j < col_b; j++){
			scanf("%d ", &b[i * col_b + j]);
		}
	}

	// Exibindo valores da matriz "b"
	printf("\nMatriz b:\n");
	for(int i = 0; i < col_a; i++){
		for(int j = 0; j < col_b; j++){
			c[i * col_b + j] = 0;
			printf("%d ", b[i * col_b + j]);
		}
		printf("\n");
	}
	printf("\n");

	// Copiando valores de 'a', 'b' e 'c' em suas cópias no device
	cudaMemcpy(dev_a, a, lin_a * col_a * sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b, b, col_a * col_b * sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(dev_c, c, lin_a * col_b * sizeof(int), cudaMemcpyHostToDevice);

	dim3 numBlocks(ceil(lin_a/(float)BLOCK_SIZE), ceil(col_b/(float)BLOCK_SIZE));
	dim3 threadsPerBlock(BLOCK_SIZE, BLOCK_SIZE);

	mul<<<numBlocks,threadsPerBlock>>>(dev_a, dev_b, dev_c, lin_a, col_b, col_a);

	// Copiando a matriz 'c' do device pro host. 
	// Essa função tem um CudaDevSync implícito.
	cudaMemcpy(c, dev_c, lin_a * col_b * sizeof(int), cudaMemcpyDeviceToHost);

	// Exibindo valores da matriz "c"
	printf("Matriz c:\n");
	for(int i = 0; i < lin_a; i++){
		for(int j = 0; j < col_b; j++){
			printf("%d ", c[i * col_b + j]);
		}
		printf("\n");
	}

	// Liberando memória
	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_c);
	free(a);
	free(b);
	free(c);
  
	return 0;
}