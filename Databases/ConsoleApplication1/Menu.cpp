#include "SystemInterface.h"

void SystemInterface::Menu::Starter()
{
	std::cout << "-------------------- MENU --------------------" << std::endl;
	std::cout << "Please, select your action:" << std::endl;
	std::cout << "[1] Login" << std::endl;
	std::cout << "[2] Register" << std::endl;
	std::cout << "[3] Search for a component" << std::endl;
	std::cout << "[4] Show components from the best advertisers" << std::endl;
	std::cout << "[0] Exit aplication" << std::endl;
	std::cout << "----------------------------------------------" << std::endl;
}

void SystemInterface::Menu::Advertiser()
{
	std::cout << "----------------- ADVERTISER -----------------" << std::endl;
	std::cout << "Please, select your action:" << std::endl;
	std::cout << "[1] Edit profile" << std::endl;
	std::cout << "[2] Search for a component" << std::endl;
	std::cout << "[3] Announce a component" << std::endl;
	std::cout << "[0] Back" << std::endl;
	std::cout << "----------------------------------------------" << std::endl;
}

void SystemInterface::Menu::Contractor()
{
	std::cout << "----------------- CONTRACTOR -----------------" << std::endl;
	std::cout << "Please, select your action:" << std::endl;
	std::cout << "[1] Edit profile" << std::endl;
	std::cout << "[2] Search for a component" << std::endl;
	std::cout << "[0] Back" << std::endl;
	std::cout << "----------------------------------------------" << std::endl;
}

void SystemInterface::Menu::Profile()
{
	std::cout << "-------------------- INFO --------------------" << std::endl;
	std::cout << "NAME: " << name << std::endl;
	std::cout << "CPF: " << cpf << std::endl;
	std::cout << "E-MAIL: " << email << std::endl;
	std::cout << "PASSWORD: " << password << std::endl;
	std::cout << "------------------- PROFILE ------------------" << std::endl;
	std::cout << "Please, select your action:" << std::endl;
	std::cout << "[1] Name" << std::endl;
	std::cout << "[2] E-mail" << std::endl;
	std::cout << "[3] Password" << std::endl;
	std::cout << "[0] Back" << std::endl;
	std::cout << "----------------------------------------------" << std::endl;
	//std::cout << "Type the information that you want to change: ";
}



