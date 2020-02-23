#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

#include "tad.h"

#define DEBUG 0
#define ERRO -404

bool stop = false;

int main(int argc, char const *argv[]){

    char ret, c, operation; // 'ret' is the return of shuntingYard and 'c' is the character
    char vet[11]; // 'vet' is the priority list

    STACK* stack = stackCreate(); // creating a stack to receive the Reverse Polish Notation (RPN)
    STACK* operators = stackCreate(); // creating a stack to auxiliate us

    vet[0] = 's'; vet[1] = 'l'; vet[2] = 'e'; // 'sqrt', 'log' and 'exp' operations will receive higher priority

    // Reading the priority list of operators
    for(int i = 3; i < 8; i++){
        scanf("%c\n", &operation);

        // Converting '**' to '^'
        if(operation == '*' && vet[i-1] == '*'){
            vet[i-1] = '^';
            i--;
        }
        else vet[i] = operation;
    }
    
    // Reading expressions char by char
    while(scanf("%c", &c) == 1){
        
        if(c != ',' && c != ';') 
            ret = shuntingYard(c, stack, operators, vet); // searching for errors + converting to RPN
        
        if (c == ',' || c == ';' || ret == ',' || ret == ';'){ // end of the current expression
            while(!stackEmpty(operators)){
                char item = pop(operators);

                if(item == '[' || item == '(' || item == '{'){
                    error(stack);
                    stackErase(operators);
                    stop = true;
                    break;
                }
                else push(stack, item); // finishing RPN
            }
            
            if(stop == true) continue;

            NODE* root = buildTree(root, stack, pop(stack)); // building the tree
            
            double result = solveTree(root, stack); // solving the tree

            if(result != ERRO && !isnan(result)) printf("%.2lf\n", result);
            else error(stack);

            destroyTree(root); // destroying tree to analyse next expression
            stackErase(stack); // same here
        }
        stop = false;
    }

    destroyStack(stack);    
    destroyStack(operators);    
    
    return 0;
}
