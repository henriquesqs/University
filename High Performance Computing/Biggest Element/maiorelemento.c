// compilar: make
// executar: make run tam=100
// 
// original por: Profº. Dr. Paulo Sérgio Lopes de Souza
// 
// modificado por: 
// Gustavo T. Mastrobuono NUSP 10734411, Henrique de S. Q. dos Santos NUSP 10819029, 
// Jhordan P. V. Pesantes NUSP 11733353, Witor M. A. de Oliveira NUSP 10692190 e Yorvin A. R. Carrion NUSP 11733332


#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

#define T 4 // macro para definir o numero de threads utilizadas

int main(int argc, char **argv) {

	double wtime; // variável para controlar o tempo de busca 
	int *vetor, i, maior_global = 0, maior_local = 0, tam;

	if (argc != 2)
	{
		printf("Wrong arguments. Please use binary <amount_of_elements>\n");
		exit(0);
	}

	tam = atoi(argv[1]);

	printf("Amount of vetor=%d\n", tam);
	fflush(0);

	vetor = (int *)malloc(tam * sizeof(int)); // Aloca o vetor da dimensão lida

	int iteracoes = 0; // variavel para controlar o numero de iteracoes de cada thread
	int thread_num = 0, nthreads = 0, resto = 0;

	iteracoes = tam / T; // limite de iterações de cada laço "for
	resto = tam % T; // resto da divisao para quando tam/T não for exata

	omp_lock_t lock;
	omp_init_lock(&lock);

	vetor[tam / 2] = tam; // atribui o maior valor ao meio do vetor
	
	if(resto == 0){

		wtime = omp_get_wtime(); // Salva o tempo de início

		#pragma omp parallel num_threads(T) private(i, maior_local) shared(maior_global)
		{	

			// Região de preenchimento do vetor
			for (i = omp_get_thread_num() * iteracoes; i < iteracoes + omp_get_thread_num() * iteracoes; i++) {		
				if(i == (tam/2)) continue;
				else vetor[i] = 1;
			}
			// Fim da região
	
			#pragma omp barrier // Sincronização das threads: esperamos todas as threads terminarem o preenchimento do vetor

			// Região de busca pelo maior elemento
			for (i = omp_get_thread_num() * iteracoes; i < iteracoes + omp_get_thread_num() * iteracoes; i++) {				
				if(vetor[i] > maior_local)
                	maior_local=vetor[i];							
			}

			// região crítica da operação, deve ser protegida pra não sobrescrever o valor do "maior" global
			omp_set_lock(&lock); 
			if (maior_local > maior_global)
			maior_global = maior_local;
			omp_unset_lock(&lock);
			// fim da região crítica
			
		}

		wtime = omp_get_wtime() - wtime; // salva o tempo de término
		// Fim da região de busca

	}

	else {

		wtime = omp_get_wtime();

		#pragma omp parallel num_threads(T) private(i, maior_local) shared(maior_global)
		{			

			if(omp_get_thread_num() == 0){
				for(i = 0; i < (tam/2); i++){
					if(i == (tam/2)) continue;
					else vetor[i] = 1;
				}
			}
			else{
				for(i = (tam/2)+1; i < tam; i++){
					if(i == (tam/2)) continue;
					else vetor[i] = 1;
				}
			}
			
			#pragma omp barrier // estamos esperando todas as threads terminarem de atribuir os valores ao vetor			

			if(omp_get_thread_num() == 0){

				for (i = 0; i < (tam/2); i++) {				
					if(vetor[i] > maior_local)
						maior_local=vetor[i];							
				}

				omp_set_lock(&lock); // região crítica da operação, deve ser protegida pra não sobrescrever o valor do "maior" global
				if (maior_local > maior_global)
				maior_global = maior_local;
				omp_unset_lock(&lock);
			}

			else{

				for (i = (tam/2); i < tam; i++) {				
					if(vetor[i] > maior_local)
						maior_local=vetor[i];							
				}

				omp_set_lock(&lock); // região crítica da operação, deve ser protegida pra não sobrescrever o valor do "maior" global
				if (maior_local > maior_global)
				maior_global = maior_local;
				omp_unset_lock(&lock);

			}
		}

		wtime = omp_get_wtime() - wtime;
	}

	printf("PAR REDUCTION: Tam=%d, maior=%d, Elapsed wall clock time = %f  \n", tam, maior_global, wtime); //Imprime o vetor ordenado
	free(vetor);																					//Desaloca o vetor lido

	return 0;
}
