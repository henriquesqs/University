/*Arquivo de cabeçalho da biblioteca com as funções da árvore de Huffman que contêm as definições de structs e cabeçalho das 
funções utilizadas*/
/*Autores: Henrique de Souza Queiroz dos Santos - 10819029 e Witor Matheus Alves de Oliveira - 10692190*/

//dentro desta biblioteca já estão incluidos todos os tipos, classes, estrutura de dados e funções utilizados em todo o código
#include <bits/stdc++.h>

using namespace std;

//struct utilizada para criação da árvore de huffman
struct treeNode{
	string caracteres;
	int freq = 0;//guarda a frequeência do caracter
	treeNode *left = NULL, *right = NULL;

	// //sobrecarregando o operador '<' pra fazer a comparação de dois nós por frequência
	// bool operator<(treeNode *(a)) {
	// 	return (freq < (a)->freq);
	// }
};

//função para comparar os nós da arvóre por frequência, utilizada na hora de criar a min heap com os nós
bool operator1(treeNode *(a), treeNode *(b) );


//ecebe uma string com o conteúdo lido na forma de uma string, conta a frequência dos caracteres da tabela ascii simples 
//que aparecem em text e organiza uma min heap deles pela frequência contada, retornando ao fim essa min heap
priority_queue < treeNode*, vector<treeNode*>, function<bool(treeNode *, treeNode *)> > frequencyCounter(string text);

//gera uma árvore de Huffman a partir de uma floresta, sendo aqui representada por uma min heap organizada por frequência 
treeNode *createHuffmanTree(priority_queue < treeNode*, vector<treeNode*>, function<bool(treeNode *, treeNode *)> > *forest);

//busca em profundidade na árvore de huffman, que retona o código binário de cada chave que
//for encontrada na forma de uma string 
string searchHuffTree(treeNode *root, bool *find, string key);

//gera uma tabela de compressão através da busca em profundidade na árvore de Huffman 
//passada com parâmetro, onde a chave é um caracter
//retorna a tabela criada
map <char, string> createTable(treeNode *root);

//gera uma tabela de descompressão através da tabela de compressão(table), onde a chave agora será um código binário
//retona essa tabela
map <string, char> reverseTable(map <char, string> table);

//função de liberar a memória alocada pra árvore
void treeDestroier(treeNode *root);