// Membros em ordem alfabética:
// Gustavo T. Mastrobuono NUSP 10734411, 
// Henrique de S. Q. dos Santos NUSP 10819029, 
// Jhordan P. V. Pesantes NUSP 11733353, 
// Witor M. A. de Oliveira NUSP 10692190 e
// Yorvin A. R. Carrion NUSP 11733332

#include <stdio.h>
#include <omp.h>

#define T 4 // numero de threads

int main(){
    
    int i = 0, n = 0, pos = 0;

    // Esse scanf assume que os valores estão dispostos linha por linha
    // como no arquivo input.txt deixado como exemplo
    scanf("%d\n%d", &n, &pos); // le tamanho do vetor e posição de comparação

    int vet[n], menorLocal = 99999, menorGlobal = 99999;

    for(int i = 0; i < n; i++)
        scanf("%d", &vet[i]); // le e armazena valores no vetor

    // Inicializa um loop em paralelo atribuindo n/T iteracoes pra cada 
    // thread, inicializa menorLocal = 99999 em cada thread localmente
    // e compartilha a variavel menorGlobal entre os processos
    #pragma omp parallel for firstprivate(menorLocal)\
    shared(menorGlobal) schedule(dynamic, n/T)
        for(i = 0; i < n; i++){
            if((vet[i] > vet[pos]) && (vet[i] < menorLocal))
                menorLocal = vet[i];

            // Após a computação do menor local no bloco recebido pelo
            // processo, efetua a comparação com o menor global
            #pragma omp critical
                if(menorLocal < menorGlobal)
                    menorGlobal = menorLocal;
        }
    
    if(menorGlobal == 99999)
        printf("-1");
    else 
        printf("%d\n", menorGlobal);
    
    return 0;
    
}