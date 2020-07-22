#include "SystemInterface.h"

// INTERFACE VARIABLES
int command;

void SystemInterface::Loop::Starter()
{
	// RUNNING INTERFACE
	do {
		Menu.Starter();

		std::cin >> command;
		system("CLS");

		if (CheckCommand(command, 0, 4) == false) continue;

		// MENU OPERATIONS
		if (command == 1) User.Login();
		else if (command == 2) User.Register();
		else if (command == 3) Component.Search();
		else if (command == 4) Component.bestSearch();

	} while (command != 0);

	command = -1;
}

void SystemInterface::Loop::Advertiser()
{	
	// RUNNING INTERFACE
	do {
		Menu.Advertiser();

		std::cin >> command;
		system("CLS");

		if (CheckCommand(command, 0, 3) == false) continue;

		// MENU OPERATIONS
		if (command == 1) Profile();
		else if (command == 2) Component.Search();
		else if (command == 3) Component.Announce();

	} while (command != 0);

	command = -1;
}

void SystemInterface::Loop::Contractor()
{
	// RUNNING INTERFACE
	do {
		Menu.Contractor();

		std::cin >> command;
		system("CLS");

		if (CheckCommand(command, 0, 2) == false) continue;

		// MENU OPERATIONS
		if (command == 1) Profile();
		else if (command == 2) Component.Search();

	} while (command != 0);

	command = -1;
}

void SystemInterface::Loop::Profile()
{
	// RUNNING INTERFACE
	do {
		Menu.Profile();

		std::cin >> command;
		std::getchar();

		system("CLS");

		if (CheckCommand(command, 0, 3) == false) continue;

		// MENU OPERATIONS
		if (command == 1) ProfileEditor.UpdateName();
		else if (command == 2) ProfileEditor.UpdateEmail();
		else if (command == 3) ProfileEditor.UpdatePassword();

	} while (command != 0);

	command = -1;
}