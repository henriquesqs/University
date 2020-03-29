/**
 * Classe principal que controla o objeto Carta, o naipe e o numero
 * desse objeto.
 * 
 * @author Henrique de Souza
 * @author Leonardo Rossi
 * 
 */
public class Carta{
    
    private int numero; // 2-14
    private int naipe; // 0-3

    /**
     * Metodo que mostra qual o numero da carta selecionada
     * 
     * @param numero numero o qual queremos setar a carta
     * 
     */
    public void setNumero(int numero){
      this.numero = numero;
    }

    /**
     * Funcao que mostra o naipe da carta selecionada
     * 
     * @param naipe naipe a qual queremos setar a carta
     * 
     */
    public void setNaipe(int naipe){
      this.naipe = naipe;
    }
    
    /**
     * Metodo para retornar o naipe da carta
     * 
     * @return naipe da carta que o chamou
     */
    public int getNaipe(){
      return this.naipe;
    }
    
    /**
     * Metodo para retornar o numero da carta
     * 
     * @return numero da carta que o chamou
     */
    public int getNumero(){
      return this.numero;
    }
    
	/**
	 * Estamos sobrecarregando a funcao toString para representa, graficamente,
	 * os dados que queremos mostrar
	 * 
	 * @param i indice de carta estamos lidando
	 * @return null se encontrar algum erro
	 */
    public String toString(int i){
        
        int ouro = 0, espada = 0, copas = 0, paus = 0;

        switch(this.naipe){
            case 0: 
                ouro = 1;
                break;
            case 1: 
                espada = 1;
                break;
            case 2: 
                copas = 1;
                break;
            case 3: 
                paus = 1;
                break;
        }

        switch(this.numero){

            case 2:

                if(ouro == 1) {

                    if (i == 0) return "+-----+";
                    if (i == 1) return "|2   2|";
                    if (i == 2) return "|  \u2666  |";
                    if (i == 3) return "|2   2|";
                    if (i == 4) return "+-----+";
                }

                if(espada == 1){

                    if (i == 0) return "+-----+";
                    if (i == 1) return "|2   2|";
                    if (i == 2) return "|  \u2660  |";
                    if (i == 3) return "|2   2|";
                    if (i == 4) return "+-----+";
                }

                if(copas == 1){

                    if (i == 0) return "+-----+";
                    if (i == 1) return "|2   2|";
                    if (i == 2) return "|  \u2665  |";
                    if (i == 3) return "|2   2|";
                    if (i == 4) return "+-----+";
                }

                if(paus == 1){

                    if (i == 0) return "+-----+";
                    if (i == 1) return "|2   2|";
                    if (i == 2) return "|  \u2663  |";
                    if (i == 3) return "|2   2|";
                    if (i == 4) return "+-----+";
                
                }

                break;
                
            case 3:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|3   3|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|3   3|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|3   3|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|3   3|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|3   3|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|3   3|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|3   3|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|3   3|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 4:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|4   4|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|4   4|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|4   4|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|4   4|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|4   4|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|4   4|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|4   4|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|4   4|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 5:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|5   5|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|5   5|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|5   5|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|5   5|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|5   5|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|5   5|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|5   5|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|5   5|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 6:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|6   6|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|6   6|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|6   6|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|6   6|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|6   6|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|6   6|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|6   6|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|6   6|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 7:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|7   7|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|7   7|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|7   7|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|7   7|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|7   7|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|7   7|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|7   7|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|7   7|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 8:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|8   8|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|8   8|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|8   8|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|8   8|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|8   8|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|8   8|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|8   8|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|8   8|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 9:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|9   9|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|9   9|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|9   9|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|9   9|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|9   9|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|9   9|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|9   9|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|9   9|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 10:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|10 10|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|10 10|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|10 10|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|10 10|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|10 10|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|10 10|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|10 10|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|10 10|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 11:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|J   J|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|J   J|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|J   J|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|J   J|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|J   J|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|J   J|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|J   J|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|J   J|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 12:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|Q   Q|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|Q   Q|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|Q   Q|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|Q   Q|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|Q   Q|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|Q   Q|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|Q   Q|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|Q   Q|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 13:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|K   K|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|K   K|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|K   K|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|K   K|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|K   K|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|K   K|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|K   K|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|K   K|";
                    if(i == 4) return "+-----+";
                }
                
                break;

            case 14:

                if(ouro == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|A   A|";
                    if(i == 2) return "|  \u2666  |";
                    if(i == 3) return "|A   A|";
                    if(i == 4) return "+-----+";
                }

                if(espada == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|A   A|";
                    if(i == 2) return "|  \u2660  |";
                    if(i == 3) return "|A   A|";
                    if(i == 4) return "+-----+";
                }

                if(copas == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|A   A|";
                    if(i == 2) return "|  \u2665  |";
                    if(i == 3) return "|A   A|";
                    if(i == 4) return "+-----+";
                }

                if(paus == 1){
                    if(i == 0) return "+-----+";
                    if(i == 1) return "|A   A|";
                    if(i == 2) return "|  \u2663  |";
                    if(i == 3) return "|A   A|";
                    if(i == 4) return "+-----+";
                }
                
                break;
        }

        return null;
    }
}