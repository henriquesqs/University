#ifndef TAD_H
#define TAD_H
#define ITEM char
#define TAM 1000

#include "tadBT.h"

// Function to create, allocate and return a pointer to NODE
NODE* nodeCreate(ITEM item);

// Function to verify if the expression has an error. If not, it converts it to reverse-polish notation
char shuntingYard(char c, STACK* stack, STACK* operators, char vet[]);

// Function to verify if an operation involving operators is valid
int validOperator(STACK* stack, char c, char* vet);

// Function to verify if a given c is a binnary operator
int isBinaryOperator(ITEM item);

// Function to verify if a given c is an unnary operator
int isUnnaryOperator(ITEM c);

#endif