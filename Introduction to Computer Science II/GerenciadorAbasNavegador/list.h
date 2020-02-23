#ifndef LIST_H
#define LIST_H
#define ITEM

typedef struct node NODE;
typedef struct list LIST;

// Funcao de criação de um novo nó
NODE* createNode();

// Funcao que aloca, inicia e retorna um ponteiro para LIST
LIST* createList();

// Funcao responsavel por limpar (liberar memoria) de um ponteiro "l" para LIST
void destroyList(LIST* list);

// Funcao que adiciona itens a lista, cada um com seus parametros enviados pela main. Ex : nome, chave.
void addList(LIST* list, NODE* node);

// Imprime a lista completa, com codigo, nome, relevancia e link;
void printList(LIST* list);

// Funcao que retorna o tamanho de uma lista
int sizeList(LIST* list);

// Funcao que retorna o maior valor dentro de uma lista
int getMax(LIST* list);

// Funcao que altera a posição de uma aba
void changeList(LIST* list);

// Funcao de ordenação 'Radix Sort'
void radixSort(LIST* list);

#endif