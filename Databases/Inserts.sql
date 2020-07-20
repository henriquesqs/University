-- -----------------------------------------------------
-- Inserting into Table `CONTRATANTE`
-- -----------------------------------------------------
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021853',5,'Joao0','Joao0@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021854',0.0,'Joao1','Joao1@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021855',2.2,'Joao2','Joao2@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021856',0.0,'Joao3','Joao3@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021857',0.0,'Joao4','Joao4@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021858',0.0,'Joao5','Joao5@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021859',6.6,'Joao6','Joao6@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021860',0.0,'Joao7','Joao7@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021861',5.3,'Joao8','Joao8@dominio.com','123456');
Insert into CONTRATANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021862',9.9,'Joao9','Joao9@dominio.com','123456');

-- -----------------------------------------------------
-- Inserting into Table `ANUNCIANTE`
-- -----------------------------------------------------
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021863',0.0,'Maria0','Maria0@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021864',1.1,'Maria1','Maria1@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021865',4.7,'Maria2','Maria2@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021866',3.3,'Maria3','Maria3@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021867',4.4,'Maria4','Maria4@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021868',5.5,'Maria5','Maria5@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021869',0.0,'Maria6','Maria6@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021870',7.7,'Maria7','Maria7@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021871',8.8,'Maria8','Maria8@dominio.com','123456');
Insert into ANUNCIANTE (CPF,AVALIACAO,NOME,EMAIL,SENHA) values ('23046021872',0.0,'Maria9','Maria9@dominio.com','123456');

-- -----------------------------------------------------
-- Inserting into Table `MONTADOR`
-- -----------------------------------------------------
Insert into MONTADOR (CPF,NOME,EMAIL) values ('23046021873','Rodosclaudio0','Rodosclaudio0@dominio.com');
Insert into MONTADOR (CPF,NOME,EMAIL) values ('23046021874','Rodosclaudio1','Rodosclaudio1@dominio.com');
Insert into MONTADOR (CPF,NOME,EMAIL) values ('23046021875','Rodosclaudio2','Rodosclaudio2@dominio.com');

-- -----------------------------------------------------
-- Inserting into Table `EVENTO`
-- -----------------------------------------------------
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (0,'23046021853',null,0,to_date('01/02/20','DD/MM/YYYY'),to_date('02/02/20','DD/MM/YYYY'),'Paredao0');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (1,'23046021854',null,0,to_date('02/03/20','DD/MM/YYYY'),to_date('03/03/20','DD/MM/YYYY'),'Paredao1');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (2,'23046021855',null,0,to_date('03/04/20','DD/MM/YYYY'),to_date('04/04/20','DD/MM/YYYY'),'Paredao2');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (3,'23046021856',null,0,to_date('04/05/20','DD/MM/YYYY'),to_date('05/05/20','DD/MM/YYYY'),'Paredao3');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (4,'23046021857',null,0,to_date('05/06/20','DD/MM/YYYY'),to_date('06/06/20','DD/MM/YYYY'),'Paredao4');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (5,'23046021858',null,0,to_date('06/07/20','DD/MM/YYYY'),to_date('01/08/20','DD/MM/YYYY'),'Paredao5');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (6,'23046021859',null,0,to_date('01/07/20','DD/MM/YYYY'),to_date('02/09/20','DD/MM/YYYY'),'Paredao6');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (7,'23046021860',null,0,to_date('02/09/20','DD/MM/YYYY'),to_date('03/10/20','DD/MM/YYYY'),'Paredao7');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (8,'23046021861',null,0,to_date('03/10/20','DD/MM/YYYY'),to_date('04/11/20','DD/MM/YYYY'),'Paredao8');
Insert into EVENTO (ID,CONTRATANTE,TIPO,PRECO,DATAINICIO,DATATERMINO,NOME) values (9,'23046021862',null,0,to_date('05/05/20','DD/MM/YYYY'),to_date('11/11/20','DD/MM/YYYY'),'Paredao9');

-- -----------------------------------------------------
-- Inserting into Table `COMPONENTE`
-- -----------------------------------------------------
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021863',0,'Produto',50,'NAO');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021864',1,'Servicos',100,'NAO');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021865',2,'Produto',150,'NAO');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021866',3,'Produto',200,'NAO');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021867',4,'Produto',250,'NAO');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021868',5,'Servicos',300,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021869',6,'Produto',350,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021870',7,'Local',400,'NAO');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021871',8,'Local',450,'NAO');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021872',9,'Local',500,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021872',10,'Produto',20,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021863',11,'Produto',10,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021864',12,'Produto',15,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021872',13,'Servicos',35,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021868',14,'Servicos',90,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021868',15,'Servicos',25,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021872',16,'Servicos',25,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021870',17,'Servicos',25,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021871',18,'Servicos',25,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021871',19,'Servicos',25,'SIM');
Insert into COMPONENTE (ANUNCIANTE,ID,NOME,PRECO,ALUGADO) values ('23046021866',20,'Produto',50,'NAO');

-- -----------------------------------------------------
-- Inserting into Table `CONTRATO`
-- -----------------------------------------------------
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (0,0,'23046021853',0);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (1,1,'23046021854',1);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (2,2,'23046021855',2);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (3,3,'23046021856',3);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (4,4,'23046021857',4);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (5,5,'23046021858',5);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (6,6,'23046021859',6);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (7,7,'23046021860',7);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (8,8,'23046021861',8);
Insert into CONTRATO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (9,9,'23046021862',9);

-- -----------------------------------------------------
-- Inserting into Table `TERMODECOMPROMISSO`
-- -----------------------------------------------------
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (0,0,'23046021853',0);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (1,1,'23046021854',1);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (2,2,'23046021855',2);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (3,3,'23046021856',3);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (4,4,'23046021857',4);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (5,5,'23046021858',5);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (6,6,'23046021859',6);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (7,7,'23046021860',7);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (8,8,'23046021861',8);
Insert into TERMODECOMPROMISSO (NUMERO,IDEVENTO,CONTRATANTE,IDCOMPONENTE) values (9,9,'23046021862',9);

-- -----------------------------------------------------
-- Inserting into Table `AVALIA`
-- -----------------------------------------------------
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (0,'23046021863','23046021853',5,null,'ANUNCIANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (1,'23046021864','23046021854',1.1,null,'CONTRATANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (2,'23046021865','23046021855',2.2,null,'ANUNCIANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (3,'23046021866','23046021856',3.3,null,'CONTRATANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (4,'23046021867','23046021857',4.4,null,'CONTRATANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (5,'23046021868','23046021858',5.5,null,'CONTRATANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (6,'23046021869','23046021859',6.6,null,'ANUNCIANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (7,'23046021870','23046021860',7.7,null,'CONTRATANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (8,'23046021871','23046021861',8.8,null,'CONTRATANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (9,'23046021872','23046021862',9.9,null,'ANUNCIANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (10,'23046021872','23046021861',5.3,null,'ANUNCIANTE');
Insert into AVALIA (ID,ANUNCIANTE,CONTRATANTE,NOTA,COMENTARIO,AVALIADOR) values (11,'23046021865','23046021853',4.7,null,'CONTRATANTE');

-- -----------------------------------------------------
-- Inserting into Table `CADASTRA`
-- -----------------------------------------------------
Insert into CADASTRA (ANUNCIANTE,MONTADOR) values ('23046021863','23046021873');
Insert into CADASTRA (ANUNCIANTE,MONTADOR) values ('23046021864','23046021874');
Insert into CADASTRA (ANUNCIANTE,MONTADOR) values ('23046021866','23046021875');

-- -----------------------------------------------------
-- Inserting into Table `TELEFONESANUNCIANTE`
-- -----------------------------------------------------
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5670','23046021863');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5671','23046021864');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5672','23046021865');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5673','23046021866');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5674','23046021867');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5675','23046021868');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5676','23046021869');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5677','23046021870');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5678','23046021871');
Insert into TELEFONESANUNCIANTE (TELEFONE,CPF) values ('(00)4321-5679','23046021872');

-- -----------------------------------------------------
-- Inserting into Table `TELEFONESCONTRATANTE`
-- -----------------------------------------------------
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5608','23046021861');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5619','23046021862');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5623','23046021856');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5644','23046021857');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5655','23046021853');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5655','23046021858');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5656','23046021859');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5681','23046021854');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5692','23046021855');
Insert into TELEFONESCONTRATANTE (TELEFONE,CPF) values ('(00)4321-5697','23046021860');

-- -----------------------------------------------------
-- Inserting into Table `TELEFONESMONTADOR`
-- -----------------------------------------------------
Insert into TELEFONESMONTADOR (TELEFONE,CPF) values ('(00)4321-5611','23046021873');
Insert into TELEFONESMONTADOR (TELEFONE,CPF) values ('(00)4321-5666','23046021874');

-- -----------------------------------------------------
-- Inserting into Table `RUAS`
-- -----------------------------------------------------
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-320','Rua caminho 0','Condomino 0');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-321','Rua caminho 1','Condomino 1');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-322','Rua caminho 2','Condomino 2');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-323','Rua caminho 3','Condomino 3');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-324','Rua caminho 4','Condomino 4');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-325','Rua caminho 5','Condomino 5');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-326','Rua caminho 6','Condomino 6');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-327','Rua caminho 7','Condomino 7');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-328','Rua caminho 8','Condomino 8');
Insert into RUAS (CEP,RUA,BAIRRO) values ('12345-329','Rua caminho 9','Condomino 9');

-- -----------------------------------------------------
-- Inserting into Table `LOCAL`
-- -----------------------------------------------------
Insert into LOCAL (IDCOMPONENTE,CAPACIDADE,METRAGEM,NUMERO,CEP,TENSAOELETRICA,QUANTIDADE_QUARTOS,QUANTIDADE_BANHEIROS,GARAGEM) values (7,null,null,71,'12345-327',110,4,2,null);
Insert into LOCAL (IDCOMPONENTE,CAPACIDADE,METRAGEM,NUMERO,CEP,TENSAOELETRICA,QUANTIDADE_QUARTOS,QUANTIDADE_BANHEIROS,GARAGEM) values (8,null,null,81,'12345-328',220,4,2,null);
Insert into LOCAL (IDCOMPONENTE,CAPACIDADE,METRAGEM,NUMERO,CEP,TENSAOELETRICA,QUANTIDADE_QUARTOS,QUANTIDADE_BANHEIROS,GARAGEM) values (9,null,null,91,'12345-329',110,4,2,null);

-- -----------------------------------------------------
-- Inserting into Table `AVAISDESEGURANCA`
-- -----------------------------------------------------
Insert into AVAISDESEGURANCA (NUMEROAVAL,NUMERO,CEP) values (7,71,'12345-327');
Insert into AVAISDESEGURANCA (NUMEROAVAL,NUMERO,CEP) values (8,81,'12345-328');
Insert into AVAISDESEGURANCA (NUMEROAVAL,NUMERO,CEP) values (9,91,'12345-329');

-- -----------------------------------------------------
-- Inserting into Table `AREASCOMUNS`
-- -----------------------------------------------------
Insert into AREASCOMUNS (IDCOMPONENTE,AREA) values (8,'Lavanderia');
Insert into AREASCOMUNS (IDCOMPONENTE,AREA) values (9,'Lavanderia');

-- -----------------------------------------------------
-- Inserting into Table `PRODUTO`
-- -----------------------------------------------------
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (0,'categoria 0',1);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (2,'categoria 1',11);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (3,'categoria 3',31);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (4,'categoria 4',41);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (6,'categoria 6',61);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (10,'categoria 6',61);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (11,'categoria 6',61);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (12,'categoria 6',61);
Insert into PRODUTO (IDCOMPONENTE,CATEGORIA,QUANTIDADE) values (20,'categoria 1',10);

-- -----------------------------------------------------
-- Inserting into Table `INFRAESTRUTURA`
-- -----------------------------------------------------
Insert into INFRAESTRUTURA (IDCOMPONENTE) values (0);
Insert into INFRAESTRUTURA (IDCOMPONENTE) values (2);
Insert into INFRAESTRUTURA (IDCOMPONENTE) values (20);

-- -----------------------------------------------------
-- Inserting into Table `NECESSITA`
-- -----------------------------------------------------
Insert into NECESSITA (MONTADOR,INFRAESTRUTURA) values ('23046021873',0);
Insert into NECESSITA (MONTADOR,INFRAESTRUTURA) values ('23046021874',2);
Insert into NECESSITA (MONTADOR,INFRAESTRUTURA) values ('23046021875',20);

-- -----------------------------------------------------
-- Inserting into Table `SERVICOS`
-- -----------------------------------------------------
Insert into SERVICOS (IDCOMPONENTE) values (1);
Insert into SERVICOS (IDCOMPONENTE) values (5);
Insert into SERVICOS (IDCOMPONENTE) values (13);
Insert into SERVICOS (IDCOMPONENTE) values (14);
Insert into SERVICOS (IDCOMPONENTE) values (15);
Insert into SERVICOS (IDCOMPONENTE) values (16);
Insert into SERVICOS (IDCOMPONENTE) values (17);
Insert into SERVICOS (IDCOMPONENTE) values (18);
Insert into SERVICOS (IDCOMPONENTE) values (19);

-- -----------------------------------------------------
-- Inserting into Table `TRANSPORTA`
-- -----------------------------------------------------
Insert into TRANSPORTA (IDCOMPONENTE,PLACA) values (3,'ABC-1233');
Insert into TRANSPORTA (IDCOMPONENTE,PLACA) values (4,'ABC-1234');

-- -----------------------------------------------------
-- Inserting into Table `ILUMINACAO`
-- -----------------------------------------------------
Insert into ILUMINACAO (IDCOMPONENTE,POTENCIA,TENSAOELETRICA) values (6,310,110);
Insert into ILUMINACAO (IDCOMPONENTE,POTENCIA,TENSAOELETRICA) values (10,4000,110);

-- -----------------------------------------------------
-- Inserting into Table `DECORACAO`
-- -----------------------------------------------------
Insert into DECORACAO (IDCOMPONENTE,TIPODEDECORACAO) values (11,null);
Insert into DECORACAO (IDCOMPONENTE,TIPODEDECORACAO) values (12,null);

-- -----------------------------------------------------
-- Inserting into Table `ENTRETENIMENTO`
-- -----------------------------------------------------
Insert into ENTRETENIMENTO (IDCOMPONENTE,CATEGORIA) values (1,null);
Insert into ENTRETENIMENTO (IDCOMPONENTE,CATEGORIA) values (5,null);

-- -----------------------------------------------------
-- Inserting into Table `ALIMENTACAO`
-- -----------------------------------------------------
Insert into ALIMENTACAO (IDCOMPONENTE,TIPO,QUANTIDADE) values (13,'tipo 0',20);
Insert into ALIMENTACAO (IDCOMPONENTE,TIPO,QUANTIDADE) values (14,'tipo 1',30);

-- -----------------------------------------------------
-- Inserting into Table `SEGURANCA`
-- -----------------------------------------------------
Insert into SEGURANCA (IDCOMPONENTE) values (15);
Insert into SEGURANCA (IDCOMPONENTE) values (16);

-- -----------------------------------------------------
-- Inserting into Table `TURNOS`
-- -----------------------------------------------------
Insert into TURNOS (IDCOMPONENTE,TURNO) values (15,'Noturno');
Insert into TURNOS (IDCOMPONENTE,TURNO) values (16,'Matutino');

-- -----------------------------------------------------
-- Inserting into Table `TIPODETRANSPORTE`
-- -----------------------------------------------------
Insert into TIPODETRANSPORTE (TIPODETRANSPORTE,CAPACIDADE) values ('tipo 0',5);
Insert into TIPODETRANSPORTE (TIPODETRANSPORTE,CAPACIDADE) values ('tipo 1',15);
Insert into TIPODETRANSPORTE (TIPODETRANSPORTE,CAPACIDADE) values ('tipo 2',25);

-- -----------------------------------------------------
-- Inserting into Table `TRANSPORTE`
-- -----------------------------------------------------
Insert into TRANSPORTE (IDCOMPONENTE,TIPO,QUANTIDADE,CNH) values (17,'tipo 0',null,'01234567890');
Insert into TRANSPORTE (IDCOMPONENTE,TIPO,QUANTIDADE,CNH) values (18,'tipo 1',null,'01234567891');
Insert into TRANSPORTE (IDCOMPONENTE,TIPO,QUANTIDADE,CNH) values (19,'tipo 2',null,'01234567892');