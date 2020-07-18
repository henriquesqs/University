# Internet Relay Chat (IRC)

This project was created in order to **simulate an Internet Relay Chat (IRC)** adapting [RFC 1459 specifications](https://tools.ietf.org/html/rfc1459). Currently, this project **supports more than one client connected at the same time** by using multithreads.

## Development

All the project was developed using **C++11 languague** and **g++ compiler** on Fedora 31 workstation. We also tested on Ubuntu 18.04.2.

## Members

This project was made by:

-   Henrique de S. Q. dos Santos, NUSP 10819029 ([henriquesqs](https://github.com/henriquesqs));
-   Witor M. A. de Oliveira, NUSP 10692190 ([witorMao](https://github.com/witormao)).

## How to use

-   Certify that you have **make** installed;
-   Use `make all` to compile the source code;
-   Open two terminals;
-   On first terminal, use `make s` to run server side application. You won't see nothing after running this;
-   On second terminal, use `make c` to run client side application;
-   Wait for the welcome message and follow the instructions provided by the application.
