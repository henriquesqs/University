/*
 Programa de recuperação de imagens a partir de um SD card.
 Feito por:	
  _                     _                                 
 | |__   ___ _ __  _ __(_) __ _ _   _  ___  ___  __ _ ___ 
 | '_ \ / _ \ '_ \| '__| |/ _` | | | |/ _ \/ __|/ _` / __|
 | | | |  __/ | | | |  | | (_| | |_| |  __/\__ \ (_| \__ \
 |_| |_|\___|_| |_|_|  |_|\__, |\__,_|\___||___/\__, |___/
                             |_|                   |_|    
	Aluno de Bacharelado em Ciências de Computação 
		   Universidade de São Paulo (USP) - São Carlos/SP
*/

#include <stdio.h>
#include <stdbool.h>

bool image = false;

bool recovering(unsigned char block[512], int currentArchive){

    /*
        All the recovering process are in this function. First of all we need to open an archive to
        allocate the bytes of an image in it. After this we need to do a search in all of the example.img file
        trying to find an other image header because it was said that an image ends in the beggining of an other, i.e.,
        when we discover other header, that's the end of the last image and the beggining of a new one.
    */

    FILE *newArchive;
    char newArchiveName[8];

    sprintf(newArchiveName, "%03d.jpg", currentArchive);

    newArchive = fopen(newArchiveName, "w");
    
    fwrite(block, 512, 1, newArchive); // allocating the bytes of the image header

    while (fread(block, 512, 1, stdin) && !(block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && block[3] == 0xe0)){
        fwrite(block, 512, 1, newArchive); // allocates the bytes in the same file until it find an other image header
    }

    /*
        If this "while" above is broken it means that we read a new image header and now we know that there starts a new image. So, we need to
        reposition the cursor to the beggining of the image header so that we can read it and allocates its bytes in the new image file.
        We're going to reposition the cursor using the fseek function below.
    */

    fseek(stdin, -512, SEEK_CUR); 
    
    fclose(newArchive);

    return true;
}

int main(int argc, char const *argv[]){

    FILE *newArchive;
    int currentArchive = 0;

    unsigned char block[512];

    while (fread(block, 512, 1, stdin)){
        
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && block[3] == 0xe0){ // we found an image header!
            image = recovering(block, currentArchive);
            currentArchive++;
        }
    }

    if (image == false){ // probably there is no images in the file gave to us :(
        printf("Could not find pictures\n");
    }

    return 0;
}

