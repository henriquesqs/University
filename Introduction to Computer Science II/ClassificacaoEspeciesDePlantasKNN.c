/*
 KNN-based program to classify a specie of plant using Euclidean Distance algorithm.
 Made by:	
  _                     _                                 
 | |__   ___ _ __  _ __(_) __ _ _   _  ___  ___  __ _ ___ 
 | '_ \ / _ \ '_ \| '__| |/ _` | | | |/ _ \/ __|/ _` / __|
 | | | |  __/ | | | |  | | (_| | |_| |  __/\__ \ (_| \__ \
 |_| |_|\___|_| |_|_|  |_|\__, |\__,_|\___||___/\__, |___/
                             |_|                   |_|    
	Aluno de Bacharelado em Ciências de Computação 
		   Universidade de São Paulo (USP) - São Carlos/SP
*/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

#define MAX 150

typedef struct{

	char class[11];
	float sepalWidth;
	float petalWidth;
	float sepalLenght;
	float petalLenght;

} CHART;

typedef struct{

	float *dist;
	char **specie;
	int trainNum[1000];

} RESULT;


void analyzingData(int testLines, int trainingLines, RESULT* example, int neighbors, CHART* train, CHART* test){

	/*
		Function to analyse the frequency of a specie to determine which class the flower is.

		PARAMETERS:
		trainingLines: number of lines in training file;
		testLines: number of lines in test file;
		neighbors: number "k" of neighbors that we'll need to calculate to determine which class the flower is.
	*/

	float hits = 0;
	int setosa = 0, versicolor = 0, virginica = 0; // function will use this integers as counters
	char** class = NULL; // "class" will store which specie the flower probably is

	class = (char**) malloc(MAX * sizeof(char*));

	for(int i = 0; i < testLines; i++){
		class[i] = (char*) malloc(MAX * sizeof(char));
	}

	for(int i = 0; i < testLines; i++){

		for(int k = 0; k < neighbors; k++){
			
			// Verifying frequency
			if( strcmp(example[i].specie[k], "setosa") == 0) setosa++;
			else if( strcmp(example[i].specie[k], "versicolor") == 0) versicolor++;
			else if( strcmp(example[i].specie[k], "virginica") == 0) virginica++;
			
			// Checking which class the flower is
			if(setosa > versicolor && setosa > virginica) strcpy(class[i], "setosa");
			else if(versicolor > setosa && versicolor > virginica) strcpy(class[i], "versicolor");
			else if(virginica > versicolor && virginica > setosa) strcpy(class[i], "virginica");

			// Preventing a draw case. If true, the nearest neighbor will determine the class of the flower
			if(setosa == versicolor) strcpy(class[i], example[i].specie[0]);
			if(setosa == virginica) strcpy(class[i], example[i].specie[0]);
			if(virginica == versicolor) strcpy(class[i], example[i].specie[0]);
		}
					
		setosa = 0, versicolor = 0, virginica = 0;
	}

	// At this point, we already know which class the example is. So, we just need to calculate the hit rate.
	for(int i = 0; i < testLines; i++){
		if( strcmp(class[i], test[i].class) == 0){
			hits++;
		}
	}

	// Finishing, we need to print side by side the class found by knn algorithm and the real class (classified by an specialist).
	for(int i = 0; i < testLines; i++){
	 	printf("%s %s\n", class[i], test[i].class);
	}

	// Printing the hit rate
	printf("%.4f\n", hits/(testLines));

	free(class);
}

void insertionSort(int testLines, int trainingLines, RESULT* example){

	/*
		Using Insertion Sort algorithm, this function will sort the distances calculated with
		Euclidean Distance algorithm but we can't lose the training number of the result. So, this
		function will also store the position of the distance to change when sort it.

		PARAMETERS:
		trainingLines: number of lines in training file;
		testLines: number of lines in test file;
		example: struct containing all data that we'll sort
	*/

   	float auxDist;
   	int auxIndex;
   	char *auxClass;

   	auxClass = (char*) malloc(MAX * sizeof(char));

    for(int i = 0; i < testLines; i++){

		for(int j = 0; j < trainingLines; j++){

			for(int g = 0; g < trainingLines; g++){

				if(example[i].dist[g] > example[i].dist[j]){

					// aux variables receives some data to save before changing them
					auxDist = example[i].dist[j];
					auxIndex = example[i].trainNum[j];
					auxClass = example[i].specie[j];

					// changing positions
					example[i].dist[j] = example[i].dist[g];
					example[i].specie[j] = example[i].specie[g];
					example[i].trainNum[j] = example[i].trainNum[g];

					example[i].specie[g] = auxClass;
					example[i].dist[g] = auxDist;
					example[i].trainNum[g] = auxIndex;
				}
			}
		}
	}

	free(auxClass);
}

void euclidianDistance(CHART* train, CHART* test, int trainingLines, int testLines, int neighbors){

	/*
		This function will calculate the distance between two points using Euclidian Distance.
		Then, the program will be able to determine from which class a flower is.

		PARAMETERS:
		train: struct created for storing the data from training file;
		test: struct created for storing the data from the file we need to find the class (test file);
		trainingLines: number of lines in training file;
		testLines: number of lines in test file.
	*/

	RESULT* example;

	example = (RESULT*) malloc(MAX * sizeof(RESULT));

	for(int i = 0; i < testLines; i++){
		example[i].dist = malloc(MAX * sizeof(float));
		example[i].specie = malloc(MAX * sizeof(char*));

		for(int j = 0; j < trainingLines; j++){
			example[i].specie[j] = malloc(MAX * sizeof(char));
		}
	}

	for(int i = 0; i < testLines; i++){
		for(int j = 0; j < trainingLines; j++){

			example[i].dist[j] = sqrt( pow(train[j].sepalLenght - test[i].sepalLenght, 2) + pow(train[j].sepalWidth - test[i].sepalWidth, 2)
								+ pow(train[j].petalLenght - test[i].petalLenght, 2) + pow(train[j].petalWidth - test[i].petalWidth, 2));

			strcpy(example[i].specie[j], train[j].class);

			example[i].trainNum[j] = j;
		}
	}

	insertionSort(testLines, trainingLines, example);
	analyzingData(testLines, trainingLines, example, neighbors, train, test);

	for(int i = 0; i < testLines; i++){
		free(example[i].dist);
		free(example[i].specie);

		for(int j = 0; j < trainingLines; j++){
			free(example[i].specie[j]);
		}
	}

	free(example);
}

CHART* gettingData(FILE *archive, int lines){

	/*
		First of all, I need to get the data from training and test files. This function will get every element in the files
		and store them in an struct. Finishing it, the function will return the struct with all data stored.

		PARAMETERS:
		sheet: struct that the function will store the data and return to main;
		archive: this function will get the data from both test and training archives. So it needs to know from which archive we're getting data off;
		lines: for the same reason mentioned above, we need to know how many lines we are dealing.
	*/

	CHART *sheet;
	sheet = malloc(MAX * sizeof(CHART));

	fscanf(archive, "%*[^\n]"); // I'm taking off the first line in archive because I don't need it

	for(int i = 0 ; i < lines; i++){
		fscanf(archive, "%f, %f, %f, %f, \"%[^\"]\"", &sheet[i].sepalLenght, &sheet[i].sepalWidth, &sheet[i].petalLenght, &sheet[i].petalWidth, sheet[i].class);
	}

	return sheet;
}

int main(int argc, char const *argv[]){

	CHART *trainingChart, *testChart;
	FILE *training, *test;
	int neighbors = 0, testLines = -1, trainingLines = -1;
	char trainingArchive[10], testArchive[10], storage[MAX];

	scanf("%s %s %d", trainingArchive, testArchive, &neighbors);

	training = fopen(trainingArchive, "r");
	test = fopen(testArchive, "r");

	while( (fscanf(training, "%s", storage)) != EOF) trainingLines++; // getting the number of lines in training file
	while( (fscanf(test, "%s", storage)) != EOF) testLines++; // getting the number of lines in test file

	if(neighbors < 1 || neighbors > trainingLines){
		printf("k is invalid\n");
		return 0;
	}

	rewind(training);
	rewind(test);

	trainingChart = gettingData(training, trainingLines); // getting data of training file
	fclose(training);

	testChart = gettingData(test, testLines); // getting data of test file
	fclose(test);

	euclidianDistance(trainingChart, testChart, trainingLines, testLines, neighbors);

	return 0;
}