-- 1. Selecionar e retornar o preco total de cada tipo de Componente presente em determinado Evento, alem do preco total desse evento (soma dos precos de cada 	tipo);

SELECT evento.nome AS Nome_Evento, c.nome AS Nome_Componente, SUM(c.preco) AS Preco_Total_Por_Tipo FROM EVENTO 
INNER JOIN CONTRATO ON EVENTO.ID = contrato.idevento 
INNER JOIN COMPONENTE C ON contrato.idcomponente = c.id
GROUP BY c.nome, evento.nome
ORDER BY evento.nome;

-- 2. Exibir os componentes os quais os Anunciantes possuem nota de avaliacao maior que a media das avaliacões para um determinado tipo de componente;

SELECT anunciante.nome as ANUNCIANTE, componente.nome as NOME_COMPONENTE--, componente.preco AS COMPONENTE_PREcO
FROM componente INNER JOIN ANUNCIANTE on Componente.anunciante = Anunciante.cpf
WHERE Anunciante.avaliacao >= (
    SELECT AVG(Anunciante.Avaliacao) FROM Anunciante
)
GROUP BY Anunciante.nome, componente.nome
ORDER BY Anunciante.nome;

-- 3. Mostrar componentes do tipo Infraestrutura que possuem um Montador cadastrado por Anunciantes com avaliacao maior que a media das avaliacões

SELECT componente.nome as NOME_COMPONENTE, componente.preco AS COMPONENTE_PRECO
FROM componente INNER JOIN INFRAESTRUTURA on infraestrutura.idcomponente = componente.id
INNER JOIN NECESSITA on infraestrutura.idcomponente = necessita.infraestrutura
INNER JOIN ANUNCIANTE on anunciante.cpf = componente.anunciante AND anunciante.avaliacao >= (
    SELECT AVG(Anunciante.Avaliacao) FROM Anunciante 
    );a a quey

-- 4. Buscar Local com uma determinada tensao eletrica (A) que seja a mesma tensao eletrica (A) que um componente do tipo Iluminacao e exibir esses componentes;

SELECT DISTINCT iluminacao.idcomponente AS ID_COMPONENTE, ruas.rua, ruas.bairro from iluminacao, componente 
inner join local on local.idcomponente = componente.id
inner join ruas on ruas.cep = local.cep
WHERE local.tensaoeletrica = iluminacao.tensaoeletrica
ORDER BY iluminacao.idcomponente;

-- 5. Selecionar Anunciantes que possuem mais de X componentes adquiridos por mais que Y Contratantes diferentes;
SELECT Componente.anunciante, Count(*) as nro_vendas from CONTRATO
INNER JOIN Componente on contrato.idcomponente = componente.id 
GROUP BY componente.anunciante
HAVING Count(Contrato.Idcomponente) > 2 AND Count(Contrato.contratante) > 2
ORDER BY Componente.anunciante;

-- 6. Selecionar e exibir, lado-a-lado, todas as combinacões de Produto, Servico e Local cuja a soma de precos seja <= X;

Select SUM(Valor) as TOTAL, p , s, l from

        (SELECT Componente.preco as Valor, Componente.id as IDcomp, PRODUTO as p, SERVIÇO as s, LOCAL as l FROM Componente 
            INNER JOIN 
            (SELECT Produto.idcomponente as PRODUTO, Servicos.idcomponente as SERVIÇO, Local.idcomponente as LOCAL
            FROM Produto, Servicos, Local group by Produto.idcomponente, Servicos.idcomponente, Local.idcomponente) 
            on PRODUTO = Componente.id OR SERVIÇO = Componente.id OR LOCAL = Componente.id 
            group by Componente.preco, Componente.id,  PRODUTO, SERVIÇO, LOCAL 
            order by PRODUTO, SERVIÇO, LOCAL),
        (SELECT Produto.idcomponente as PRODUTO_s, Servicos.idcomponente as SERVIÇO_s, Local.idcomponente as LOCAL_s
            FROM Produto, Servicos, Local group by Produto.idcomponente, Servicos.idcomponente, Local.idcomponente)
    WHERE PRODUTO_s = p AND SERVIÇO_s = s AND LOCAL_s = l GROUP BY p, s, l having SUM(Valor) >= 600 ORDER BY p, s, l;

-- 7. Selecionar e exibir os Anunciantes que possuem mais que X avaliacões e a sua media de avaliacões seja maior que Y;
SELECT Avalia.Anunciante, Anunciante.NOME, Anunciante.EMAIL, Anunciante.AVALIACAO FROM Avalia, Anunciante 
    where UPPER(Avalia.AVALIADOR) = 'CONTRATANTE' AND Anunciante.CPF = Avalia.Anunciante 
    GROUP BY Avalia.Anunciante, Anunciante.NOME, Anunciante.EMAIL, Anunciante.AVALIACAO 
    HAVING COUNT(Avalia.Anunciante) >= 3;

-- 8. Selecionar e exibir os Anunciantes que possuem componentes comprados mais de X vezes por um mesmo Contratante em datas diferentes;
Select Anunciante.cpf as ANUNCIANTE, COUNT(DISTINCT Evento.datainicio) as APARICOES from
    (SELECT Anunciante.cpf as a, Evento.Contratante as c, Componente.id as COMPONENTE, Evento.id as EVENTO, Evento.datainicio as d  
    from Contrato, Componente, Anunciante, Evento 
    where Contrato.idcomponente = Componente.id and Componente.anunciante = Anunciante.cpf and Contrato.idEvento = Evento.id 
    group by Anunciante.cpf, Contrato.Contratante, Evento.Contratante, Componente.id, Evento.id, Evento.datainicio 
    order by Anunciante.cpf),
    Anunciante, Evento
    where Anunciante.cpf = a and Evento.contratante = c and Evento.datainicio != d
    group by Anunciante.cpf HAVING COUNT(DISTINCT Evento.datainicio) >= 2 order by Anunciante.cpf;


-- 9. Exibir a data mais proxima que um componente X (idComponente) do Anunciante Y estará disponível para ser alugado;
--OBS: Será exibido para o User o "ID" do componente entao ele saberá qual o ID do componente ofertado pelo Anunciante X e poder´efetuar a busca em cima desse ID.

select Componente.id, Componente.nome, Evento.datatermino from Evento, Contrato, Componente 
    where Evento.id = Contrato.idEvento and Contrato.idcomponente = Componente.id and upper(Componente.alugado) = 'SIM'and Componente.Anunciante = '23046021872';

--
-- 10.  Selecionar componentes que estão cadastrados no sistemas mas foram contratados para algum evento e 
--      possuem anunciante com mais de 1 componente comprado por mais de 1 contratante diferente
--
-- OBS: Essa é a query de divisão: estamos dividindo a tabela de componentes pela de contrato

SELECT DISTINCT ID, ANUNCIANTE, NOME, PRECO, ALUGADO from componente
WHERE componente.id in 
    (
        SELECT distinct contrato.idcomponente from contrato 
        inner join componente on componente.id = contrato.idcomponente 
        inner join anunciante on cpf = componente.anunciante
        WHERE componente.anunciante in 
        (
            SELECT distinct Componente.anunciante from CONTRATO
            INNER JOIN Componente on contrato.idcomponente = componente.id 
            GROUP BY componente.anunciante
            HAVING Count(distinct Contrato.Idcomponente) > 1 AND Count(distinct Contrato.contratante) > 1            
        )
    )
ORDER BY componente.id;