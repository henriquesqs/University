// Trabalho desenvolvido por
// Henrique de Souza Q. dos Santos, Nº USP 10819029
// Leonardo Rossi Luiz, Nº USP 10851691
// USP - São Carlos, 2019

import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

@SuppressWarnings({"unused", "serial"})
public class VideoPokerGUI extends JFrame implements ActionListener {
	
	private int money;
	private int aposta;
	private int trocas;
    private Baralho deck;
	private Placar placar;    
    
    private JFrame frameInicial;
    private JFrame frameJogo;
    
    private StringBuilder text;
	private JTextField textField;
	private JTextArea txtrSeuSaldo;
	private JTextArea txtrSuaAposta;
	private JTextField betInput;
	
	private JCheckBox CheckCarta[];	
	private JLabel lblCarta[];
	
	private final Action ExitGame;
	private final Action StartGame;
	private final Action Instructions;
	private final Action ChangeCards;
	private final Action Bet;
	
	private static VideoPokerGUI framePrincipal;		
	
	private JButton btnBet;
	private JButton btnExit;	
	private JButton btnStart;
	private JButton btnChange;
	private JButton btnInstructions;
	
	private JLabel saldo;
	private JLabel pressEnter;
	
	// Construtor da GUI do Video Poker
    public VideoPokerGUI() {
    	
    	super("VideoPoker: o jogo de apostas online");
    	    	
    	aposta = 0;
    	trocas = 2;
    	placar = new Placar();
        deck = new Baralho();
        money = placar.getMoney();
        
        Bet = new Bet();
        frameInicial = new JFrame();        
		ExitGame = new ExitGame();
		StartGame = new StartGame();
		Instructions = new Instructions();
		ChangeCards = new ChangeCards();
        
        // Abaixo escrevemos o texto que sera exibido na tela inicial ao clicar no botao "instrucoes"
        text = new StringBuilder();
        text.append("INSTRUCOES PARA A UTILIZACAO DO JOGO\r\n" + 
				"		\r\n" + 
				"		Similiar ao Poker normal, o VideoPoker e' um jogo de aposta utilizando cartas.\r\n" + 
				"		O jogador recebe 5 cartas a cada rodada, com direito a 2 trocas de 1 - 5 cartas."
				+ "		\r\n" + 
				"		O jogo ira' calcular automaticamente se o usuario conseguir alguma combinacao de cartas, sendo elas: \r\n" + 
				"		\r\n" + 
				"		DOIS PARES: o premio e' o valor da aposta;\r\n" + 
				"		TRINCA: o premio e' 2x o valor da aposta;\r\n" + 
				"		STRAIGHT (5 cartas seguidas de naipes diferentes): o premio e' 5x o valor da aposta;\r\n" + 
				"		FLUSH (5 cartas do mesmo naipe nao seguidas): o premio e' 10x o valor da aposta;\r\n" +
				"		FULL HAND (uma trinca e um par): o premio e' 20x o valor da aposta;\r\n" +
				"		QUADRA : o premio e' 50x o valor da aposta;\r\n" +
				"		STRAIGHT FLUSH (5 cartas seguidas do mesmo naipe): o premio e' 100x o valor da aposta;\r\n" +
				"		ROYAL STRAIGHT FLUSH (5 cartas seguidas do mesmo naipe de 10 ate As): o premio e' 200x o valor da aposta.\r\n" +
				"\r\n Espero que voce tenha uma boa experiencia. Boa sorte!" +
				"	\r\n");	
		
		// Botao de "Iniciar o Jogo"		
		btnStart = new JButton("Iniciar");
		btnStart.setFont(new Font("Roboto", Font.BOLD, 16));
		btnStart.setForeground(Color.WHITE);
		btnStart.setBackground(Color.GREEN);
		btnStart.setAction(StartGame);
		btnStart.setBounds(226, 227, 89, 23);
		frameInicial.getContentPane().add(btnStart);
			
		// Botao de "Sair do Jogo"
		btnExit = new JButton("Sair");
		btnExit.setBackground(Color.RED);
		btnExit.setForeground(Color.WHITE);
		btnExit.setFont(new Font("Roboto", Font.BOLD, 16));
		btnExit.setAction(ExitGame);
		btnExit.setBounds(89, 227, 89, 23);
		frameInicial.getContentPane().add(btnExit);
		
		// Botao de "Trocar" cartas
		btnChange = new JButton("Trocar");
		btnChange.setBackground(Color.BLUE);
		btnChange.setForeground(Color.WHITE);
		btnChange.setFont(new Font("Roboto", Font.BOLD, 16));
		btnChange.setAction(ChangeCards);
		btnChange.setBounds(255, 182, 110, 23);
		frameInicial.getContentPane().add(btnChange);
		
		// Botao de "Instrucoes"
		btnInstructions = new JButton("INSTRUCOES");
		btnInstructions.setFont(new Font("Roboto", Font.BOLD, 16));
		btnInstructions.setAction(Instructions);
		btnInstructions.setBackground(Color.ORANGE);
		btnInstructions.setForeground(Color.WHITE);
		btnInstructions.setBounds(146, 178, 128, 23);
		frameInicial.getContentPane().add(btnInstructions);
		
		// Botao de "Apostar"		
		btnBet = new JButton("APOSTAR");
		btnBet.setFont(new Font("Roboto", Font.BOLD, 16));
		btnBet.setForeground(Color.WHITE);
		btnBet.setBackground(Color.GREEN);
		btnBet.setAction(Bet);
		btnBet.setBounds(255, 212, 110, 23); // 294, 169, 114, 92
		frameInicial.getContentPane().add(btnBet);
		
		// Esse JTextArea eh responsavel por mostrar o texto "Sua Aposta" na guia
		txtrSuaAposta = new JTextArea();
		txtrSuaAposta.setFont(new Font("Roboto", Font.BOLD, 13));
		txtrSuaAposta.setEditable(false);
		txtrSuaAposta.setText(" SUA APOSTA:");
		txtrSuaAposta.setBounds(54, 212, 88, 21);
		
		// Esse JTextArea eh responsavel por mostrar o texto "Seu Saldo" na guia
		txtrSeuSaldo = new JTextArea();
		txtrSeuSaldo.setText(" SEU SALDO:");
		txtrSeuSaldo.setFont(new Font("Roboto", Font.BOLD, 13));
		txtrSeuSaldo.setEditable(false);
		txtrSeuSaldo.setBounds(54, 182, 88, 22);
		
    	// Esse JTextField eh responsavel por criar o campo onde o usuario digitara o valor da aposta
    	betInput = new JTextField();
    	betInput.setBounds(152, 213, 86, 20);
		betInput.setColumns(10);	
		
		// Esse label vai controlar o saldo do usuario
		saldo = new JLabel("");
		saldo.setBounds(152, 186, 86, 14);
		saldo.setText(Integer.toString(money));	
		
		// Adicionando a imagem principal do jogo
		JLabel imagemPrincipal = new JLabel("");
		Image img = new ImageIcon(this.getClass().getResource("/image4.png")).getImage();
		imagemPrincipal.setIcon(new ImageIcon(img));
		imagemPrincipal.setBounds(10, 22, 414, 129);
		frameInicial.getContentPane().add(imagemPrincipal);
		
		// Abaixo iremos criar as "labels" que controlarao as 
		// imagens das cartas e as "checkBoxes" que controlarao as 
		// escolhas das cartas que serao trocadas a cada rodada
		
		lblCarta = new JLabel[5];
		CheckCarta = new JCheckBox[5];
		for(int i = 0; i < 5; i++) {
			lblCarta[i] = new JLabel("Carta "+i);
			CheckCarta[i] = new JCheckBox("CheckBox"+i);
		}
		
		lblCarta[0].setBounds(30, 11, 65, 102);
		lblCarta[1].setBounds(105, 11, 65, 102);
		lblCarta[2].setBounds(180, 11, 65, 102);
		lblCarta[3].setBounds(255, 11, 65, 102);
		lblCarta[4].setBounds(332, 11, 65, 102);

		CheckCarta[0].setBounds(54, 120, 21, 23);
		CheckCarta[1].setBounds(128, 120, 21, 23);		
		CheckCarta[2].setBounds(203, 120, 21, 23);
		CheckCarta[3].setBounds(277, 120, 21, 23);	
		CheckCarta[4].setBounds(352, 120, 21, 23);
		
		// Abaixo adicionamos os elementos da tela principal
		this.add(btnStart);
		this.add(btnExit);
		this.add(btnInstructions);
		this.add(imagemPrincipal);

    }
    
    // Metodo que inicia o jogo
    public void startGame() throws IllegalArgumentException{
    	
    	// Abrindo a nova guia do jogo
    	frameJogo = new JFrame("VideoPoker: o jogo de apostas online");    	
    	frameJogo.setBounds(100, 100, 450, 300);
    	frameJogo.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    	frameJogo.getContentPane().setLayout(null);
    	frameJogo.setVisible(true);
    	
    	btnExit.setBounds(255, 150, 110, 23);
    	frameJogo.add(btnExit); // Adicionando botao de "sair" do jogo		
    	frameJogo.add(btnBet);	// Adicionando botao de "aposta" do jogo
		frameJogo.getContentPane().add(betInput); // Adicionando o campo que o usuario digita a aposta
		frameJogo.getContentPane().add(txtrSuaAposta); // Adicionando o texto "sua aposta"
		frameJogo.getContentPane().add(txtrSeuSaldo); // Adicionando o texto "seu saldo"
		frameJogo.getContentPane().add(saldo); // Adicionando o saldo do usuario na tela
		frameJogo.add(btnChange); // adicionando o botao de "trocar" do jogo
			
		
		// Gerando as cartas do usuario
		for(int i = 0; i < 5; i++) {
			deck.getCards(i);
			CheckCarta[i].setSelected(false);
			CheckCarta[i].setEnabled(true);
		}
					
		showCardsImage(deck);
		
		JOptionPane.showMessageDialog(null, "Deseja trocar alguma(s) carta(s)? Se sim, marque-as clicando na caixa"
				+ " de selecao\n em baixo da carta que desejar trocar. Ao final de sua escolha, clique no botao APOSTAR.");		
    }
    
    // Metodo que retorna uma string contendo o naipe da carta
    public String getSuit(int naipe) {
    	
    	String suit = null;
    	if(naipe == 0) {
			suit = "diamonds";
		}
		else if(naipe == 1){
			suit = "spades";
		}
		else if(naipe == 2) {
			suit = "hearts";
		}
		else if(naipe == 3) {
			suit = "clubs";
		}
    	return suit;
    }
    
    // Metodo responsavel por exibir na tela as imagens das cartas
    public void showCardsImage(Baralho deck) {
    	
    	Image img;
		String suit = null;
    	
    	for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 5; j++) {
				
				int naipe = deck.getCard(j).getNaipe(); // pegando o naipe da carta				
				int numero = deck.getCard(j).getNumero(); // pegando o numero da carta
				
				suit = getSuit(naipe); // convertendo o naipe (0-3) para uma string (0: diamonds, 1: spades, 2: hearts, 3: clubs)
				
				img = new ImageIcon(this.getClass().getResource("/"+numero+"_of_"+suit+".jpg")).getImage();
				lblCarta[j].setIcon(new ImageIcon(img));
				frameJogo.getContentPane().add(lblCarta[j]);
				frameJogo.getContentPane().add(CheckCarta[j]);
				
			}
		}
    	
    }
    
	// Metodo responsavel por criar a aï¿½ao de finalizacao do jogo ao clicar no botao
	private class ExitGame extends AbstractAction {
		public ExitGame() {
			putValue(NAME, "sair");
			putValue(SHORT_DESCRIPTION, "Finaliza o jogo");
			
		}
		public void actionPerformed(ActionEvent e) {			
			
			JOptionPane.showMessageDialog(null, "Obrigado por participar do nosso jogo!\n"
					+ "Esperamos que tenha se divertido");
			System.exit(0);			
			
		}
	}
	
	// Metodo responsavel por criar a acao de troca de cartas selecionadas ao clicar no botao
	private class ChangeCards extends AbstractAction {
		public ChangeCards() {
			putValue(NAME, "trocar");
			putValue(SHORT_DESCRIPTION, "Troca as cartas marcadas nas caixas de selecao");
			
		}
		public void actionPerformed(ActionEvent e) {
			int selected = 0;
			
			for(int i = 0; i < 5; i++)  // verificando quais das caixas de selecao estao marcadas
				if(CheckCarta[i].isSelected()) selected++; // contando quantas cartas foram marcadas
			
			if(selected == 0) { // se o usuario nao selecionou nenhuma carta e clicou no botao de trocar
				JOptionPane.showMessageDialog(null, "Voce nao selecionou nenhuma carta para trocar.");
				return;
			}
			
			else if(trocas == 0) { // se o usuario nao pode mais trocar as cartas
				JOptionPane.showMessageDialog(null, "Voce nao pode mais trocar nenhuma carta. Por favor, clique em APOSTAR");
				return;
			}
			
			for(int i = 0; i < 5; i++) {
				if(CheckCarta[i].isSelected() && trocas > 0) {
					deck.getCards(i);
				}
			}
			trocas--;
			showCardsImage(deck);
		}
	}
	
	// Metodo responsavel por criar a acao de inicializacao do jogo ao clicar no botao
	private class StartGame extends AbstractAction {
		public StartGame() {
			putValue(NAME, "Iniciar");
			putValue(SHORT_DESCRIPTION, "Clique para iniciar o jogo");
		}
		public void actionPerformed(ActionEvent e) {
			framePrincipal.setVisible(false);
			startGame();
		}
	}
	
	// Metodo responsavel por criar a acao de mostrar mensagem de instrucao do jogo ao clicar no botao
	private class Instructions extends AbstractAction {
		public Instructions() {
			putValue(NAME, "Instrucoes");
			putValue(SHORT_DESCRIPTION, "Clique para visualizar as instrucoes do jogo");
		}
		public void actionPerformed(ActionEvent e) {	    
			JOptionPane.showMessageDialog(frameInicial.getComponent(0), text);			
		}
	}
	
	// Metodo responsavel por criar a acao de aposta no jogo ao clicar no botao
	private class Bet extends AbstractAction {
		public Bet() {
			putValue(NAME, "APOSTAR");
			putValue(SHORT_DESCRIPTION, "Clique para apostar o valor digitado acima");
		}
		public void actionPerformed(ActionEvent e) {
		
			try { // vamos verificar se o usuario digitou um input valido
				aposta = Integer.parseInt(betInput.getText());				
			}
			catch(Exception f) { // se ele digitar uma aposta diferente de numeros, lanï¿½amos uma mensagem
				JOptionPane.showMessageDialog(null, "Valor invalido. Por favor, digite um valor com numeros de 0-9!");
				return;
			}
			
			if(aposta <= 0) { // se ele digitar uma aposta <= 0
				JOptionPane.showMessageDialog(null, "Aposta invalida. Digite um valor maior que zero! Se desejar sair, clique no botao 'sair'!");
				return;
			}
			else if(aposta > placar.getMoney()) { // se ele digitar uma aposta > o saldo dele
				JOptionPane.showMessageDialog(null, "Aposta invalida. Voce so pode apostar um valor menor ou igual ao seu saldo!");
				return;
			}
		
			// Calculando o resultado da aposta
			placar.getScore(deck.getVetor(), 5, aposta);
			money = placar.getMoney();
			
			// Atualizando o mostrador do saldo
			saldo.setText(Integer.toString(money));
			
			if(money == 0) {
				JOptionPane.showMessageDialog(null, "Que pena, voce perdeu toda a sua grana! >:D");
				System.exit(0);
			}
			
			else {				
				
				for(int i = 0; i < 5; i++) {
					deck.getCards(i);
					CheckCarta[i].setSelected(false);
					CheckCarta[i].setEnabled(true);
				}
				
				trocas = 2;				
				showCardsImage(deck);		
				deck.resetBaralho();
				
				// DESCOMENTAR PARA COLOCAR O AVISO DE "SELECIONE CARTAS PARA TROCAR" TODA VEZ QUE APOSTAR
//				JOptionPane.showMessageDialog(null, "Deseja trocar alguma(s) carta(s)? Se sim, marque-as clicando na caixa"
//						+ " de selecao\n em baixo da carta que desejar trocar. Ao final de sua escolha, clique no botao APOSTAR.");		
			}			
		}
	}	
	
	public static void main(String[] args) {
		
		framePrincipal = new VideoPokerGUI();
		framePrincipal.setBounds(100, 100, 450, 300);
		framePrincipal.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		framePrincipal.getContentPane().setLayout(null);
		framePrincipal.setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) {
		// TODO Auto-generated method stub
		
	}
}