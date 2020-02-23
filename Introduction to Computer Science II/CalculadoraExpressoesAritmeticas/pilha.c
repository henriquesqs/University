#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

#include "tadPilha.h"

#define DEBUG 0
#define ITEM char

struct stack{
    ITEM content[TAM]; // array with ITEM
    int size; // size of 'content' array

    double num[TAM]; // array with double
    int numSize; // size of 'num' array
};

STACK* stackCreate(){

    /*
        Function to create a pointer to STACK.
        
        RETURN:
            - stack: allocated and initialized stack.
    */

    STACK* stack = (STACK*) malloc(sizeof(STACK));
    
    if(stack != NULL) {
        stack->size = 0;
        stack->numSize = 0;
    }
    
    else printf("Erro on creating the stack");

    return stack;

}

STACK* stackInvert(STACK* stack){

    /*
        Function to invert the content in a stack.

        PARAMETERS:
            - stack: stack to invert its content.
        RETURN:
            - aux: inverted stack.
    */

    STACK* aux = stackCreate();

    while(!stackEmpty(stack)){
        char item = pop(stack);
        push(aux, item);
    }

    return aux;
}

ITEM pop(STACK* stack){

    /*
        Function to pop a item from the top of a stack.
        
        PARAMETERS:
            - stack: stack sent to pop its top item.
        RETURN:
            - item: popped item;
    */

    ITEM item;

    if(stack != NULL && !stackEmpty(stack)){
        item = stack->content[stack->size-1];
        stack->size--;
        // printf("Top item, %c, sucessfully pop off the stack\n\n", item);
        return item;
    }
    // printf("Error on poping the top item\n");
}

ITEM stackTop(STACK* stack){    

    /*
        Function to verify what's on stack top;

        PARAMETERS:
            - stack: stack to verify its top content;
        RETURN:
            - top item from the stack;
    */
   
    return stack->content[stack->size-1];
}

int push(STACK* stack, ITEM item){

    /*
        Function to push an item in a stack top.
        
        PARAMETERS:
            - stack: stack sent to check if it's empty;
            - item: the item that was sent to be push on the top;
        RETURN:
            - 1: if we successfully push the item;
            - 0: if we failed to push the item.
    */

    if(stack != NULL && !stackFull(stack)){

        stack->content[stack->size] = item;
        stack->size++;
        // printf("Item %c sucessfully pushed to the stack\n\n", stack->content[stack->size-1]);
        return 1;
    }
    // printf("Error on pushing the item %c\n", item);
    return 0;
}

int stackEmpty(STACK* stack){

    /*
        Function to check if a stack is empty or not.
        
        PARAMETERS:
            - stack: stack sent to check if it's empty.
        RETURN:
            - 1: stack is empty;
            - 0: stack is not empty.
    */

    if(stack->size == 0){
        // printf("Stack is empty");
        return 1;
    }
    else{
        // printf("Stack is not empty");
        return 0;
    }

}

int stackFull(STACK* stack){

    /*
        Function to check if a stack is full or not.
        
        PARAMETERS:
            - stack: stack sent to check if it's full.
        RETURN:
            - 1: stack is full;
            - 0: stack is not full.
    */

    if(stack->size == TAM) return 1;
    else return 0;
}

void stackErase(STACK* stack){

    /* 
        Function to erase the content in a stack.

        PARAMETERS:
            - stack: stack to erase all of its content.
    */

    stack->size = 0;    
    stack->numSize = 0;
}

void stackPrint(STACK* stack){

    /*
        Function to print the content in a stack;

        PARAMETERS:
            - stack: stack to print its content;
    */

    printf("\nsize: %d\n", stack->size);
    for(int i = stack->size-1; i >= 0; i--) 
        printf("item: %c\n", stack->content[i]);
    
    return;
}

void stackAddNum(STACK* stack, double num){

    /* 
        Function to add a double to 'num' array in stack.
        We're doing this because STACK holds 'ITEM' content, but
        we need to save a double number.

        PARAMETERS:
            - stack: stack to store the number;
            - num: double number to store.
    */
    
    stack->num[stack->numSize++] = num;
}

double toDouble(STACK* stack){

    /* 
        Function to return a double from 'num' array in stack.
        To not read the same number again, we need to increase
        the size of 'num' array.

        PARAMETERS:
            - stack: stack with double array.
        RETURN:
            - num: double number from 'num' array.
    */

    return stack->num[stack->size++];
}

void destroyStack(STACK* stack){

    /*
        Funtion to destroy a stack, free'ing it.

        PARAMETERS:
            - stack: stack to free.
    */

   free(stack);
}