/*Arquivo que contêm as funções utilizadas para operações com a árvore de Huffman gerada*/
/*Autores: Henrique de Souza Queiroz dos Santos - 10819029 e Witor Matheus Alves de Oliveira - 10692190*/

#include "huffTree.hpp"

//função para comparar os nós da arvóre por frequência, utilizada na hora de criar a min heap com os nós
bool operator1(treeNode *(a), treeNode *(b) ) {
	return ((a)->freq > (b)->freq);
}

//recebe uma string com o conteúdo lido na forma de uma string, conta a frequência dos caracteres da tabela ascii simples 
//que aparecem em text e organiza uma min heap deles pela frequência contada, retornando ao fim essa min heap
priority_queue < treeNode*, vector<treeNode*>, function<bool(treeNode *, treeNode *)> > frequencyCounter(string text){
	
	//criando um vetor de ponteiros pros nós da árvore
	vector <treeNode *> vetAux;
	vetAux.resize(256);//tamanho da tabela ascii simples

	//contando a aparição de cada caracter da entrada
	for (int i = 0; i < text.length(); ++i){
		if(vetAux[(int)text[i]] == NULL){
			vetAux[(int)text[i]] = new treeNode;
			vetAux[(int)text[i]]->caracteres = text[i];
			vetAux[(int)text[i]]->freq++;
		}else vetAux[(int)text[i]]->freq++;
	}	

	//criando a min_heap de acordo com a frequência da aparição dos caracteres
	priority_queue < treeNode*, vector<treeNode*>, function<bool(treeNode *, treeNode *)> > queue1(operator1);

	//inserindo os nós nela
	for (int i = 0; i < 256; ++i) if(vetAux[i] != NULL) queue1.push(vetAux[i]);

	return queue1;
}

//gera uma árvore de Huffman a partir de uma floresta, sendo aqui representada por uma min heap organizada por frequência 
treeNode *createHuffmanTree(priority_queue < treeNode*, vector<treeNode*>, function<bool(treeNode *, treeNode *)> > *forest){
	treeNode *aux, *aux1, *aux2;

	//enquanto a floresta não ter apenas uma árvore
	while(forest->size() > 1){
		//alocando um novo nó para ser pai dos dois nós de menor frequência
		aux = new treeNode;

		//tirando os dois elementos de menor frequência
		aux1 = forest->top();
		forest->pop();
		aux2 = forest->top();
		forest->pop();

		//juntando os dois nós em um nó só, como sendo filhos do nó alocado
		aux->left = aux1;
		aux->right = aux2;
		aux->freq = aux1->freq + aux2->freq;

		aux1 = aux2 = NULL;
		//reinsere a árvore criada na floresta inicial
		forest->push(aux);
	}

	return aux;
}

//busca em profundidade na árvore de huffman, que retona o código binário de cada chave que
//for encontrada na forma de uma string 
string searchHuffTree(treeNode *root, bool *find, string key){
	//cout << "dentro da busca, key: " << key << "\n";
	string aux = "";
	//caso tenha nó raíz
	if(root != NULL){
		if(key.compare(root->caracteres) != 0){
			//*find = false;
			//se ainda não encontrou a chave e existe nó filho esquerdo, chama a busca recursivamente para ele
			if(!(*find) && root->left != NULL) {
				aux += searchHuffTree(root->left, find, key);
				if(*find) aux += "0";
			}

			//se ainda não encontrou a chave e existe nó filho direito, chama a busca recursivamente para ele
			if(!(*find) && root->right != NULL) {
				aux += searchHuffTree(root->right, find, key);
				if(*find) aux += "1";
			}
		}else {
			//caso tenha encontrado a chave
			*find = true;
			return aux;
		}
	}
	//retora a string vazia caso não tenha encontrado a chave na árvore
	return aux;
}

//gera uma tabela de compressão através da busca em profundidade na árvore de Huffman 
//passada com parâmetro, onde a chave é um caracter
//retorna a tabela criada
map <char, string> createTable(treeNode *root){
	//gerando uma tabela de compreessão com a key sendo os caracteres ascii e  o valor a string gereado pra busca na árvore de huffman
	map <char, string> table;
	
	//auxiliar pra gerar o código de cada caracter da tabela ascii
	string aux, aux1;

	bool find = false;

	char c;
	for (int i = 0; i < 256; ++i){
	 	c = (char)i;
	 	aux = c;
	 	aux1 = searchHuffTree(root, &find, aux);

	 	if(aux1.compare("") != 0){
	 		reverse(begin(aux1), end(aux1));
	 		table.insert( pair<char, string>(aux[0], aux1)  );
		 	find = false;
	 	}

	}
	return table;
}

//gera uma tabela de descompressão através da tabela de compressão(table), onde a chave agora será um código binário
//retona essa tabela
map <string, char> reverseTable(map <char, string> table){
	map <string, char> rTable;

	map<char, string>::iterator itr; 
    for (itr = table.begin(); itr != table.end(); ++itr) rTable.insert( pair<string, char>(itr->second, itr->first)  ); 

   return rTable;
}

//função de liberar a memória alocada pra árvore
void treeDestroier(treeNode *root){
	if(root->left != NULL) treeDestroier(root->left);
	if(root->right != NULL) treeDestroier(root->right);
	delete root;
	return;
}