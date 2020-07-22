#include "SystemInterface.h"

void InitializeConnection(ocilib::Connection &con, ocilib::Statement &statement) {
    try {
        // MAKE CONNECTION (REMEMBER TO CHANGE HOST, USERNAME AND PASSWORD TO CONNECT TO DB)
        ocilib::Environment::Initialize();
        con = ocilib::Connection("(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=ENTERYOURHOST)(PORT=ENTERYOURPORT))(CONNECT_DATA=(SERVER=DEDICATED)(SID=orcl)))", "USERNAME", "PASSWORD");

        // SQL COMMAND EXECUTOR
        statement = ocilib::Statement(con);

    } catch (std::exception &ex) {
        std::cout << "Connection Error" << std::endl;
        std::cout << ex.what() << std::endl;
        exit(0);
    }
}

int main(void) {
    // INITIALIZE DATABASE CONNECTION
    ocilib::Connection con;
    ocilib::Statement statement;

    InitializeConnection(con, statement);

    // START OUR INTERFACE
    SystemInterface _interface(con, statement);
    _interface.Loop.Starter();

    std::cout << "Good Bye" << std::endl;

    // FINALIZE APPLICATION
    ocilib::Environment::Cleanup();
    return EXIT_SUCCESS;
}

// Executar programa: Ctrl + F5 ou Menu Depurar > Iniciar Sem Depuração
// Depurar programa: F5 ou menu Depurar > Iniciar Depuração

// Dicas para Começar:
//   1. Use a janela do Gerenciador de Soluções para adicionar/gerenciar arquivos
//   2. Use a janela do Team Explorer para conectar-se ao controle do código-fonte
//   3. Use a janela de Saída para ver mensagens de saída do build e outras mensagens
//   4. Use a janela Lista de Erros para exibir erros
//   5. Ir Para o Projeto > Adicionar Novo Item para criar novos arquivos de código, ou Projeto > Adicionar Item Existente para adicionar arquivos de código existentes ao projeto
//   6. No futuro, para abrir este projeto novamente, vá para Arquivo > Abrir > Projeto e selecione o arquivo. sln
