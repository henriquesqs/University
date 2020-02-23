/**
 * Classe princial da simulacao do jogo Video Poker.
 * Essa classe e' responsavel por controlar toda a jogatina.
 * 
 * @author Henrique de Souza
 * @author Leonardo Rossi
 * 
 */

import java.io.IOException;

public class Main {
	
  /**
   * Metodo auxiliar para mostrar todas as cartas na mao do jogador
   * 
   * @param deck recebe o vetor de cartas do usuario
   * 
   */
  public static void showCards(Baralho deck){

        System.out.print("\n   1           2           3           4           5");
        System.out.println("");
        for (int i = 0; i < 5; i++) {
          for (int j = 0; j < 5; j++) {
              System.out.print(deck.getCard(j).toString(i)+ "     ");
          }
          System.out.print('\n');
        }
        System.out.print('\n');
  }

  public static void main(String[] args) throws IOException{

	boolean flag;  
	  
    Placar placar = new Placar();
    Baralho deck = new Baralho();
    int aposta = 0;
    
    // Iremos rodar o jogo enquanto o usuario possuir dinheiro maior que 0
    while (placar.getMoney() > 0) {

      System.out.println("\nPressione a tecla ENTER para iniciar a rodada.");
      System.out.print("Pressione 0 (zero) para sair.\n");
      
      String enter = EntradaTeclado.leString();
      while (!(enter.equals("")) && !(enter.equals("0"))) {
    	  System.out.println("Por favor, digite novamente!");
    	  enter = EntradaTeclado.leString(); 
      }
      
      if (enter.equals("0")) {
    	  System.out.println("Obrigado e ate a proxima! Adeus!");
    	  return;
      }

      else if (enter.equals("")){

    	flag = false;
        System.out.print("Voce tem " + placar.getMoney() + " creditos. Quanto deseja apostar?\nAposta: ");
        while(!flag) {
        	try {
        		aposta = EntradaTeclado.leInt();
        		flag = true;
        	} 
        	catch (Exception e) {
        		System.out.println("Por favor, digite novamente!");
        	}
        }
        	
        while(aposta <= 0 || aposta > placar.getMoney()){
          
          System.out.println("\nAposta invalida. Lembre-se, voce so pode apostar um valor menor ou igual ao seu saldo e maior do que zero!\n");
          System.out.print("\nVoce tem " + placar.getMoney() + " creditos. Quanto deseja apostar?\nAposta: ");
          flag = false;
          while(!flag) {
          	try {
          		aposta = EntradaTeclado.leInt();
          		flag = true;
          	} 
          	catch (Exception e) {
          		System.out.println("Por favor, digite novamente!");
          	}
          }

        }
        
        // Iniciando o vetor de cartas do usuario
        for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }

        showCards(deck);

        int switchCards = 2; // O usuario pode realizar no maximo duas trocas de cartas, podendo escolher de 0-5 de suas cartas

        while(switchCards != 0){ // enquanto o usuario poder trocar de cartas, iremos perguntar a ele se ele gostaria de o fazer
          
          System.out.print("Deseja trocar alguma de suas cartas?\nSe sim, digite SIM. Do contrario, digite NAO:\nSua escolha: ");
          
          String changing = EntradaTeclado.leString();
          while(!(changing.equals("sim")) && !(changing.equals("SIM")) && !(changing.equals("nao")) && !(changing.equals("NAO"))) {
        	  System.out.println("Por favor, digite novamente!");
        	  changing = EntradaTeclado.leString();
          }
          
          if(changing.equals("sim") || changing.equals("SIM")){
            
            System.out.print("\nQuais cartas gostaria de trocar? (digite separando os numeros por espaco)\nTroque as cartas ");

            String cardsToChange = EntradaTeclado.leString();
            String[] _cardsToChange = cardsToChange.split(" ");
            
            for(int i = 0; i < _cardsToChange.length; i++)
               deck.getCards(Integer.parseInt(_cardsToChange[i]) - 1);

            showCards(deck);
            
            switchCards -= 1;
          }

          else if(changing.equals("nao") || changing.equals("NAO") || changing.equals("n�o") || changing.equals("N�O")){
            System.out.println("\nOk. Iremos iniciar a rodada. Boa sorte!");
            switchCards = 0;
          }
          
          else {
              System.out.println("\nResposta invalida. Vamos entender que voce nao quer trocar nenhuma. :P");
              switchCards = 0;
          }
        }

        placar.getScore(deck.getVetor(), 5, aposta);
        int credit = placar.getMoney();
        System.out.println("\nSeu saldo apos sua aposta: " + credit + "\n");
      }
    }

    if(placar.getMoney() == 0)
      System.out.println("\nQue pena, voce perdeu todo seu dinheiro >:D");
    
    else if(placar.getMoney() > 0)
      System.out.println("\nObrigado por participar do nosso jogo. Espero que tenha se divertido!");
    
    return;
  }
}
