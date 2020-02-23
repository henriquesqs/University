/*Arquivo com código fonte do projeto 2*/
/*Autores: Henrique de Souza Queiroz dos Santos - 10819029 e Witor Matheus Alves de Oliveira - 10692190*/

#include <bits/stdc++.h>

using namespace std;

//counter - função que calcula o número de combinações possíveis para subir a escada dado o vetor de restrições e retorna o número de combinações possíveis
//parâmetros:
//stairs - número de degraus da escada
//restrictions - vetor de restrições
//dp - vetor utilizado para guardar os resultados utilizados na memoization
int counter(int stairs, vector<int> restrictions, vector<int> dp){
    
	//caso base, casoo número de degruas que sobrou seja 0, significa que a combinação utlizada comnseguiu subir completamente os degraus da escada
    if(stairs == 0) return 1;
    
	//caso ainda sobre alguns degraus para subir
    else 
	if(stairs > 0){
        //se o número de combinações para um determinado número de degraus não tiver sido calculado ainda
        if(dp[stairs] == 0){
			//para cada uma das restrições que não forem maiores que o número de degrais restantes, calcula o número de 
			//combinações possíveis para esser valor e guarda no vetor de dp na posição correta
            for(int i = 0; i < restrictions.size(); ++i){
                if(restrictions[i] <= stairs) 
                    dp[stairs] += counter(stairs - restrictions[i], restrictions, dp);
            }
        }
		return dp[stairs];
    }
    
}


int main()
{
    cout << "Digite o número de degraus da escada: \n";
    int stairs;
    cin >> stairs;
    
    cout << "Digite o número de restrições:\n";
    int numRest;
    cin >> numRest;
    
    cout << "Digite as restrições:\n";
    
    vector<int> restrictions;
    restrictions.resize(numRest);
    
    for(int i = 0; i < numRest; i++) cin >> restrictions[i];
    
    vector<int> dp;
    dp.resize(stairs+1);
    
    cout << "Número de maneiras de subir a escada:\n" << counter(stairs, restrictions, dp) << "\n";

    return 0;
}
