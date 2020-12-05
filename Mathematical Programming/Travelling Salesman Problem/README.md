# Travelling Salesman Problem
This projects uses [OR-Tools]() with [SCIP]() to solve [Waterloo's](http://www.math.uwaterloo.ca/tsp/world/countries.html) city datasets using [MIP solver](https://developers.google.com/optimization/mip/integer_opt) from OR-Tools. It also uses 2-OPT and LKH heuristics for better approachs to the optimal result found by Waterloo.

## Requisites
- [OR-Tools](https://developers.google.com/optimization/install);
- [Numpy](https://numpy.org/doc/stable/user/install.html);
- [SKLearn](https://scikit-learn.org/stable/install.html);
- [Elkai](https://github.com/filipArena/elkai) (for LKH heuristc);
- [Matplotlib](https://matplotlib.org/users/installing.html#installing-an-official-release);

## Instructions
- Clone this repo and open this jupyter notebook;
- You'll need to grant permission to login into your Google Drive account. It only does it to use the .tsp file located at your Google Drive root folder. To change this, change file location (like shown below) and ignore the permission cell;

![](https://i.imgur.com/vJGk3S3.png)

- Run the jupyter.

## Notes
- A huge thanks to **[@filipArena](https://github.com/filipArena)** for sharing Elkai with the community. It helped us a lot;
- The source of **2-OPT** heuristic on this code is [here](https://stackoverflow.com/a/53977320/10304974).

## Credits
- [Bruno dos Santos](https://github.com/brunin-cps);
- Me;
- [Paulo H. da Silva](https://github.com/pau1o-hs);
- [Witor M. A. de Oliveira](https://github.com/witormao);

