#include "SystemInterface.h"

void SystemInterface::ProfileEditor::UpdateName()
{
	std::cout << "------------------- UPDATE -------------------" << std::endl;
	std::cout << "Type the new Name: ";
	std::getline(std::cin, name);

	// UPDATE
	st.Execute("update " + userType[type] + " set NOME ='" + name + "' where CPF='" + cpf + "'");
	con.Commit();
}

void SystemInterface::ProfileEditor::UpdateEmail()
{
	std::cout << "------------------- UPDATE -------------------" << std::endl;
	std::string tmp;

	std::cout << "Type the new E-mail: ";
	std::cin >> tmp;

	// Checar se o email ja existe
	ocilib::Resultset rs = QueryBuilder("select Email from " + userType[type] + " where Email='" + tmp + "'");

	// USER FOUND
	if (rs.GetCount() != 0 || !is_email_valid(tmp))
	{
		std::cout << "Register Failed" << std::endl;
		std::cout << "This E-mail is already registered or incorrect. Please check your informations." << std::endl << std::endl;
		return;
	}

	// UPDATE
	email = tmp;

	st.Execute("update " + userType[type] + " set EMAIL = '" + email + "' where CPF='" + cpf + "'");
	con.Commit();
}

void SystemInterface::ProfileEditor::UpdatePassword()
{
	std::cout << "------------------- UPDATE -------------------" << std::endl;
	std::cout << "Type the new Password: ";
	std::cin >> password;

	// UPDATE
	st.Execute("update " + userType[type] + " set SENHA = '" + password + "' where CPF='" + cpf + "'");
	con.Commit();
}