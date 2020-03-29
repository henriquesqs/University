import javax.swing.JOptionPane;

/**
 * Classe responsavel por controlar o placar/ pontuacao do jogo.
 * Aqui serao verificadas quais combinacoes o usuario conseguiu fazer
 * e o dinheiro do usuario sera controlado
 * 
 * @author Henrique de Souza
 * @author Leonardo Rossi
 *
 */
public class Placar {

  private int money;

  /**
   * Metodo construtor da classe Placar. Inicializa o saldo do usuario com 200.
   * 
   */
  public Placar() {
    this.money = 200;
  }

  /**
   * Metodo que retorna o saldo atual do jogador
   * 
   * @return o saldo atual do jogador
   */
  public int getMoney() {
    return this.money;
  }

  /**
   * Funcao que fara a verificacao se o jogador conseguiu alguma combinacao de
   * cartas e verificara qual o seu retorno financeiro.
   * 
   * Combinacoes possiveis:
   * 
   * Dois pares (por exemplo: 2,2,3,4,3) Trinca (por exemplo: 2, 2, 3, 2, 4)
   * Straight: 5 cartas seguidas de naipes diferentes Flush: 5 cartas do mesmo
   * naipe nao seguidas Fullhand: uma trinca e um par Quadra (por exemplo: 2, 2,
   * 2, 4, 2) StraightFlush: 5 cartas seguidas do mesmo naipe Royal Straight
   * Flush: 5 cartas seguidas do mesmo naipe de 10 até o As
   * 
   * @param cartas    vetor de objetos Carta
   * @param numCartas quantidade de cartas na mao do jogador
   * @param aposta valor da aposta do jogador
   * 
   */
  public void getScore(Carta[] cartas, int numCartas, int aposta) {

    int[][] vet = new int[2][15];
    int trinca = 0, pares = 0, quadra = 0, straight = 0, flush = 0, royal = 0;
    
    this.money -= aposta; // removendo do saldo do usuario o quanto ele apostou

    // Preenchendo o vetor auxiliar com a quantidade de ocorrencias
    // de cada numero de carta e naipe no baralho
    for (int i = 0; i < numCartas; i++){

      int index = cartas[i].getNumero();
      int naipe = cartas[i].getNaipe();

      vet[0][index]++;
      vet[1][naipe]++;

    }

    // Verificando se possuimos 5 cartas do mesmo naipe
    for (int i = 0; i < 5; i++)
      if (vet[1][i] == 5)
        flush++;

    // Verificando a ocorrencia de dois pares ou uma trinca ou uma quadra.
    // Alem disso, utilizamos esse laco para verificar a ocorrencia de um straight
    // (estamos vendo se as 5 cartas sao diferentes)
    
    for (int i = 0; i < 15; i++) {

      if (vet[0][i] == 2)
        pares++;

      else if (vet[0][i] == 3)
        trinca++;

      else if (vet[0][i] == 4)
        quadra++;

      else if (vet[0][10] == 1 && vet[0][11] == 1 && vet[0][12] == 1 && vet[0][13] == 1 && vet[0][14] == 1) 
    	royal++;
      
      else if(i <= 10 && vet[0][i] == 1 && vet[0][i+1] == 1 && vet[0][i+2] == 1 && vet[0][i+3] == 1 && vet[0][i+4] == 1)
    	straight++;
    }
 
    // Se houver uma sequencia de cartas do 8 ate o As de mesmo naipe, recebe 200x o valor da aposta
    if (flush == 1 && royal >= 1) {
    	JOptionPane.showMessageDialog(null, "PARABENSSSSSSS! Voce conseguiu um Royal Straight Flush!\nPremio: 200x o valor da aposta!!!");
//    	System.out.println("\nPARABENSSSSSSS! Voce conseguiu um Royal Straight Flush!\nPremio: 200x o valor da aposta.");
        this.money += (200 * aposta);
        return;
    }
    
    // Se encontrarmos um straight flush, o premio e' 100x o valor da aposta
    if (straight == 1 && flush == 1) {
    	JOptionPane.showMessageDialog(null, "Parabens! Voce conseguiu um straight flush!\nPremio: 100x o valor da aposta.");
//      System.out.println("\nParabens! Voce conseguiu um straight flush!\nPremio: 100x o valor da aposta.");
      this.money += (100 * aposta);
      return;
    }
    
    // Se houverem 4 cartas iguais, recbe 50x o valor da aposta
    if (quadra == 1) {
    	JOptionPane.showMessageDialog(null, "Parabens! Voce conseguiu uma quadra!\nPremio: 50x o valor da aposta.");
//      System.out.println("\nParabens! Voce conseguiu uma quadra!\nPremio: 50x o valor da aposta.");
      this.money += (50 * aposta);
      return;
    }
    
    // Verificando se possuimos um fullhand. O premio e' 20x a aposta.
    if (pares == 1 && trinca == 1) {
    	JOptionPane.showMessageDialog(null, "Parabens! Voce conseguiu um fullhand!\nPremio: 20x o valor da aposta.");
//      System.out.println("\nParabens! Voce conseguiu um fullhand!\nPremio: 20x o valor da aposta.");
      this.money += (20 * aposta);
      return;
    }
    
    // Se houverem 5 cartas do mesmo naipe nao seguidas, recebe 10x o valor da aposta
    if (flush == 1 && straight == 0) {
    	JOptionPane.showMessageDialog(null, "Parabens! Voce conseguiu um flush!\nPremio: 10x o valor da aposta.");
//      System.out.println("\nParabens! Voce conseguiu um flush!\nPremio: 10x o valor da aposta.");
      this.money += (10 * aposta);
      return;
    }
    
    // Se houverem 5 cartas diferentes (com naipes diferentes), recebe 5x o valor da aposta
    if (straight == 1 && flush == 0) {
    	JOptionPane.showMessageDialog(null, "Parabens! Voce conseguiu um straight!\nPremio: 5x o valor da aposta.");
//      System.out.println("\nParabens! Voce conseguiu um straight!\nPremio: 5x o valor da aposta.");
      this.money += (5 * aposta);
      return;
    }
    
    // Se tiver 1 trinca, recebe 2x o valor da aposta
    if (trinca == 1 && pares == 0) {
    	JOptionPane.showMessageDialog(null, "Parabens! Voce conseguiu uma trinca!\nPremio: 2x o valor da aposta.");
//      System.out.println("\nParabens! Voce conseguiu uma trinca!\nPremio: 2x o valor da aposta.");
      this.money += (2 * aposta);
      return;
    }
    
    // Se houver 2 pares, recebe a quantia que gastou
    if (pares == 2) {
    	JOptionPane.showMessageDialog(null, "Parabens! Voce conseguiu dois pares!\nPremio: valor da aposta.");
//      System.out.println("\nParabens! Voce conseguiu dois pares!\nPremio: valor da aposta.");
      this.money += aposta;
      return;
    } 
  }
}