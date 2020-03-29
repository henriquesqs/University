# Video Poker
Video Poker is a card game that simulates the regular poker, but with some changes on its rules. 

### Languagues and Tools
- Java

### Introduction
First of all, you'll need to **download** this folder. 

You can use your favorite IDE that can handle with java's dependencies, build path etc to open and **setup the game**. We recommend [Eclipse](https://www.eclipse.org/downloads/) or [Visual Studio Code](https://code.visualstudio.com/download) to you.

Once you've downloaded this folder and setup your environment, you can play on:

- your **terminal**: simply run `Main.java` file; or
- with a **GUI (Graphical user interface)** window: execute `VideoPokerGUI.java` file.

On this tutorial, we'll show you how the application works with the GUI.

### The game
The objective of this game is to win as much credits as you can, but that depends on your luck.  You'll only be able to bet if you have at least 1 credit. The game won't allow you to bet more money than you have.

After starting the game, you'll receive **5 cards and 200 credits**. To win the round, *i.e*, to don't lose your credits, you'll need to get one of the combinations of cards below:

![combinations of cards](https://i.imgur.com/pgdI49o.png)

> **Image by [casinoreports](https://www.casinoreports.ca/video-poker/rules/).**

Each combination has its own prize. **From top to bottom**, the prizes are:

 - 200 times your bet;
- 100 times your bet;
- 50 times your bet;
- 20 times your bet;
- 10 times your bet;
- 5 times your bet;
- 2 times your bet;
- your bet (you don't lose credits, neither win credits).

### Starting the game
After executing `VideoPokerGUI.java` file, you'll see this window:

![first window of the app](https://i.imgur.com/0ElV0lS.png)

By clicking on ***Instrucoes*** (instructions) the application will show you the rules and instructions of the game. By clicking on ***sair*** (exit), it closes the window and stops the application. Finally, by clicking on ***Iniciar***  (start) it will start the application and you'll se this message :

![start message](https://i.imgur.com/tfomLcV.png)

This message asks if you want to change one of the cards. **At each round, you can change one to five of your cards three times**. Clicking on "ok" button will allow you to change your cards, place your bet or exit the game. 

Suppose that we want to change card one and three. So, you must check the box below each card like the image below and click on "***trocar***" (change) button:

![the main game window before change](https://i.imgur.com/xQfyxhx.png)

The game will provide you new cards for the selected ones. Suppose we'll place a bet of 100 credits. So, we need to enter 100 on the field aside the text ***sua aposta*** (your bet) and click on the green button ***apostar*** (bet):

![the main game window during the bet and afther the cards change](https://i.imgur.com/3kKJeT1.png)

As you can see, on this example we have two of a kind. **The application will automatically see if have some of the combinations listed above and will provide you your current credits balance after the bet**. On this case, we receive our bet as a prize:

![the main game window after the bet](https://i.imgur.com/FDNEUhu.png)

The game shows a prompt saying that you've had the combination two of a kind and tells your prize. By clicking on ok, you'll be able to repeat the process or exit the game.

Hope you'll enjoy it! :)

### Credits
Our development group is:
 - Henrique de S. Q. dos Santos (me);
- Leonardo R. Luiz.

**The images on this project are on google**.
