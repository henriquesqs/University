#ifndef TADPILHA_H
#define TADPILHA_H

#define ITEM char
#define TAM 1000

typedef struct stack STACK;

// Function to create, allocate and return a pointer to STACK
STACK* stackCreate();

// Function to invert a given pointer to STACK
STACK* stackInvert(STACK* stack);

// Function to erase all the content in a 'stack'
void stackErase(STACK* stack);

// Function to print the content in a 'stack'
void stackPrint(STACK* stack);

// Function to pop the top item from a 'stack'
char pop(STACK* stack);

// Function to return the top item from a 'stack'
char stackTop(STACK* stack);

// Function to verify if the 'stack' is full
int stackFull(STACK* stack);

// Function to verify if the 'stack' is empty
int stackEmpty(STACK* stack);

// Function to push an 'item' into the 'stack' top
int push(STACK* stack, ITEM item);

// Function to print an error message and erase the content of 'stack'
void error(STACK* stack);

// Function to add a num to 'stack'
void stackAddNum(STACK* stack, double num);

// Function to convert a given char to double
double toDouble(STACK* stack);

// Function to destroy a 'stack'
void destroyStack(STACK* stack);

#endif