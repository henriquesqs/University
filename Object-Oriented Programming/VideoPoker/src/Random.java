/**
 * Classe de geracao aleatoria de numeros com ou sem 
 * valor maximo e minimo. Baseada na classe produzida
 * pelo professor Delamaro.
 * 
 * @author Henrique de Souza
 * @author Leonardo Rossi
 * 
 */

import java.util.*;
import java.util.concurrent.TimeUnit;

public class Random {

    // parametros para geracao do numero aleatório
    private long p = 2147483648L;
    //private long m = 843314861;
    //private long a = 453816693;
    
    private long xi = 1023; // seed
    
    /**
     * Construtor da classe random, com semente dada pela chamada
     * 
     * @param k nova seed definida pelo usuario
     * 
     */
    public Random(int k){ 
        xi = k; // inicializacao da semente
    }

    /**
     * Construtor da classe Random. Gera um valor 'xi' de acordo
     * com o tempo, em millisegundos, da maquina.
     * 
     */
    public Random(){

        xi = Calendar.getInstance().getTimeInMillis() % p;
    
        // O try-catch serve para dar um "delay" (atraso) na geracao de numeros
        // que sao feitos num intervalo muito próximo

        try{
            TimeUnit.MICROSECONDS.sleep(11333);
        }catch(InterruptedException x){
            
        }
        
    }
    
 /**
  * Funcao que retorna um numero aleatorio no intervalo [0,1)
  * 
  * @param max valor maximo para a geracao do numero aleatorio
  * @return o numero gerado 
  */
    public int getIntRand(int max){

        try{
            TimeUnit.MILLISECONDS.sleep(5);
        }catch(InterruptedException x){
            
        }
        
        return (int) ((long)Calendar.getInstance().getTimeInMillis() % (max)); // calculo do proximo xi (entre 0-1)
    
    }

    /**
     * Funcao que gera um numero aleatorio no intervalo (min, max)
     * 
     * @param min intervalo minimo de geracao do numero aleatorio
     * @param max intervalo maximo de geracao do numero aleatorio
     * @return numero aleatorio no intervalo (min, max)
     * @throws IllegalArgumentException parametros invalidos
     * 
     */
    
    public int getIntRand(int min, int max) throws IllegalArgumentException {

        if(max <= min)
            throw new IllegalArgumentException("Parametros invalidos");
        
        return getIntRand(max-min) + min;
    }

    /**
     * Funcao que retorna um valor gerado entre (0, Integer.MAX_VALUE)
     * 
     * @return numero inteiro entre 0 e MAX_VALUE
     * 
     */
    public int getIntRand(){
        return getIntRand(Integer.MAX_VALUE); 
    }

    /**
     * Funcao que define a semente de geracao de numeros aleatorios
     * 
     * @param k nova semente k
     * 
     */
    public void setSemente(int k){
        xi = k; // alteracao da semente
    }
}