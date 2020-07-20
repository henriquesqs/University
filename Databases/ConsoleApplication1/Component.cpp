#include "SystemInterface.h"

void SystemInterface::Component::Search()
{
	std::string component;

	std::cout << "------------------- SEARCH -------------------" << std::endl;
	std::cout << "Please, enter the name of the component you want to search for:" << std::endl;
	std::cout << ">> ";
	std::cin >> component;

	// Buscar pelos componentes com esse nome na tabela
	ocilib::Resultset rs = QueryBuilder("select ID, ANUNCIANTE, PRECO, NOME from COMPONENTE where UPPER(NOME)=UPPER('" + component + "')");

	if (rs.GetCount() == 0)
	{
		std::cout << "Component not found." << std::endl;
	}
	else {
		// Exibir lista de componentes com aquele nome, bem como o nome dos anunciantes e o preco
		std::cout << "----------------------------------------" << std::endl;
		std::cout << "|   ID   |    Anunciante   |   Preco   |" << std::endl;
		std::cout << "----------------------------------------" << std::endl;

		// Exibindo na tela todos os componentes existentes no banco
		do {
			std::cout << "|   " << std::setfill('0') << std::setw(3) << rs.Get<int>(1) << "  |   " << rs.Get<ocilib::ostring>(2) << "   |   " << std::setfill('0') << std::setw(5) << rs.Get<float>(3) << "   |" << std::endl;
		} while (rs.Next());

		std::cout << "------------------------------------------------" << std::endl << std::endl;
	}
}

void SystemInterface::Component::Announce()
{
	std::string componentName;
	std::string price;

	std::cout << "------------------ ANNOUNCE ------------------" << std::endl;
	std::cout << "Type the characteristics of the components referring below:" << std::endl;

	std::cout << "Component name(Servicos, Local or Produto): ";
	std::getchar();
	std::getline(std::cin, componentName);

	for (int i = 0; componentName[i]; i++) componentName[i] = tolower(componentName[i]);

	if (componentName != "servicos" && componentName != "local" && componentName != "produto")
	{
		std::cout << "The Component name needs to be 'Servicos', 'Local' or 'Produto'"<< std::endl;
		return;
	}

	std::cout << "Component price (two decimal places): ";
	std::cin >> price;

	// Checando ultimo id
	ocilib::Resultset rs = QueryBuilder("select MAX(ID) from Componente");

	// ID
	// Precisamos somar 1 ao ID para que nao tenha restricoes da chave primaria (unica)
	int componentID = rs.Get<int>(1) + 1;

	std::string strID = std::to_string(componentID);
	std::cout << "Component ID:" << strID << std::endl;

	// Insercao no banco
	st.Execute("insert into Componente values ('" + cpf + "', " + strID + ", '" + componentName + "', " + price + ", 'NAO')");
	con.Commit();
}

void SystemInterface::Component::bestSearch()
{
	std::cout << "---------------- BEST SEARCH -----------------" << std::endl;
	
	ocilib::Resultset rs = QueryBuilder("SELECT anunciante.nome, componente.nome FROM componente INNER JOIN ANUNCIANTE on Componente.anunciante = Anunciante.cpf WHERE Anunciante.avaliacao >= (SELECT AVG(Anunciante.Avaliacao) FROM Anunciante ) GROUP BY Anunciante.nome, componente.nome ORDER BY Anunciante.nome");

	if (rs.GetCount() == 0)
	{
		std::cout << "No components found." << std::endl;
	}
	else {
		// Exibir lista de componentes com aquele nome, bem como o nome dos anunciantes e o preco
		std::cout << "-------------------------------------------" << std::endl;
		std::cout << "|    Anunciante --> Tipo do Componente    |" << std::endl;
		std::cout << "-------------------------------------------" << std::endl;

		// Exibindo na tela todos os componentes existentes no banco
		do {
			std::cout << "|    " << rs.Get<ocilib::ostring>(1) << " --> " << rs.Get<ocilib::ostring>(2) << "    |" << std::endl;
		} while (rs.Next());

		std::cout << "------------------------------------------------" << std::endl << std::endl;
	}
}
