/*Arquivo com a função main que só faz a leitura dos nomes dos arquivos e faz a chamada das funções para compressão 
de descompressão dos arquivos*/
/*Autores: Henrique de Souza Queiroz dos Santos - 10819029 e Witor Matheus Alves de Oliveira - 10692190*/

#include "huffTree.hpp"
#include "util.hpp"

int main(){
	string fileIn, fileOut;
	cout << "Digite o nome do arquivo de texto a ser comprimido: ";
	getline(cin, fileIn);

	cout << "Digite o nome do arquivo comprimido que será gerado: ";
	getline(cin, fileOut);

	//variável para verificação de erros na abertura de arquivos
	bool error = false;

	//armazena o conteúdo lido do arquivo a ser comprimido na forma de uma string que será reaproveitada posteriormente
	string text = readFile(fileIn, &error);

	if(error == false){
		//contando a frequencia dos caracteres já lidos e organizando os caracteres em uma min-heap por frequência
		priority_queue < treeNode*, vector<treeNode*>, function<bool(treeNode *, treeNode *)> > queue1(operator1);
		queue1 = frequencyCounter(text);

		//gera a árvore de Huffman a partir da frequencia dos caracteres lidos do arquivo de entrada
		treeNode *huffTree = createHuffmanTree(&queue1);

		//gerando a tabela pra compressão a partir da árvore de Huffman já criada, onde as chaves são os caracteres em 
		//ascii e os valores são as strings binárias geradas da busca na árvore de huffman
		map <char, string> table = createTable(huffTree);
		
		//gera o arquivo comprimido de nome contido em fileOut
		cout << "Gerando o arquivo" << fileOut << "\n";
		int tam = 0;
		generateCompressedFile(fileOut, text, table, &error, &tam);

		if(error == true) return 0;
		

		//chama a função de descompressão do arquivo comprimido, o segundo argumento é a tabela de compressão reversa,
		//onde as chaves são as strings binárias e os valores os caracteres em ascii
		cout << "Descomprimindo o arquivo" << fileOut << "\n";
		string decompressedText = decompressFile(fileOut, reverseTable(table), &error);

		if(error == true) return 0;


		//gera um arquivo com o conteúdo descomprimido que pode ser utilizado para a comparação com o arquivo original 
		//para a verificação do correto funcionamento do código

		//pegando o nome do arquivo de entrada excluso a terminação ".txt"
		string name = fileIn.substr(0, fileIn.length() - 4) + "PraComparar.txt";
		
		cout << "Gerando arquivo para comparação chamado: " << name << "\n";

		ofstream file;	
		file.open(name);
		file << decompressedText;

		cout << "Tamanho do arquivo de entrada: " << text.length() << " bytes" << "\n";
		cout << "Tamanho do arquivo comprimido: " << tam << " bytes" << "\n";

		cout << "Tudo certo. Até mais!" << "\n";

		//libera a memória alocada dinamicamente
		treeDestroier(huffTree);
	}

	return 0;

}