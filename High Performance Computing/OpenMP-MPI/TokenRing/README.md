# Token Ring
This program distributes a token by sending and receiving it between available quantity of process in the running machine using Open MPI API.

## Instructions
- Compile by using: `make`
- Run by using: `make run`

## Notes
- If running with `make run`, this program will use all the available process in your machine. In order to set the number of process, use `mpirun -np NUM tokenring` and set NUM to a desired number of process to run;
- Check Open MPI [documentation](https://www.open-mpi.org/doc/current/) for more details.

## Credits
In the source code