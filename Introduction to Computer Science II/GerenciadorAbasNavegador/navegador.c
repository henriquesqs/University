/*
    Programa que simula o gerenciamento de abas de um computador utilizando uma lista
    duplamente encadeada.

    Feito por: henriquesqs
*/

#include <stdio.h>
#include "list.h"
  
int main(int argc, char const *argv[]){
    
    int option;
    LIST* list = createList();

    while(1){
        scanf("%d\n", &option);

        switch(option){
            
            case 1: // abrindo nova aba
                addList(list, createNode());
            break;

            case 2: // alterando a localização da aba
                changeList(list);
            break;

            case 3: // ordenação das abas
                radixSort(list);
            break;

            case 4: // exibindo todas as abas
                printList(list);
            break;

            case 5: // "fechando" o navegador
                destroyList(list);
                return 0;
        }
    }
}