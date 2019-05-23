import java.util.Random;

/**
 * Classe responsavel por controlar o vetor de cartas do jogo.
 * Aqui serao distribuidas as cartas (gerando o numero e naipe de cada uma.
 *
 * @author Henrique de Souza
 * @author Leonardo Rossi
 * 
 */

public class Baralho{
	
  
  private int[][] baralho;
  private Carta[] cartas;
  private Random r1 = new Random();
  
  	
  	// Construtor da classe Baralho
  	public Baralho() {
  		baralho = new int[52][4];
  		cartas = new Carta[5];
  	}
    
    /**
     * Metodo para gerar o vetor de cartas do usuario, anotando
     * quais cartas ja foram distribuidas.
     * 
     * @param i indice da catra que gostaria de gerar
     * 
     */
    public void getCards(int i){

	int numero = gerarNumero();
    int naipe = gerarNaipe();
      
	while(baralho[numero][naipe] == 1){
		numero = gerarNumero();
		naipe = gerarNaipe();
	}
    	        
	baralho[numero][naipe] = 1;
	
	if (cartas[i] == null) cartas[i] = new Carta();
	cartas[i].setNumero(numero);
	cartas[i].setNaipe(naipe);

    }
    
    
    /**
     * Metodo que reseta o baralho, fazendo com que todas as cartas
     * que ja foram utilizadas voltem ao baralho
     * 
     */
    public void resetBaralho(){
    	baralho = new int[52][4];
    }
    
    
    /**
     * Retorna uma unica carta do vetor de cartas
     * 
     * @param i indice da carta que gostaria de retornar
     * @return carta a ser retornada
     */
    public Carta getCard(int i){
      return cartas[i];
    }
    
    /**
     * Metodo para retornar o vetor contendo todas as cartas do usuario
     * 
     * @return vetor de cartas do usuario
     */
    public Carta[] getVetor(){
      return cartas;
    }

    /**
     * Funcao que gera o naipe da carta (0-3) atraves da
     * geracao de numeros aleatorios dentro desse intervalo
     * 
     * @return o naipe gerado paraa carta
     * 
     */
    public int gerarNaipe(){

        // Estamos gerando o naipe no intervalo de 0 - 3
        // 0 - ouro ; 1 - espadas ; 2 - copas ; 3 - paus
        
//    	int naipe = (r1.getIntRand(4));    	

        return r1.nextInt(4);
    }

    /**
     * Esse metodo gera um numero aleatorio no intervalo de 2-14
     * atraves da geracao de numeros aleatorios nesse intervalo
     * 
     * @return o numero gerado para a carta
     * 
     */
    public int gerarNumero(){
        
//      int numero = (r1.getIntRand(2, 15));
    	    	    	
    	int numero = r1.nextInt(13) + 2;
    	    		   
        return numero;
    }
}