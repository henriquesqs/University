#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "list.h"

struct node{
    
    char title[31];   // maximo de 30 letras
    char url[1025];   // maximo de 1024 letras

    int day;
    int month;
    int hour;
    int min;
    int position;
    int key;
    
    NODE* next;       // ponteiro para a proxima guia
    NODE* previous;   // ponteiro para a guia anterior
};

struct list {

    NODE* start;
    NODE* end;
    
    int max;          // variável que guarda a maior chave na lista
    int size;        // variável que guarda o tamanho da lista
};

LIST* createList(){

    /*
        Função responsável pela criação e alocação de um novo ponteiro para LIST.

        RETORNO:
            - l: ponteiro para LIST recém criado.
    */

    LIST* list = (LIST*) malloc(sizeof(LIST));
    
    if(list != NULL){
        list->start = NULL;
        list->end = NULL;
        list->size = 0;
        list->max = 0;
    }

    return list;
}

NODE* createNode(){

    /*
        Função responsável pela criação do nó e recebimento de
        seu conteúdo.

        RETORNO:
            - node: recém criado nó;
    */

    NODE* node = (NODE*) malloc(sizeof(NODE));
        
    // Copiando informações para o novo nó (nova aba)
    scanf("%30[^\n]\n", node->title); // lendo o título da aba
    scanf("%1024[^\n]\n", node->url); // lendo a url do site
    scanf("%d%d%d%d", &node->day, &node->month, &node->hour, &node->min);

    return node;
}

void destroyList(LIST* list){

    /*
        Função responsável por apagar por completo uma lista 
        (liberação do espaço alocado) e seu conteúdo.

        PARAMETROS:
            - list: ponteiro para LIST que o usuário deseja apagar.
    */

    NODE* aux = list->start;
    
    while (aux != NULL) {

        NODE* item = aux;
        aux = aux->next;
        free(item);
    }

    free(list);
}

void addList(LIST* list, NODE* node){

    /*
        Função responsável por adicionar uma nova aba a uma determinada lista.
        
        PARAMETROS:
            - list: ponteiro para a lista que o usuário deseja adicionar um item;
            - node: 'aba' que será adicionada na lista.
            
    */

    // Gerando a chave que será usada em uma eventual busca
    char str[10];
    sprintf(str, "%02d%02d%02d%02d", node->month, node->day, node->hour, node->min);

    // Convertendo a chave para um número inteiro
    node->key = atoi(str);

    // Verificando (e atualizando, se necessário) o maior valor entre as chaves
    if(list->max < node->key) list->max = node->key;

    // Condições para a adição de uma nova aba
    if(list != NULL){
        
        // se a lista estiver vazia
        if(list->start == NULL){
            
            list->start = node;
            node->previous = NULL;
        }
        
        // se a lista não estiver vazia
        else{ 
            
            list->end->next = node;
            node->previous = list->end;
            node->next = NULL;
        }
    
        // Atualizando ponteiros da lista
        list->end = node;
        list->size++;
        node->position = list->size; // a posição do nó é o tamanho da lista depois do incremento

        return;
    }

    else printf("deu ruim");
    return;
}

void printList(LIST* list){

    /*
        Função para exibir na tela a lista atual de abas

        PARAMETROS:
            - list: ponteiro para a lista de abas atuais.

    */

    NODE* aux = list->start;
    
    while (aux != NULL) {

        printf("%s %s %.2d/%02d %02d:%02d\n", aux->title, aux->url, aux->day, aux->month, aux->hour, aux->min);
        aux = aux->next;
    }
    
    printf("\n");
}

int sizeList(LIST* list){

    /*
        Função para verificar e retornar o tamanho de 'list'
        
        PARAMETROS:
            - list: ponteiro para LIST.
        
        RETORNO:
            - list->size: tamanho da lista.
    */
    
    return list->size;
}

int getMax(LIST* list){
    
    /*
        Função para verificar qual a maior chave na lista.

        PARAMETROS:
            - list: ponteiro para LIST.
        
        RETORNO:
            - list->max: maior chave dentro da lista.
    */

    return list->max;
}

void fixPosition(LIST* list){
    
    /*
        Função para reorganizar as posições das abas
        dentro da lista.

        PARAMETROS:
            - list: ponteiro para LIST. 
    */

    NODE* aux = list->start;

    for(int position = 1; aux != NULL; position++){
        aux->position = position;
        aux = aux->next;
    }
}

void changeList(LIST* list){

    /*
        Funcao que altera a localização de uma aba aberta.

        PARAMETROS:
            - list: ponteiro para LIST.
        
    */

    char title[31];
    int position;
    bool found = false;

    // Recebendo informações para a alteração da aba
    scanf("%30[^\n]\n", title);
    scanf("%d\n", &position);

    NODE *tab, *aux; // 'tab' irá armazenar a aba que queremos mover

    // Laço que busca a aba que queremos mover
    aux = list->start;
    while(aux != NULL){
        
        // Verificando se achamos a aba que queremos
        if(strcmp(aux->title, title) == 0){
            found = true;
            tab = aux;
            
            // Verificando se aux não está no começo/fim da lista
            if(aux->previous != NULL) aux->previous->next = aux->next;
            if(aux->next != NULL) aux->next->previous = aux->previous;
            
            // Verificando se a aba que queremos está no começo ou no fim da lista
            if (tab == list->start) list->start = tab->next;
            if (tab == list->end) list->end = tab->previous;

            // Apagando o restante das informações da aba
            aux->previous = NULL;
            aux->next = NULL;
            list->size--;

            break;
        }
        else aux = aux->next;
    }

    // Verificando se, de fato, encontramos a aba
    if(found == false) return;

    // Verificando se a nova posição excede a quantidade de abas
    if(position > list->size){
        
        addList(list, tab); // se exceder, devemos apenas adicionar no final da lista
        fixPosition(list); // organizando as posições das abas
        return;
    }

    // Laço que busca a posição onde queremos inserir a nova aba
    aux = list->start;
    while(aux != NULL){
        
        // Verificando se encontramos a posição para onde devemos mover a aba
        if(aux->position == position){

            // Devemos 'mover' todas as abas seguintes para a direita
            list->size++;
            tab->next = aux;
            if (aux->previous != NULL) tab->previous = aux->previous;
            
            aux->previous = tab;

            if(aux == list->start) list->start = tab;
            
            if(tab->previous != NULL) tab->previous->next = tab;
            
            fixPosition(list); // arrumando as novas posições

            break;
        }
        else aux = aux->next;
    }
}

void radixSort(LIST* list){

    /*
        Função de ordenação utilizando o Radix Sort.
        Para facilitar a ordenação da lista duplamente encadeada,
        o algoritmo Bucket Sort foi utilizado como sub-rotina.

        PARAMETROS:
            - list: ponteiro para LIST.
    */

    int i, exp = 1;
    int size = sizeList(list);
    int max = getMax(list);

    NODE* tmp;
    NODE* aux[size];

    while( max/exp > 0 ){
        
        int bucket[10] = {0}; // bucket com 10 posições (0-9)
        tmp = list->start;
        
        // Contador da ocorrência dos dígitos menos significativos
        for(i = 0; i < size; i++, tmp = tmp->next)
            bucket[ (tmp->key / exp) % 10 ]++;

        // Verificando referência de onde armazenar o número
        for(i = 1; i < 10; i++)
            bucket[i] += bucket[i-1];
        
        tmp = list->end;

        // Buscando onde armazenar o nó temporário
        for(i = size-1; i >= 0; i--, tmp = tmp->previous)
            aux[--bucket[ (tmp->key / exp) % 10]] = tmp;
        
        // Reorganizando os ponteiros 'next' e 'end' do ponteiro para LIST
        for(i = 0; i < size; i++){
            
            // se estivermos no começo da lista
            if(i == 0){
                list->start = aux[i];
                list->start->previous = NULL;
                list->end = aux[i];
            }
            else{
                aux[i]->previous = aux[i-1];
                aux[i]->next = NULL;
                aux[i-1]->next = aux[i];
                list->end = aux[i];
            }
        }

        // Verificando os próximos bits
        exp *= 10;
    }
}