#ifndef TADBT_H
#define TADBT_H

#include "tadPilha.h"

typedef struct node NODE;

// Function to create a tree from a given pointer to STACK
NODE* buildTree(NODE* root, STACK* stack, ITEM item);

// Function to print the infix expression tree 
void printTree(NODE* root);

// Function to destroy a tree from its root
void destroyTree(NODE* root);

// Function to evaluate an expression tree
double solveTree(NODE* root, STACK* stack);

#endif