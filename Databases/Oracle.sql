-- -----------------------------------------------------
--
--  FILE WITH QUERIES TO CREATE THE DATABASE
--
--  OBSERVATIONS:
--
--      - At the creation of each table, we try to drop 
--        a possible existent table;
--
--      - We only comment the first occurrence of 
--        something: e.g, the first occurrence of a
--        constraint to create an unique index.
--
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema H10819029
-- Selecting the schema we are going to use
-- -----------------------------------------------------
ALTER SESSION SET current_schema = H10819029;

-- -----------------------------------------------------
-- Table `Contratante`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Contratante';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Contratante (
  CPF VARCHAR2(11) NOT NULL,
  Avaliacao BINARY_FLOAT DEFAULT 0 NULL,
  Nome VARCHAR2(45) NOT NULL,
  Email VARCHAR2(45) NOT NULL,
  Senha VARCHAR2(45) NOT NULL,
  PRIMARY KEY (CPF),
  -- constraint to turn 'email' into unique, i.e., can't have two 'email's with the same value on this table
  CONSTRAINT EmailContratante_UNIQUE UNIQUE  (Email))
;


-- -----------------------------------------------------
-- Table `Evento`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Evento';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Evento (
  ID INTEGER NOT NULL,
  Contratante VARCHAR2(45) NOT NULL,
  Tipo VARCHAR2(45) NULL,
  Preco BINARY_FLOAT NOT NULL,
  DataInicio DATE NOT NULL,
  DataTermino DATE NOT NULL,
  Nome VARCHAR2(45) NOT NULL,
  CONSTRAINT PK_Evento PRIMARY KEY (ID, Contratante)
 ,
  -- Constraint to create a Foreign Key to CPF on table CPF referecing Contratante on this table.
  -- We are cascading (deleting) data after a drop to ensure we'll not have old and inaccurate data.
  CONSTRAINT FKEvento_Contratante
    FOREIGN KEY (Contratante)
    REFERENCES Contratante (CPF)
    ON DELETE CASCADE
   )
;

-- Generate ID using sequence and trigger
CREATE SEQUENCE Evento_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER Evento_seq_tr
 BEFORE INSERT ON Evento FOR EACH ROW
 WHEN (NEW.ID IS NULL)
BEGIN
 SELECT Evento_seq.NEXTVAL INTO :NEW.ID FROM DUAL;
END;
/

CREATE INDEX FKEvento_Contratante_idx ON Evento (Contratante ASC);


-- -----------------------------------------------------
-- Table `Anunciante`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Anunciante';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Anunciante (
  CPF VARCHAR2(11) NOT NULL,
  Avaliacao BINARY_FLOAT DEFAULT 0 NULL,
  Nome VARCHAR2(45) NOT NULL,
  Email VARCHAR2(45) NOT NULL,
  Senha VARCHAR2(45) NOT NULL,
  PRIMARY KEY (CPF),
  CONSTRAINT EmailAnunciante_UNIQUE UNIQUE  (Email))
;


-- -----------------------------------------------------
-- Table `Componente`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Componente';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Componente (
  Anunciante VARCHAR2(45) NOT NULL,
  ID INTEGER NOT NULL,
  Nome VARCHAR2(45) NOT NULL,
  Preco BINARY_FLOAT NOT NULL,
  Alugado VARCHAR2(4) NOT NULL,
  PRIMARY KEY (ID)
 ,
 -- Constraint to check if value of 'Alugado' is either 'SIM' or 'NAO' and nothing else.
 CONSTRAINT Check_alugado
    CHECK (UPPER(Alugado) IN ('SIM', 'NAO'))
 ,
 -- Constraint to check if value of 'Nome' is either 'PRODUTO', 'SERVICOS' or 'LOCAL' and nothing else.
 -- This one was done to ensure our disjunction of 'Componente'.
  CONSTRAINT Check_Nome
    CHECK (UPPER(Nome) IN ('PRODUTO', 'SERVICOS', 'LOCAL'))
 ,
  CONSTRAINT FKComponente_Anunciante
    FOREIGN KEY (Anunciante)
    REFERENCES Anunciante (CPF)
    ON DELETE CASCADE
   )
;

-- Generate ID using sequence and trigger
CREATE SEQUENCE Componente_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER Componente_seq_tr
 BEFORE INSERT ON Componente FOR EACH ROW
 WHEN (NEW.ID IS NULL)
BEGIN
 SELECT Componente_seq.NEXTVAL INTO :NEW.ID FROM DUAL;
END;
/

CREATE INDEX FKComponente_Anunciante_idx ON Componente (Anunciante ASC);

-- -----------------------------------------------------
-- Table `Produto`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Produto';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Produto (
  IDComponente INTEGER NOT NULL,
  Categoria VARCHAR2(45) NOT NULL,
  Quantidade INTEGER NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKProduto_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Componente (ID)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Contrato`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Contrato';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Contrato (
  Numero INTEGER NOT NULL,
  IDEvento INTEGER NOT NULL,
  Contratante VARCHAR2(45) NOT NULL,
  IDComponente INTEGER NOT NULL,
  PRIMARY KEY (Numero),
  -- Constraint to create a composite key of IDEvento, Contratante and IDComponente
  CONSTRAINT COMPOSITE_UNIQUE UNIQUE (IDEvento, Contratante, IDComponente),
  CONSTRAINT FKContrato_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Componente (ID)
    ON DELETE CASCADE
  ,
  CONSTRAINT FK_IDS
    FOREIGN KEY (IDEvento, Contratante)
    REFERENCES Evento (ID, Contratante)
    ON DELETE CASCADE)
;

-- Trigger that updates 'Preco' on table Evento
--
-- We created a trigger to update "Preco" on table Evento every time a new "Componente" is added to
-- "Contrato", i.e., its "bought" or "rent" buy a "Contratante".

CREATE OR REPLACE TRIGGER updatePrecoEvento
  AFTER INSERT ON Contrato
  FOR EACH ROW
DECLARE
    oldEventoPreco BINARY_FLOAT; -- var to store current "preco" of Evento
    newPreco BINARY_FLOAT;       -- var to store "preco" of new Componente
BEGIN

    -- Gets current "Preco" from Evento
    SELECT preco
      INTO oldEventoPreco 
      FROM Evento 
    WHERE Evento.id = :new.IDEvento;
    
    -- Gets "Preco" of Componente
    SELECT preco
      INTO newPreco
      FROM Componente
    WHERE Componente.id = :new.Idcomponente;
    
    -- Updates "Preco" of Evento
    UPDATE Evento
      SET Evento.Preco = oldEventoPreco + newPreco
    WHERE Evento.id = :new.IDEvento;
    
END;
/

-- Generate ID using sequence and trigger
CREATE SEQUENCE Contrato_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER Contrato_seq_tr
 BEFORE INSERT ON Contrato FOR EACH ROW
 WHEN (NEW.Numero IS NULL)
BEGIN
 SELECT Contrato_seq.NEXTVAL INTO :NEW.Numero FROM DUAL;
END;
/

CREATE INDEX FKContrato_Contratante_idx ON Contrato (Contratante ASC);


-- -----------------------------------------------------
-- Table `TermoDeCompromisso`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE TermoDeCompromisso';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE TermoDeCompromisso (
  Numero INTEGER NOT NULL,
  IDEvento INTEGER NOT NULL,
  Contratante VARCHAR2(45) NOT NULL,
  IDComponente INTEGER NOT NULL,
  PRIMARY KEY (Numero),
  CONSTRAINT COMPOSITETDC UNIQUE (IDEvento, Contratante, IDComponente),
  
  -- This one is beautiful: we've created a constraint to reference the composite key created above on Contrato
  CONSTRAINT FKCOMPOSITETDC
    FOREIGN KEY (IDEvento, Contratante, IDComponente)
    REFERENCES Contrato (IDEvento, Contratante, IDComponente)
    ON DELETE CASCADE
  ,
  CONSTRAINT FKTDC_Contratante
    FOREIGN KEY (Contratante)
    REFERENCES Contratante (CPF)
    ON DELETE CASCADE
   )
;

-- Generate ID using sequence and trigger
CREATE SEQUENCE TermoDeCompromisso_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER TermoDeCompromisso_seq_tr
 BEFORE INSERT ON TermoDeCompromisso FOR EACH ROW
 WHEN (NEW.Numero IS NULL)
BEGIN
 SELECT TermoDeCompromisso_seq.NEXTVAL INTO :NEW.Numero FROM DUAL;
END;
/

CREATE INDEX FKTDC_Contratante_idx ON TermoDeCompromisso (Contratante ASC);


-- -----------------------------------------------------
-- Table `Avalia`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Avalia';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Avalia (
  ID INTEGER NOT NULL,
  Anunciante VARCHAR2(45) NOT NULL,
  Contratante VARCHAR2(45) NOT NULL,
  Nota BINARY_FLOAT NOT NULL,
  Comentario VARCHAR2(45) NULL,
  Avaliador VARCHAR2(11) NOT NULL,
  PRIMARY KEY (ID)
 ,
 CONSTRAINT check_Avaliador
  CHECK (UPPER(Avaliador) IN ('ANUNCIANTE', 'CONTRATANTE'))
 ,
  CONSTRAINT FKAvalia_Anunciante
    FOREIGN KEY (Anunciante)
    REFERENCES Anunciante (CPF)
    ON DELETE CASCADE
   ,
  CONSTRAINT FKAvalia_Contratante
    FOREIGN KEY (Contratante)
    REFERENCES Contratante (CPF)
    ON DELETE CASCADE
   )
;

-- Generate ID using sequence and trigger
CREATE SEQUENCE Avalia_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER Avalia_seq_tr
 BEFORE INSERT ON Avalia FOR EACH ROW
 WHEN (NEW.ID IS NULL)
BEGIN
 SELECT Avalia_seq.NEXTVAL INTO :NEW.ID FROM DUAL;
END;
/

CREATE INDEX FKAvalia_Anunciante_idx ON Avalia (Anunciante ASC);
CREATE INDEX FKAvalia_Contratante_idx ON Avalia (Contratante ASC);


-- Trigger that updates 'Avaliacao' on table Anunciante
-- We created a trigger to update "Avaliacao" of "Anunciante" every time a new row is inserted on "Avalia" with "Avaliador" = CONTRATANTE
create or replace TRIGGER updateAnuncAval
  AFTER INSERT OR UPDATE OR DELETE ON Avalia
  FOR EACH ROW
  WHEN (UPPER(new.Avaliador) = 'CONTRATANTE')
DECLARE
    -- As we are leading with attributes from the table we are inserting a row (avalia), we needed to use this pragma
    -- to allow us to do the jobs below. After each select, we needed to commit before continuing
    PRAGMA AUTONOMOUS_TRANSACTION;
    oldAnuncNota BINARY_FLOAT; -- var to store current (old) Avaliacao of Anunciante
    newAnuncNota BINARY_FLOAT; -- var to store new Avaliacao of Anunciante
    tableRows INTEGER; -- var to check if there is at least one row to use this trigger to avoid errors

BEGIN

    select count(*) into tableRows from Avalia;
    commit;

    IF tableRows > 0 then

      -- Selecting and saving current Avaliacao into oldAnuncNota
      SELECT avaliacao
        into oldAnuncNota
      FROM Anunciante
      WHERE cpf = :new.Anunciante;
      commit;

      -- Updating Avaliacao which is the mean value between the old Avaliacao value + the new one
      newAnuncNota := (oldAnuncNota + :new.Nota)/2;

      -- Saving new Avaliacao of Anunciante into his row on table Anunciante
      UPDATE Anunciante
      SET Avaliacao = newAnuncNota
      WHERE cpf = :new.Anunciante;
      commit;
    END IF;

END;

/

-- Trigger that updates 'Avaliacao' on table Contratante
-- We created a trigger to update "Avaliacao" of "Contratante" every time a new row is inserted on "Avalia" with "Avaliador" = ANUNCIANTE
create or replace TRIGGER updateContrAval
  AFTER INSERT OR UPDATE OR DELETE ON Avalia
  FOR EACH ROW
  WHEN (UPPER(new.Avaliador) = 'ANUNCIANTE')
DECLARE
    -- As we are leading with attributes from the table we are inserting a row (avalia), we needed to use this pragma
    -- to allow us to do the jobs below. After each select, we needed to commit before continuing
    PRAGMA AUTONOMOUS_TRANSACTION; 
    oldContrNota BINARY_FLOAT; -- var to store current 'nota' 
    newContrNota BINARY_FLOAT; -- var to store new 'nota'
    tableRows INTEGER; -- var to check if there is at least one row to use this trigger to avoid errors
BEGIN

    select count(*) into tableRows from Avalia;
    commit;
    
    IF tableRows > 0 then

      SELECT avaliacao
        into oldContrNota
      FROM Contratante
      WHERE cpf = :new.Contratante;
      commit;

      newContrNota := (oldContrNota + :new.Nota)/2;

      UPDATE Contratante
      SET Avaliacao = newContrNota
      WHERE cpf = :new.Contratante;
      commit;
    END IF;

END;
/


-- -----------------------------------------------------
-- Table `Montador`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Montador';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Montador (
  CPF VARCHAR2(11) NOT NULL,
  Nome VARCHAR2(45) NOT NULL,
  Email VARCHAR2(45) NOT NULL,
  PRIMARY KEY (CPF),
  CONSTRAINT EmailMontador_UNIQUE UNIQUE  (Email))
;


-- -----------------------------------------------------
-- Table `Cadastra`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Cadastra';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Cadastra (
  Anunciante VARCHAR2(45) NOT NULL,
  Montador VARCHAR2(45) NOT NULL,
  PRIMARY KEY (Anunciante, Montador),
  CONSTRAINT FKCadastra_Anunciante
    FOREIGN KEY (Anunciante)
    REFERENCES Anunciante (CPF)
    ON DELETE CASCADE
   ,
  CONSTRAINT FKCadastra_Montador
    FOREIGN KEY (Montador)
    REFERENCES Montador (CPF)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `TelefonesAnunciante`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE TelefonesAnunciante';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE TelefonesAnunciante (
  Telefone VARCHAR2(13) NOT NULL,
  CPF VARCHAR2(11) NOT NULL,
  PRIMARY KEY (Telefone, CPF),
  CONSTRAINT FKTelefonesA_CPF
    FOREIGN KEY (CPF)
    REFERENCES Anunciante (CPF)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `TelefonesContratante`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE TelefonesContratante';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE TelefonesContratante (
  Telefone VARCHAR2(13) NOT NULL,
  CPF VARCHAR2(11) NOT NULL,
  PRIMARY KEY (Telefone, CPF),
  CONSTRAINT FKTelefonesC_CPF
    FOREIGN KEY (CPF)
    REFERENCES Contratante (CPF)
    ON DELETE CASCADE
  )
;


-- -----------------------------------------------------
-- Table `TelefonesMontador`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE TelefonesMontador';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE TelefonesMontador (
  Telefone VARCHAR2(13) NOT NULL,
  CPF VARCHAR2(11) NOT NULL,
  PRIMARY KEY (Telefone, CPF),
  CONSTRAINT FKTelefonesM_CPF
    FOREIGN KEY (CPF)
    REFERENCES Montador (CPF)
    ON DELETE CASCADE
  )
;


-- -----------------------------------------------------
-- Table `Infraestrutura`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Infraestrutura';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Infraestrutura (
  IDComponente INTEGER NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKInfraestrutura_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Produto (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Necessita`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Necessita';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Necessita (
  Montador VARCHAR2(45) NOT NULL,
  Infraestrutura INTEGER NOT NULL,
  PRIMARY KEY (Montador, Infraestrutura)
 ,
  CONSTRAINT FKNecessita_Infraestrutura
    FOREIGN KEY (Infraestrutura)
    REFERENCES Infraestrutura (IDComponente)
    ON DELETE CASCADE
   ,
  CONSTRAINT FKNecessita_Montador
    FOREIGN KEY (Montador)
    REFERENCES Montador (CPF)
    ON DELETE CASCADE
   )
;

CREATE INDEX FK_Infraestrutura_idx ON Necessita (Infraestrutura ASC);


-- -----------------------------------------------------
-- Table `Ruas`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Ruas';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Ruas (
  CEP VARCHAR2(9) NOT NULL,
  Rua VARCHAR2(45) NOT NULL,
  Bairro VARCHAR2(45) NOT NULL,
  PRIMARY KEY (CEP),
  CONSTRAINT Rua_UNIQUE UNIQUE  (Rua)
  )
;


-- -----------------------------------------------------
-- Table `Local`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Local';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Local (
  IDComponente INTEGER NOT NULL,
  Capacidade INTEGER NULL,
  Metragem BINARY_FLOAT NULL,
  Numero INTEGER NOT NULL,
  CEP VARCHAR2(9) NOT NULL,
  TensaoEletrica INTEGER NULL,
  Quantidade_Quartos INTEGER NOT NULL,
  Quantidade_Banheiros INTEGER NOT NULL,
  Garagem VARCHAR2(4) NULL,
  PRIMARY KEY (IDComponente)
 ,
 CONSTRAINT check_Garagem
  CHECK (UPPER(Garagem) IN ('SIM', 'NAO'))
  ,
  CONSTRAINT CEPLocal_UNIQUE UNIQUE  (CEP),
  CONSTRAINT NumeroLocal_UNIQUE UNIQUE  (Numero),
  CONSTRAINT FKLocal_CEP
    FOREIGN KEY (CEP)
    REFERENCES Ruas (CEP)
    ON DELETE CASCADE
   ,
  CONSTRAINT FKLocal_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Componente (ID)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `AvaisDeSeguranca`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE AvaisDeSeguranca';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE AvaisDeSeguranca (
  NumeroAval INTEGER NOT NULL,
  Numero INTEGER NOT NULL,
  CEP VARCHAR2(9) NOT NULL,
  PRIMARY KEY (NumeroAval),
  CONSTRAINT NumeroADS_UNIQUE UNIQUE  (Numero),
  CONSTRAINT CEPADS_UNIQUE UNIQUE  (CEP),
  CONSTRAINT FKAvaisDeSeguranca_CEP
    FOREIGN KEY (CEP)
    REFERENCES Ruas (CEP)
    ON DELETE CASCADE
   ,
  CONSTRAINT FKAvaisDeSeguranca_Numero
    FOREIGN KEY (Numero)
    REFERENCES Local (Numero)
    ON DELETE CASCADE
   )
;

-- Generate ID using sequence and trigger
CREATE SEQUENCE AvaisDeSeguranca_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER AvaisDeSeguranca_seq_tr
 BEFORE INSERT ON AvaisDeSeguranca FOR EACH ROW
 WHEN (NEW.NumeroAval IS NULL)
BEGIN
 SELECT AvaisDeSeguranca_seq.NEXTVAL INTO :NEW.NumeroAval FROM DUAL;
END;
/


-- -----------------------------------------------------
-- Table `areasComuns`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE areasComuns';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE areasComuns (
  IDComponente INTEGER NOT NULL,
  area VARCHAR2(45) NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKareasComuns_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Local (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Fotos`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Fotos';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Fotos (
  IDComponente INTEGER NOT NULL,
  Foto BLOB NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKFotos_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Local (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Servicos`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Servicos';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Servicos (
  IDComponente INTEGER NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKServicos_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Componente (ID)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Transporta`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Transporta';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Transporta (
  IDComponente INTEGER NOT NULL,
  Placa VARCHAR2(8) NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT Placa_UNIQUE UNIQUE  (Placa),
  CONSTRAINT FKTransporta_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Produto (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Iluminacao`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Iluminacao';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Iluminacao (
  IDComponente INTEGER NOT NULL,
  Potencia INTEGER NULL,
  TensaoEletrica INTEGER NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKIluminacao_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Produto (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Decoracao`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Decoracao';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Decoracao (
  IDComponente INTEGER NOT NULL,
  TipoDeDecoracao VARCHAR2(45) NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKDecoracao_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Produto (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Entretenimento`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Entretenimento';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Entretenimento (
  IDComponente INTEGER NOT NULL,
  Categoria VARCHAR2(45) NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKEntretenimento_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Servicos (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Alimentacao`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Alimentacao';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Alimentacao (
  IDComponente INTEGER NOT NULL,
  Tipo VARCHAR2(45) NULL,
  Quantidade INTEGER NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKAlimentacao_IDComponentes
    FOREIGN KEY (IDComponente)
    REFERENCES Servicos (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Seguranca`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Seguranca';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Seguranca (
  IDComponente INTEGER NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT FKSeguranca_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Servicos (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `Turnos`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Turnos';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Turnos (
  IDComponente INTEGER NOT NULL,
  Turno VARCHAR2(45) NOT NULL,
  PRIMARY KEY (IDComponente, Turno),
  CONSTRAINT check_Turno
    CHECK (UPPER(Turno) IN ('MATUTINO', 'VESPERTINO', 'NOTURNO', 'DIURNO'))
  ,
  CONSTRAINT FKTurnos_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Seguranca (IDComponente)
    ON DELETE CASCADE
   )
;


-- -----------------------------------------------------
-- Table `TipoDeTransporte`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE TipoDeTransporte';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE TipoDeTransporte (
  TipoDeTransporte VARCHAR2(45) NOT NULL,
  Capacidade INTEGER NOT NULL,
  PRIMARY KEY (TipoDeTransporte))
;


-- -----------------------------------------------------
-- Table `Transporte`
-- -----------------------------------------------------
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE Transporte';
EXCEPTION
   WHEN OTHERS THEN NULL;
END;
/ 

CREATE TABLE Transporte (
  IDComponente INTEGER NOT NULL,
  Tipo VARCHAR2(45) NOT NULL,
  Quantidade INTEGER NULL,
  CNH VARCHAR2(11) NOT NULL,
  PRIMARY KEY (IDComponente),
  CONSTRAINT CNHTransporte_UNIQUE UNIQUE  (CNH)
 ,
  CONSTRAINT FKTransporte_Tipo
    FOREIGN KEY (Tipo)
    REFERENCES TipoDeTransporte (TipoDeTransporte)
    ON DELETE CASCADE
   ,
  CONSTRAINT FKTransporte_IDComponente
    FOREIGN KEY (IDComponente)
    REFERENCES Servicos (IDComponente)
    ON DELETE CASCADE
   )
;

CREATE INDEX FKTransporte_Tipo_idx ON Transporte (Tipo ASC);