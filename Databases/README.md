# Party organization helper service

Project made as requirement to Databases classes. We've created a service to help advertisers to offer products, services and some spots to contractors who want to throw a party or something else.

## Members

-   Henrique de S. Q. dos Santos ([@henriquesqs](http://github.com/henriquesqs))
-   Leonardo R. Luiz
-   Paulo H. da Silva ([@pau1o-hs](http://github.com/pau1o-hs))
-   Witor M. A. de Oliveira ([@witormao](http://github.com/witormao))

## Development

We've created this application using **Visual Studio 19 in x64** with the help of **Ocilib**, a library which helps to connect a C++ application to **Oracle databases**. We've connected to Oracle db through **sqldeveloper v19.4.0**, also from Oracle.

## Creating the database

We've done this project using **sqldeveloper** so this tutorial will assume you're using it.

-   To create the db, import **Oracle.sql** to sqldeveloper and run the queries;
-   To populate the db, import **Inserts.sql** to sqldeveloper and run;

## How to run the application

-   **Download and install Ocilib** via its official repo clicking [here](https://vrogier.github.io/ocilib/) **or** use [Microsoft's VCPKG](https://github.com/microsoft/vcpkg) to download and install Ocilib. VCPKG also automatically integrates Ocilib to Visual Studio (see their [documentation](https://github.com/microsoft/vcpkg#quick-start-windows) to get help);
-   After installing Ocilib, **create a project on Visual Studio and import ConsoleApplication1 to this new project**;
-   **Compile** and **run** the source code with **x64 option**.

Now you should see a prompt screen with a menu helping you through our application. 

![Application preview](https://github.com/henriquesqs/University/blob/main/Databases/preview.png?raw=true)

Have fun! :)
