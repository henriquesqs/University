#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <ctype.h>

#include "tad.h"

#define ERRO -404

struct node{
    ITEM content;
    NODE* left;
    NODE* right;

};

NODE* nodeCreate(ITEM item){

    /*
        Function to create a pointer to NODE*.
        
        RETURN:
            - node: allocated and initialized node.
    */

    NODE* node = (NODE*)malloc(sizeof(NODE));

    node->left = NULL;
    node->right = NULL;
    node->content = item;
    return node;
}

NODE* buildTree(NODE* root, STACK* stack, ITEM item){

    /*
        Function to create a binary tree from a stack.
        
        PARAMETERS:
            - root: root to a binary tree;
            - stack: stack will an expression inside.
        RETURN:
            - root: updated Root.
    */

    root = nodeCreate(item);

    if (stackEmpty(stack)) return root;
    
    if(isBinaryOperator(item)){
        item = pop(stack);
        root->left = buildTree(root->left, stack, item);
        
        item = pop(stack);
        root->right = buildTree(root->right, stack, item);
    }

    else if(isUnnaryOperator(item)){
        item = pop(stack);
        root->left = buildTree(root->left, stack, item);
    }

    return root;
}

void destroyTree(NODE* root){

    /*
        Function to destroy a tree from its root.

        PARAMETERS:
            - root: root of the tree.
    */

    if(root == NULL) return;
    destroyTree(root->left);
    destroyTree(root->right);
    free(root);
}

void printTree(NODE *root){

    /*
        Function to print the infix expression tree

        PARAMETERS:
            - root: root to a tree
    */
    
    if(root == NULL) return;
    printTree(root->left);
    printf("%c ", root->content);
    printTree(root->right);
}

double solveTree(NODE* root, STACK* stack){

    /*
        This function receives a node of the expression tree 
        and recursively evaluates it.

        PARAMETERS:
            - root: root to the expression tree;
            - stack: stack with double values.
        RETURN:
            evaluated value of the tree
    */

    // empty tree 
    if (root == NULL) return 0;
  
    // leaf node (a double)
    if (root->left == NULL && root->right == NULL)
        return toDouble(stack);
    
    // Solving left subtree 
    double left_value = solveTree(root->right, stack); 

    // Solving right subtree 
    double right_value = solveTree(root->left, stack); 

    // Checking if it's a binary operator
    if (root->content == '+') // sum op
        return left_value+right_value; 
  
    if (root->content == '-') // sub op
        return left_value-right_value; 
  
    if (root->content == '*') // multip op
        return left_value*right_value; 

    if (root->content == '^') // power op
        return pow(left_value,right_value); 

    if (root->content == '/'){ // div op
        if(right_value != 0) 
            return left_value/right_value; 
        else
            return ERRO;
    }
    
    // Checking if it's a unnary operator
    if(root->content == 'l') // log op
        return log2(right_value);

    if(root->content == 's') // sqrt op
        return sqrt(right_value);

    if(root->content == 'e') // exp op
        return exp(right_value);
}