/*Arquivo util onde estão implementadas algumas funções necessárias para esta implementação, como leitura de arquivo algoritmo 
de compressão e descompressão utilizados e funções para conversçoes (binário <-> char) necesárias*/
/*Autores: Henrique de Souza Queiroz dos Santos - 10819029 e Witor Matheus Alves de Oliveira - 10692190*/

#include "util.hpp"

//lê byte a byte um arquivo com o nome contido em filename e retorna uma string com o conteúdo do arquivo
string readFile(string fileName, bool *error){
	string text;
	char aux;
	ifstream file;
	file.open(fileName);

	if(file.is_open()){
		//lendo do arquivo enquanto ele n acabar
		while(file.read(&aux, 1)) text += aux;
		file.close();
	}else {
		*error = true;
	}
	return text;
}

//converte uma string de tamanho 8 (1 byte), que representa um número binário em um caracter
char binaryStringToChar(string value){
	char aux = 0;
	for (int i = 0; i < value.length(); ++i) aux += (value[(value.length()-1) - i] - 48) * pow(2, i);
	return aux;
}

//converte um caracter em um valor binário representado em uma string
string charToBinaryString(char c) {
	string value;
    for (int i = 7; i >= 0; --i) value += ((c & (1 << i))? '1' : '0');
    return value;
}

//gera um novo arquivo de nome em fileName, escreve o conteúdo do arquivo a ser comprimido(text) 
//codificado pela tabela de compressão(table) em binário, sendo que para fazer isso acumula os 
//valores em binário seguindo em uma string de 8 posições e esta quando totalmente preenchida é 
//convertido em um char que é escrito no arquivo, isso se reprete até terminar o código binário 
//gerado pela codificaçãod de text 
void generateCompressedFile(string fileName, string text, map<char, string> table, bool *error, int *tam){
	ofstream file;
	file.open(fileName, ofstream::binary);
	string aux, aux1;
	aux = "00000000";
	int j = 0;

	char c;

	if(file.is_open()){
		//iterador pra pegar o valor retornado pela busca na tabela
		map<char, string>::iterator itr;

		//para cada caracter no conteúdo do arquivo lido busca ele na tabela e escreve o seu código no arquivo comprimido
		for (int i = 0; i < text.length(); ++i){
			
			//buscando pelo caracter na tabela
			itr = table.find(text[i]);
			if(itr != table.end()){				
				for (int k = 0; k < itr->second.length(); ++k){					
					//mexendo com uma string[8] pra dps converter em um char e escrever

					if(j < 8){//se ainda não tiver completado 1 byte com dados úteis
						aux[j] = table[(int)text[i]][k];
						j++;
					}else{//caso tenha completado 1 byte de dados úteis
						//converte ele pra char e escreve ele
						c = binaryStringToChar(aux);
						file << c;
						(*tam)++;
						
						//reiniciando aux e atualizando que ele não tem nada escrito ainda
						aux = "        ";
						j = 0;

						//o próximo bit é escrito em aux novamente, iniciando assim um novo byte armazenado em aux
						aux[j] = table[(int)text[i]][k];
						j++;
					}
				}

				//se for o último byte gerado pela codificação do texto e ele não tiver sido
				//preenchido por completo com caracteres úties na codificação
				if(i == text.length() - 1 && j < 8){
					for (int i = j; i < 8; ++i) aux[i] = '0';
					//converte ele pra char e escreve ele
					c = binaryStringToChar(aux);
					file << c;
					(*tam)++;

					//j representa o número de bits úteis na compressão e que consequentemente serão úteis 
					//na descompressão, mas por não conseguir escrver bit a bit, somos obrigados a escrever 
					//um byte completo mesmo quem nem todos os bits dele sejam úteis para o programa, para
					//resolver isso, não ler os bits execedentes na descompressão e não descomprimir errado, 
					//escrevemos um byte a mais no arquivo, sendo que ele representa o número de bits não 
					//utilizados no último byte escrito antes dele
					c = 8 - j;
					file << c;	
					(*tam)++;
				}		

			}
		}

	}else{
		*error = true;
		cout  << "Erro na abertura do arquivo a ser comprimido!!!";
	}
}

//lê o arquivo comprimido de nome contido em filename, decodifica os bytes lidos dele com a 
//ajuda da tabela de descompressão(rTable) no conteúdo original do arquivo passado para ser
//comprimido e retorna o conteúdo decodificado na forma de uma string
string decompressFile(string fileName, map<string, char> rTable, bool *error){
	//lendo arquivo comprimido
	string text = readFile(fileName, error);

	if(*error == true){
		cout  << "Erro na abertura do arquivo a ser descomprimido!!!";
		return "";
	}

	//convertendo o conteúdo lido em valor binário
	string binario;
	for (int i = 0; i < text.length(); ++i) binario += charToBinaryString(text[i]);

	//o último caracter escrito no arquivo indica quantos bits representam dados úteis referentes ao arquivo 
	//comprimido, isto teve de ser feito, pois é possível realizar a escrita de no mínimo 1 byte no arquivo, 
	//e ao mesmo tempo na hora de gerar o código do arquivo comprimido, não necessariamente o tamanho dos bits
	//serão múltiplos de 1 byte, podendo assim sobrar alguns bits não úteis na descompressão, mas que tiveram 
	//de ser escritos no arquivo devido ás limitações do sistema de output
	int lastUsefulBits;
	if(text[text.length()-1] != 0) lastUsefulBits = text[text.length()-1];

	//iterador pra pegar o valor retornado pela busca na tabela
	map<string, char>::iterator itr;
	string auxKey, textFinal;

	//aqui seleciona n bits da string lida do arquivo comprimido e realiza a busca desses n bits na forma de uma 
	//string na tabela de descompressão até encontrar um caracter correspondente nela, quando a busca obtêm sucesso 
	//a próxima string a ser buscada parte do bit posterior a string com busca bem sucedida

	//o 8 somado a lastUsefulBits se refere ao próprio byte que representa o valor de lastUselBits
	for (int i = 0; i < binario.length()-(lastUsefulBits+8); ++i){
		//j começa do 1, pq estamos usando no método substr, onde o segundo parametro é o número 
		//de caracteres lidos a partir da posição indicada pelo primeiro parâmetro nela
		for (int j = 1; j < binario.length()-(lastUsefulBits+8); ++j){
			auxKey = binario.substr(i, j);
			
			//buscando pelo valor binário na tabela de descompressão
			itr = rTable.find(auxKey);
			if(itr != rTable.end()){
				//se encontrou uma chave de i até j, agr tem q pesquisar de j pra frente, 
				//lembrando que i é a posição incial pra buscar uma substring
				i += j - 1;

				//colocando o caracter na string que representa o conteúdo do arquivo descomprimido
				textFinal += itr->second;
				break;
			}
		}
	}
	return textFinal;
}