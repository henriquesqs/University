#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

#include "tad.h"

#define DEBUG 0

bool flag = false;

int isBinaryOperator(ITEM c){

    /*
        Function to verify if a given c is a binary operator or not.

        PARAMETERS:
            - c: given char to analyse.
        RETURN:
            - 0: 'c' is not a binnary operator;
            - 1: 'c' is a binnary operator;
    */

    if (c == '+' || c == '-' || c == '*' || c == '/' || c == '^') 
        return 1; 
    
    return 0; 
}

int isUnnaryOperator(ITEM c){

    /*
        Function to verify if a given c is an unnary operator or not.

        PARAMETERS:
            - c: given char to analyse.
        RETURN:
            - 0: 'c' is not an unnary operator;
            - 1: 'c' is an unnary operator;
    */

    if (c == 'l' || c == 's' || c == 'e') 
        return 1; 
    
    return 0; 
}

void error(STACK* stack){

    /*
        Function to print an error message and read but ignore
        an line until '\n'. It also erase all the content in a stack.

        PARAMETERS:
            - stack: stack to erase its content;
    */

    printf("Expressao incorreta.\n");
    scanf("%*[^\n]\n");
    stackErase(stack);
    return;
}

int validOperator(STACK* operators, char c, char vet[]){

    /*
        Function to verify if an operator have higher priority than an
        operator that is already inside the stack. If so, we will
        just push to the operators stack. Otherwise, we will pop
        everything and push to the final stack until we find an
        operator with fewer priority.

        PARAMETERS:
            - operators: stack to verify the priorities;
            - c: caracter (operator);
            - vet: array with the priority list.

        RETURN:
            - 0: operation is not valid. We need to pop everything to push the new operator;
            - 1: operation is valid. We will just push the operator onto operators stack.
    */

    char item = stackTop(operators); // getting the top item

    if(stackEmpty(operators)) return 1;
    else if(item == '(' || item == '{' || item == '[') return 1;
    
    int j = 0; // 'j' will get the precedence of the top item
    int i = 0; // 'i' will get the precedence of the new item

    /*
        For better-understanding:
        Suppose that inside the operators stack we have '(' and '+' and
        the new item is '*'. 
        Suppose that '*' is higher-priority than '+'. So, we will just push 
        the '*' to the operators stack. 
        
        On the contrary, if '*' have fewer precedence than '+', we will 
        pop the '+' and push it into the final stack and push the '*' to 
        the operators stack.

        Suppose top item '^' and new item '-':
        
        index | 0 1 2 3 4
        item  | * + - ^ /
                      j
                    i
    */

    for(i = 0; i < 8; i++)
        if(vet[i] == c) break;
    
    for(j = 0; j < 8; j++)
        if(vet[j] == item) break;

    if(j < i) // if the top item have greater precedence than the new item
        return 0;
    else // if the top item have fewer precedence than the new item
        return 1;
}

char shuntingYard(char c, STACK* stack, STACK* operators, char vet[]){

    /*
        Function to verify if the string is well-formated.
        We are going to verify each character. More details in the code.
        If the expression is well-formated, the function will convert it
        to Reverse Polish Notation using Shunting Yard algorithm.

        PARAMETERS:
            - c: character to verify if we will push or pop;
            - stack: stack holding all the characters;
            - operators: auxiliar stack to auxiliate us;
            - vet: operators priority list.
        
        OBSERVATIONS:
            To facilitate our job, EVERY UNNARY operation will be representate as it's first letter.
            For example, if we found a "l" we know that the 2 next letters are "o" and "g". So, we
            will put it out and put the "l" into the stack to representate a log operation.

            The boolean "flag" will assure us that we are not leading with a double operator case
    */

    // Verifying if it's a number
    if(isdigit(c)){
        
        char num[20]; 
        int numSize = 0;

        double number;

        num[numSize++] = c;
        flag = false;

        while(1){ // while true
            
            scanf("%c", &c); // we read the input

            if(isdigit(c) || c == '.')  // if we found a number or a dot
                num[numSize++] = c;     // we'll store it into 'num' array

            else{ // if we found something different, we ended the number reading
                
                num[numSize] = '\0';  // indicating the end of the number
                number = atof(num);  // converting number to double
                numSize = 0;        // reseting to read other numbers

                // adding 'x' into stack to tell us that there is a double
                push(stack, 'x');

                // saving this double 'number' to solve it before
                stackAddNum(stack, number);
                break;
            }

            if(c == ',' || c == ';') return c;
        }
    }

    // Verifying if it's a unnary operator
    if(c == 'l' || c == 's' || c == 'e'){
        
        switch(c){
            case 'l':
                push(operators, c); // we push the c to the stack
                break;

            case 's':
                push(operators, c); // we push the c to the stack
                break;

            case 'e':
                push(operators, c); // we push the c to the stack
                break;
        }
    }
    
    // Verifying if it's a binary operator
    if(c == '+' || c == '-' || c == '*' || c == '/'){
        
        char str[5];

        // Converting '**' to '^'
        if (c == '*' && scanf("%[*]", str) == 1){
            if(strcmp(str, "*") == 0) c = '^';
                
            else{
                error(stack);
                stackErase(operators);
                return c;
            }
        }

        // Verifying if it's a double operator case
        if(flag == true){
            error(stack);
            stackErase(operators);
            flag = false;
            return c;
        }
        
        char item = stackTop(operators); // getting top item

        // Verifying if a higher priority operator will overlap another
        if(stackEmpty(operators) || validOperator(operators, c, vet))
            push(operators, c);

        else{
            while(!validOperator(operators, c, vet)){
                item = pop(operators);
                
                if(item != '(' && item != '{' && item != '[')
                    push(stack, item);
            }
            push(operators, c);
        }
        
        flag = true;
        return c;
    }

    // Verifying if it's a left bracket
    if(c == '(' || c == '{' || c == '[')
        push(operators, c);
    
    // Verifying if it's a right bracket
    if(c == ')' || c == '}' || c == ']'){

        char item;
        flag = false;

        switch(c){
            
            case ')':
                while(!stackEmpty(operators)){
                    item = pop(operators);

                    if(item == '[' || item == '{'){
                        error(stack);
                        stackErase(operators);
                        return c;
                    }
                    else if(item != '(') push(stack, item);
                    else return c;
                }

                // If we're here, it means that we didnt found any left bracket
                error(stack);
                stackErase(operators);
            
            break;
                
            case '}':
                while(!stackEmpty(operators)){
                    item = pop(operators);

                    if(item == '(' || item == '['){
                        error(stack);
                        stackErase(operators);
                        return c;
                    }
                    else if(item != '{') push(stack, item);
                    else return c;
                }

                // If we're here, it means that we didnt found any left bracket
                error(stack);
                stackErase(operators);
            
            break;
                
            case ']':
                while(!stackEmpty(operators)){
                    item = pop(operators);

                    if(item == '(' || item == '{'){
                        error(stack);
                        stackErase(operators);
                        return c;
                    }
                    else if(item != '[') push(stack, item);
                    else return c;
                }

                // If we're here, it means that we didnt found any left bracket
                error(stack);
                stackErase(operators);

            break;
        }
    }

    flag = false;
    return c;
}