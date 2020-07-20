#include "SystemInterface.h"

// DEFINING STATIC METHODS
ocilib::Statement SystemInterface::st;
ocilib::Connection SystemInterface::con;

std::string SystemInterface::name;
std::string SystemInterface::cpf;
std::string SystemInterface::email;
std::string SystemInterface::password;
std::string SystemInterface::userType[2] = { "Anunciante", "Contratante" };
int SystemInterface::type;

class SystemInterface::Menu SystemInterface::Menu;
class SystemInterface::Loop SystemInterface::Loop;
class SystemInterface::User SystemInterface::User;
class SystemInterface::ProfileEditor SystemInterface::ProfileEditor;
class SystemInterface::Component SystemInterface::Component;

void SystemInterface::SetUserInfo(ocilib::Resultset& rs)
{
	name = rs.Get<ocilib::ostring>(1);
	cpf = rs.Get<ocilib::ostring>(2);
	email = rs.Get<ocilib::ostring>(3);
	password = rs.Get<ocilib::ostring>(4);
}

bool SystemInterface::CheckCommand(int& command, int min, int max)
{
	// Comandos variam seu range dependendo do tipo de usuario
	if (command >= min && command <= max) return true;

	std::cout << "Wrong input" << std::endl << std::endl;
	return false;
}

bool SystemInterface::is_email_valid(std::string& email)
{
	// define a regular expression
	const std::regex pattern
	("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+");

	// try to match the string with the regular expression
	return std::regex_match(email, pattern);
}

ocilib::Resultset SystemInterface::QueryBuilder(std::string str)
{
	// EXECUTE QUERY COMMAND
	st.Execute(str);

	// GET RESULT SET
	ocilib::Resultset rs = st.GetResultset();
	rs.Next();

	return rs;
}