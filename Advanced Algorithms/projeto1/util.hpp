/*Arquivo de cabeçalho do arquivo util.cpp onde estão as inclusões de bibliotecas necessárias além dos cabeçalhos das funções utilizadas*/
/*Autores: Henrique de Souza Queiroz dos Santos - 10819029 e Witor Matheus Alves de Oliveira - 10692190*/

#include <bits/stdc++.h>
using namespace std;


//lê byte a byte um arquivo com o nome contido em filename e retorna uma string com o conteúdo do arquivo
string readFile(string fileName, bool *error);

//converte uma string de tamanho 8 (1 byte), que representa um número binário em um caracter
char binaryStringToChar(string value);

//converte um caracter em um valor binário representado em uma string
string charToBinaryString(char c);

//gera um novo arquivo de nome em fileName, escreve o conteúdo do arquivo a ser comprimido(text) 
//codificado pela tabela de compressão(table) em binário, sendo que para fazer isso acumula os 
//valores em binário seguindo em uma string de 8 posições e esta quando totalmente preenchida é 
//convertido em um char que é escrito no arquivo, isso se reprete até terminar o código binário 
//gerado pela codificaçãod de text 
void generateCompressedFile(string fileName, string text, map<char, string> table, bool *error, int *tam);

//lê o arquivo comprimido de nome contido em filename, decodifica os bytes lidos dele com a 
//ajuda da tabela de descompressão(rTable) no conteúdo original do arquivo passado para ser
//comprimido e retorna o conteúdo decodificado na forma de uma string
string decompressFile(string fileName, map<string, char> rTable, bool *error);
