#include "SystemInterface.h"

void SystemInterface::User::Login()
{
	// LOGIN INTERACTION
	std::cout << "-------------------- LOGIN -------------------" << std::endl;

	std::cout << "User type (0 - Advertiser and 1 - Contractor): ";
	std::cin >> type;

	if (CheckCommand(type, 0, 1) == false) return;

	std::cout << "Email: ";
	std::cin >> email;

	std::cout << "Password: ";
	std::cin >> password;

	// QUERY BUILDER
	ocilib::Resultset rs = QueryBuilder("select Nome, CPF, Email, Senha from " + userType[type] + " where upper(Email)=upper('" + email + "') and Senha='" + password + "'");

	// USER FOUND
	if (rs.GetCount() != 0)
	{
		std::cout << std::endl << "Logged Successfully" << std::endl;
		std::cout << "Hello, " << rs.Get<ocilib::ostring>(1) << std::endl;

		// SET USERINFO
		SetUserInfo(rs);

		// GOTO USERTYPE LOOP
		if (type == 0) Loop.Advertiser();
		else if (type == 1) Loop.Contractor();
	}
	else std::cout << "Login Failed" << std::endl << std::endl;
}

void SystemInterface::User::Register()
{
	// REGISTER INTERACTION
	std::cout << "------------------ REGISTER ------------------" << std::endl;
	std::cout << "Type the informations bellow:" << std::endl;

	std::cout << "User type (0 - advertiser and 1 - contractor): ";
	std::cin >> type;

	if (CheckCommand(type, 0, 1) == false) return;

	std::cout << "Name: ";
	std::getchar();
	std::getline(std::cin, name);

	std::cout << "CPF: ";
	std::cin >> cpf;

	std::cout << "E-mail: ";
	std::cin >> email;

	std::cout << "Password: ";
	std::cin >> password;

	// Checando validade semantica do CPF
	if ((int) cpf.size() != 11)
	{
		std::cout << "CPFs contem 11 digitos!" << std::endl << std::endl;
		return;
	}

	// Check informations
	// Verificando se o CPF ja esta em uso
	ocilib::Resultset rs = QueryBuilder("select Email, CPF from " + userType[type] + " where CPF='" + cpf + "'");

	// USER FOUND
	if (rs.GetCount() != 0)
	{
		std::cout << "Register Failed" << std::endl;
		std::cout << "This CPF is already registered. Please check your informations." << std::endl << std::endl;
		return;
	}

	// Verificando se o E-mail ja esta em uso
	rs = QueryBuilder("select Email, CPF from " + userType[type] + " where CPF='" + cpf + "'");

	// Outro problema com o Email seria um erro de sintaxe
	if (rs.GetCount() != 0 || !is_email_valid(email))
	{
		std::cout << "Register Failed" << std::endl;
		std::cout << "This E-mail is already registered or incorrect. Please check your informations." << std::endl << std::endl;
		return;
	}
	else
	{
		// INSERT DATA INTO DATABASE AND COMMIT
		st.Execute("insert into " + userType[type] + " values ('" + cpf + "', 0, '" + name + "', '" + email + "', '" + password + "')");
		con.Commit();

		// RECOVER INSERTED DATA
		rs = QueryBuilder("select Nome, CPF, Email, Senha from " + userType[type] + " where Email='" + email + "' and Senha='" + password + "'");

		// SET USERINFO
		SetUserInfo(rs);

		std::cout << std::endl << "Registered Successfully" << std::endl;
		std::cout << "Hello, " << name << std::endl;

		// GOTO USERTYPE LOOP
		if (type == 0) Loop.Advertiser();
		else if (type == 1) Loop.Contractor();
	}
}