import static org.junit.Assert.*;

import org.junit.Test;

public class JUnit {
	
	@Test
	public void testSetNumero() {
	
		Carta carta = new Carta();	
		carta.setNumero(3);
		
		assertEquals(3, carta.getNumero());
		
	}
	
	@Test
	public void testGetMoney() {
		Placar placar = new Placar();
		assertEquals(200, placar.getMoney());
	}
	
	@Test
	public void testSetNaipe() {
		Carta carta = new Carta();	
		carta.setNaipe(0);
		assertEquals(0, carta.getNaipe());
	}
	
	@Test
	public void testDeck() {
		
		Baralho deck = new Baralho();
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }	
	
		
		deck.getCard(0).setNumero(2);
		deck.getCard(0).setNaipe(2);
		deck.getCard(1).setNumero(2);
		deck.getCard(1).setNaipe(3);
		
		assertEquals(2, deck.getCard(0).getNumero());
		assertEquals(2, deck.getCard(1).getNumero());
		assertEquals(2, deck.getCard(0).getNaipe());
		assertEquals(3, deck.getCard(1).getNaipe());
		
		deck.resetBaralho();
		
	}
	
	@Test
	public void test2PARES() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(2);
		deck.getCard(1).setNumero(2);
		deck.getCard(2).setNumero(3);
		deck.getCard(3).setNumero(3);
		deck.getCard(4).setNumero(4);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(1);
		deck.getCard(2).setNaipe(2);
		deck.getCard(3).setNaipe(3);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
	
	@Test
	public void testTrinca() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(2);
		deck.getCard(1).setNumero(2);
		deck.getCard(2).setNumero(2);
		deck.getCard(3).setNumero(3);
		deck.getCard(4).setNumero(4);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(1);
		deck.getCard(2).setNaipe(2);
		deck.getCard(3).setNaipe(3);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
	
	@Test
	public void testStraight() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(2);
		deck.getCard(1).setNumero(3);
		deck.getCard(2).setNumero(4);
		deck.getCard(3).setNumero(5);
		deck.getCard(4).setNumero(6);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(1);
		deck.getCard(2).setNaipe(2);
		deck.getCard(3).setNaipe(3);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
	
	@Test
	public void testFlush() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(5);
		deck.getCard(1).setNumero(2);
		deck.getCard(2).setNumero(10);
		deck.getCard(3).setNumero(7);
		deck.getCard(4).setNumero(13);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(0);
		deck.getCard(2).setNaipe(0);
		deck.getCard(3).setNaipe(0);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
	
	@Test
	public void testFullHand() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(3);
		deck.getCard(1).setNumero(3);
		deck.getCard(2).setNumero(3);
		deck.getCard(3).setNumero(4);
		deck.getCard(4).setNumero(4);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(1);
		deck.getCard(2).setNaipe(2);
		deck.getCard(3).setNaipe(3);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
	
	@Test
	public void testQuadra() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(3);
		deck.getCard(1).setNumero(3);
		deck.getCard(2).setNumero(3);
		deck.getCard(3).setNumero(3);
		deck.getCard(4).setNumero(4);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(1);
		deck.getCard(2).setNaipe(2);
		deck.getCard(3).setNaipe(3);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
	
	@Test
	public void testStraightFlush() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(3);
		deck.getCard(1).setNumero(4);
		deck.getCard(2).setNumero(5);
		deck.getCard(3).setNumero(6);
		deck.getCard(4).setNumero(7);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(0);
		deck.getCard(2).setNaipe(0);
		deck.getCard(3).setNaipe(0);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
	
	@Test
	public void testRoyalStraightFlush() {
		
		Baralho deck = new Baralho();
		Placar placar = new Placar();
		
		for(int i = 0; i < 5; i++){
          deck.getCards(i);
        }
		
		deck.getCard(0).setNumero(10);
		deck.getCard(1).setNumero(11);
		deck.getCard(2).setNumero(12);
		deck.getCard(3).setNumero(13);
		deck.getCard(4).setNumero(14);
		
		deck.getCard(0).setNaipe(0);
		deck.getCard(1).setNaipe(0);
		deck.getCard(2).setNaipe(0);
		deck.getCard(3).setNaipe(0);
		deck.getCard(4).setNaipe(0);
		
		placar.getScore(deck.getVetor(), 5, 100);
			
	}
}
