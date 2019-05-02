/*
 
 Programa de recomendação e predição de filmes e notas, respectivamente, baseando-se em usuários com gostos parecidos.
 Feito por:	
  _                     _                                 
 | |__   ___ _ __  _ __(_) __ _ _   _  ___  ___  __ _ ___ 
 | '_ \ / _ \ '_ \| '__| |/ _` | | | |/ _ \/ __|/ _` / __|
 | | | |  __/ | | | |  | | (_| | |_| |  __/\__ \ (_| \__ \
 |_| |_|\___|_| |_|_|  |_|\__, |\__,_|\___||___/\__, |___/
                             |_|                   |_|    
	Aluno de Bacharelado em Ciências de Computação 
		   Universidade de São Paulo (USP) - São Carlos/SP
*/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main(int argc, char const *argv[])
{
	bool NotaCalculada = false;
	int users, itens;
	float limiar;

	scanf("%d%d%f", &users, &itens, &limiar);

	int matriz[users][itens];

	/* 
	O bloco lógico "for" irá percorrer a matriz 
	preenchendo-a com os valores dados no input 
	*/

	for (int j = 0; j < users; j++)
	{

		for (int k = 0; k < itens; k++)
		{

			scanf("%d", &matriz[j][k]);
		}
	}

	float similaridade = 0, numerador = 0, denominador = 0, raiz1 = 0, raiz2 = 0;
	float Nota = 0, somatorioVotosComZero = 0, media_fixa = 0, media_usuario = 0, variacao_s = 0, numeradorNota = 0;
	float linha0 = 0, somatoriaSimi = 0, votosContabeis = 0, somatorioVotosSemZero = 0;

	for (int x = 0; x < users; x++)
	{

		if (NotaCalculada == true)
		{
			printf("\n");
			NotaCalculada = false;
		}
		for (int z = 0; z < itens; z++)
		{

			/*
			Para fazermos a predição da nota de determinado usuário,
			primeiro precisamos descobrir quais usuários ainda não
			deram nota para algum filme, ou seja, usuários com notas
			iguais a 0. A seguir, iremos procurar valores iguais a 0 na matriz
			*/

			if (matriz[x][z] == 0)
			{
				linha0 = 0;
				somatorioVotosComZero = 0;

				for (int linha = 0; linha < itens; linha++)
				{

					if (matriz[x][linha] == 0)
					{

						linha0++;
					}

					somatorioVotosComZero += matriz[x][linha];
					media_fixa = somatorioVotosComZero / (itens - linha0);

					/*
					Para deixar claro:
					A media_fixa é igual ao somatório das notas 
					dividido pela quantidade total de itens 
					menos a quantidade de itens iguais a '0', já 
					que esses não entram na média
					*/
				}

				/*
				O bloco lógico (for) a seguir, referente ao inteiro L, irá calcular todas as operações
				a seguir antes da linha a ser analisada, a que possui uma nota ainda não computada.
				*/

				for (int L = 0; L < users && L != x; L++)
				{

					similaridade = 0;
					numerador = 0;
					raiz1 = 0;
					raiz2 = 0;
					votosContabeis = 0;
					somatorioVotosSemZero = 0;

					/*
					A similaridade será calculada, a seguir, utilizando a
					função cosseno que foi fornecida nas instruções do
					exercício
					*/

					for (int M = 0; M < itens; M++)
					{

						if (matriz[L][z] != 0)
						{
							numerador += matriz[x][M] * matriz[L][M];

							raiz1 += pow(matriz[x][M], 2);
							raiz2 += pow(matriz[L][M], 2);

							denominador = sqrt(raiz1) * sqrt(raiz2);

							similaridade = numerador / denominador;

							if (matriz[L][M] != 0) // Buscando todos os votos com excessão dos '0's
							{

								votosContabeis++;
							}
							somatorioVotosSemZero += matriz[L][M];
							media_usuario = somatorioVotosSemZero / votosContabeis; // A media_usuario é a media aritmética dos votos do usuário
						}
					}

					/*
					Para a predição da nota, devemos encontrar usuários com votos (gostos)
					similares ao usuário que ainda não deixou sua nota para determinado filme.
					Isso será feito com a ajuda do limiar fornecido no input. Segue, então: 
					*/

					if (limiar < similaridade)
					{

						somatoriaSimi += fabs(similaridade);

						variacao_s += similaridade * (matriz[L][z] - media_usuario);

						numeradorNota = media_fixa + (variacao_s / somatoriaSimi);

						Nota = numeradorNota;
					}

					if (L + 1 == users)
					{
						NotaCalculada = true;
					}
				}

				/*
				Esse segundo bloco lógico "for" relacionado ao inteiro L, apesar de parecer repetido,
				irá calcular todas as operações das linhas após a linha analisada, ou seja, a 
				linha que contém um voto não computado (0)
				*/

				for (int L = x + 1; L < users && L != x; L++)
				{

					similaridade = 0;
					numerador = 0;
					raiz1 = 0;
					raiz2 = 0;
					votosContabeis = 0;
					somatorioVotosSemZero = 0;

					for (int M = 0; M < itens; M++)
					{

						if (matriz[L][z] != 0)
						{

							numerador += matriz[x][M] * matriz[L][M];

							raiz1 += pow(matriz[x][M], 2);
							raiz2 += pow(matriz[L][M], 2);

							denominador = sqrt(raiz1) * sqrt(raiz2);

							similaridade = numerador / denominador;

							if (matriz[L][M] != 0) // Buscando todos os votos com excessão dos '0's
							{
								votosContabeis++;
							}
							somatorioVotosSemZero += matriz[L][M];
							media_usuario = somatorioVotosSemZero / votosContabeis; // A media_usuario é a media aritmética dos votos do usuário
						}
					}

					if (limiar < similaridade) // bloco "if" que seleciona usuários com gostos parecidos ao usuário que queremos predizer a nota
					{

						somatoriaSimi += fabs(similaridade);

						variacao_s += similaridade * (matriz[L][z] - media_usuario);

						numeradorNota = media_fixa + (variacao_s / somatoriaSimi);

						Nota = numeradorNota;
					}

					if (L + 1 == users)
					{
						NotaCalculada = true;
					}
				}

				/*
				Finalizando o código, a nota prevista para o usuário será printada caso ela seja maior que 0.
				Do contrário, significa que não existem dados suficientes para a previsão da nota a ser dada
				pelo usuário, portanto, Dados Insuficientes (DI) será printado.
				*/

				if (Nota > 0)
				{
					printf("%.2f ", Nota);
				}
				else
				{
					printf("DI ");
				}

				Nota = 0;
				somatorioVotosComZero = 0;
				media_fixa = 0;
				media_usuario = 0;
				variacao_s = 0;
				numeradorNota = 0;
				linha0 = 0;
				somatoriaSimi = 0;
				votosContabeis = 0;
				somatorioVotosSemZero = 0;
			}
		}
	}

	return 0;
}