#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define MAXBYTES 600000

int size = 0;

char *strlower(char *str){

    /*
        Function to convert uppercase letters to lowercase.

        PARAMETERS:
            - str: string that we want to convert to lowercase.

        RETURN:
            - str: converted string.
    */

    char *p = (char *)str;

    while (*p) {
        *p = tolower((char)*p);
        p++;
    }
    return str;
}

void freeing(char** array, int MAX){

    /*
        Function to free an allocated bidimensional array of char.

        PARAMETERS:
            - array: bidimensional array to free;
            - MAX: quantity of bytes to free.
        
    */

    for(int i = 0; i < MAX; i++){
        free(array[i]);
    }
    
    free(array);
}

char** allocating(int bytes){

    /*
        Function to allocate a bidimensional array of char.

        PARAMETERS:
            - bytes: quantity of bytes to allocate.
        
        RETURN:
            - array: allocated array.
    */

    char** array;
    array = (char**) malloc(bytes * sizeof(char*));
    
    for(int i = 0; i < bytes; i++){
        array[i] = (char*) malloc(50 * sizeof(char));
    }
    
    if(array == NULL) printf("error in function 'allocating'");
    return array;
}

void printArray(char** array, int size){ 
    
    /*
        Function to print a bidimensional array of char. 

        PARAMETERS:
            - array: array to print;
            - size: array's size.
    */

    FILE* output;

    output = fopen("output.txt", "w+");
	
    for (int k = 0; k < size; k++){
        fprintf(output, "%s\n", array[k]);
	}

    fclose(output);
} 

int binarySearch(char** array, char* key, int max, int min){
    
    /*
        Function to search for a key in a bidimensional array of chars.

        PARAMETERS:
            - array: array that we want to search in for the key;
            - key: the element that we will search for;
            - max: maximum value of array's index;
            - min: minimum value of array's index.

        RETURN:
            - success: indicates if we successfully found the key or not.

    */

    if(min > max) return 0;

    int index = (int)((min+max)/2.0);

    if (strcmp(key, array[index]) == 0) return 1;
    else if (strcmp(key, array[index]) < 0) return binarySearch(array, key, index - 1, min);
    else return binarySearch(array, key, max, index + 1);

    return -404;
}

void merge(char** array, int start, int end, char** temp, int middle){ 

    /*
        Funcion two merge two parts of an array.

        PARAMETERS:
            - array: array which we want to divide;
            - start: minium array's index;
            - end: maximum array's index;
            - temp: temporally array to auxiliate;
            - middle: middle array's index.
    */
    
    int i = start;      // index of the 1st part
    int j = middle+1;   // index of the 2nd part
    int k = 0;          // index of the auxiliar array

    while (i <= middle && j <= end) {
        if (strcmp(array[i], array[j]) <= 0) {
            strcpy(temp[k], array[i]); 
            i++;
        } 
        else {
            strcpy(temp[k], array[j]);
            j++;
        }
        k++;
    }

    while (i <= middle) {
        strcpy(temp[k], array[i]);
        i++; k++;
    }   

    while (j <= end) {
        strcpy(temp[k], array[j]);
        j++; k++;
    }   

    for (i = start, k = 0; i <= end; i++, k++) {
        strcpy(array[i], temp[k]);
    }
}

void mergeSort(char** array, int start, int end, char** temp){

    /*
        Merge Sort algorithm to sort a bidimensional array of chars.

        PARAMETERS:
            - array: bidimensional array to sort;
            - start: minimum array's index;
            - end: maximum array's index;
            - temp: temporally array to auxiliate.

    */
    
    if (end <= start) return; // base case

    int middle = (int) ((end+start)/2.0);

    mergeSort(array, start, middle, temp);   
    mergeSort(array, middle+1, end, temp);
    merge(array, start, end, temp, middle);
}

int repeatedWords(char** destiny, char** array, int value){

    /*
        Function to transfer elements from a bidimensional array to another
        without transfering the repeated ones.

        PARAMETERS:
            - destine: array that we will transfer the elements for;
            - array: array with the elements (including the repeated ones);
            - size: size of the 'array'.
        
        RETURN:
            - transferedItems: quantity of elements that we sucessfully transfered.

    */

    int transferedItems = 0;
    int j = 0;

    for(j = 1; j < value; j++){
        
        if(array[j+1] == NULL) break;

        while( (strcmp(array[j-1], array[j])) == 0) j++;

        strcpy(destiny[transferedItems], array[j-1]);
        transferedItems++;
    }
    
    return transferedItems;
}

void spellChecker(char** dictionary, FILE* tweetArchive, int size){

    /*  
        Function that opens a tweet file and search for incorrect words (not found in 
        the dictionary) in this tweet.

        PARAMETERS:
            - dictionary: dictionary that we use to check if some word is correct or not;
            - tweetArchive: tweet that we will check the text;
            - size: size of the dictionary (we will use this in Binary Search).
    */

    char **temp = NULL, *key = NULL, aux[1000];
    int k = 0, found = 0;

    temp = allocating(280);
    key = malloc(45 * sizeof(char));

    while(fscanf(tweetArchive, "%s", aux) != EOF){ // reading the tweet until the EOF
        
        if(strcmp(aux, "\"text\":") == 0){ // if we find something like "text":

            fscanf(tweetArchive, "%*[^\"]%*[\"]"); // we need to drop off what we don't need
            while( fscanf(tweetArchive, "%[a-zA-Z]%*[^a-zA-Z\"]", temp[k]) ){ // and then we need to read the line until we found a ""
            
                strcpy(key, temp[k]); // copying the read word to an auxiliar because we need the original word even if it's in upper case
                temp[k] = strlower(temp[k]); // converting the read word to lower case
                if(!binarySearch(dictionary, temp[k], size, 0)){ // if binary search returns something different from -404
                    found = printf("%s ", key); // it means that we found a word that isnt in the dictionary. So we need to print it!
                }
                k++; 
            }
            printf("\n");
        }
    }

    if (found == 0) printf("No tweets to check"); // in case that we didnt found any tweet to check, the function printf will never return something different from 0

    free(key);
    freeing(temp, 280);
}

char** creatingDictionary(FILE* bookArchive){

    /*
        Function to create a sorted dictionary (bidimensional array of char) that will storage
        all the words (strings) found in a book archive.

        PARAMETERS:
            - bookArchive: file of the book that the function will check for the words;
    */

    char **aux = NULL, **temp = NULL;;

    aux = allocating(MAXBYTES);
    temp = allocating(MAXBYTES);
    
    while(fscanf(bookArchive, "%[a-zA-Z]%*[^a-zA-Z][^\n]", aux[size]) != EOF){
        aux[size] = strlower(aux[size]);
        size++;
    }
    
    mergeSort(aux, 0, size-1, temp);
    //printArray(dictionary, i);
    
    freeing(temp, MAXBYTES);

    return aux;

}

int main(int argc, char const *argarray[]){

    FILE *bookArchive, *tweetArchive;
    char **dictionary = NULL, **aux = NULL;
    char archiveName[20], tweet[20];
    
    dictionary = allocating(MAXBYTES);

    scanf("%s %s", archiveName, tweet);

    bookArchive = fopen(archiveName, "r");
    tweetArchive = fopen(tweet, "r");
    aux = creatingDictionary(bookArchive); // getting book data to use as the new 'world dictionary' :P
    size = repeatedWords(dictionary, aux, size);
    spellChecker(dictionary, tweetArchive, size-1);

    fclose(tweetArchive);
    fclose(bookArchive);

    freeing(aux, MAXBYTES);
    freeing(dictionary, MAXBYTES);
    
    return 0;
}
