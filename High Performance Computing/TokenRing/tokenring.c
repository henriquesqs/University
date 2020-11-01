// To compile: mpicc tokenring.c -o tokenring
//
// To run:
// Default: mpirun tokenring (executes this program with available num of cores)
//
// Source code by:
// Gustavo T. Mastrobuono NUSP 10734411,
// Henrique de S. Q. dos Santos NUSP 10819029,
// Jhordan P. V. Pesantes NUSP 11733353,
// Witor M. A. de Oliveira NUSP 10692190,
// Yorvin A. R. Carrion NUSP 11733332

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

  int npes;   // Armazena numero de processos
  int token;  // Token a ser passado entre os processos
  int myrank; // Armazena rank de processos

  MPI_Status status; // Controla o status do ambiente MPI

  // Inicializa o ambiente do MPI
  MPI_Init(&argc, &argv);

  // Armazena o nro total de processos disponiveis em 'npes'
  MPI_Comm_size(MPI_COMM_WORLD, &npes);

  // Armazena o ranking dos processos em 'myrank'
  MPI_Comm_rank(MPI_COMM_WORLD, &myrank);

  // Se rank == 0, estamos no nosso primeiro processo
  if (myrank == 0) {

    token = 0;

    // Enviando um inteiro MPI_INT (token) para o próximo processo
    // (myrank + 1) no grupo associado ao comunicador MPI_COMM_WORLD
    MPI_Send(&token, 1, MPI_INT, (myrank + 1), 0, MPI_COMM_WORLD);

    // Recebe um inteiro do último processo no grupo
    MPI_Recv(&token, 1, MPI_INT, npes - 1, 0,
             MPI_COMM_WORLD, &status);

    printf("Token recebido pelo último processo: %d\n\n", token);
  }

  else {

    // Recebe um inteiro do processo anterior no grupo
    MPI_Recv(&token, 1, MPI_INT, myrank - 1, 0,
             MPI_COMM_WORLD, &status);

    token++;

    // Se estivermos no último processo do grupo, envia
    // o token para o primeiro processo (de rank 0)
    if (myrank == npes - 1) {
      MPI_Send(&token, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    }

    // Se não, envia o token pro próximo processo no grupo
    else {
      MPI_Send(&token, 1, MPI_INT, myrank + 1, 0, MPI_COMM_WORLD);
    }
  }

  // Encerra o ambiente do MPI
  int retorno = MPI_Finalize();
  if (retorno == MPI_SUCCESS)
    printf("MPI_Finalize efetuado com sucesso! Encerrando processo %d.\n",
           myrank);
  else
    printf("Encerrando programa com erro %d do MPI.\n", retorno);

  printf("\n");
  return 0;
}