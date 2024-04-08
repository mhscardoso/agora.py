CREATE TABLE IF NOT EXISTS entity (
	"id"          SERIAL PRIMARY KEY,
	"name"        VARCHAR(255) UNIQUE,
	"description" VARCHAR(255),
	"image_url"   VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS edges (
	"from" 			INTEGER REFERENCES entity(id),
	"to"   			INTEGER REFERENCES entity(id),
	"description"   VARCHAR(255),
	PRIMARY KEY ("from", "to")
);


-- Inserindo dados iniciais
------------------------------------------- Entities --------------------------------------------------
INSERT INTO entity ("name", "description") 
	VALUES ('Jean Paul Prates', 'Presidente da Petrobras');                                        -- 1

INSERT INTO entity ("name", "description") 
	VALUES ('Luiz Inácio Lula da Silva', 'Presidente do Brasil (23-27)');                          -- 2

INSERT INTO entity ("name", "description") 
	VALUES ('Alexandre Silveira', 'Ministro de Minas e Energia');                                  -- 3

INSERT INTO entity ("name", "description") 
	VALUES ('Fátima Bezerra', 'Governadora do Rio Grande do Norte');                               -- 4

INSERT INTO entity ("name", "description") 
	VALUES ('Clarice Coppetti', 'Diretora de Rel. Inst. e Sust. Petrobras');                       -- 5

INSERT INTO entity ("name", "description") 
	VALUES ('Sergio Caetano Leite', 'Diretor Financeiro e de Rel. com Investidores da Petrobras'); -- 6

INSERT INTO entity ("name", "description") 
	VALUES ('William França Silva', 'Diretor de Refino e Gás Natural da Petrobras');               -- 7
-------------------------------------------------------------------------------------------------------


--------------------------------------------- Edges ---------------------------------------------------
----------- Jean comum a todos ---------
INSERT INTO edges ("from", "to")
	VALUES (1, 2);

INSERT INTO edges ("from", "to")
	VALUES (1, 3);

INSERT INTO edges ("from", "to")
	VALUES (1, 4);

INSERT INTO edges ("from", "to")
	VALUES (1, 5);

INSERT INTO edges ("from", "to")
	VALUES (1, 6);

INSERT INTO edges ("from", "to")
	VALUES (1, 7);
----------------------------------------


---- Rel. de Lula com Fátima Bezerra e Alexandre Silveira --
INSERT INTO edges ("from", "to")
	VALUES (2, 3);

INSERT INTO edges ("from", "to")
	VALUES (2, 4);
------------------------------------------------------------


---- Rel. de Alexandre Silveira com os Diretores -----------
INSERT INTO edges ("from", "to")
	VALUES (3, 5);

INSERT INTO edges ("from", "to")
	VALUES (3, 6);

INSERT INTO edges ("from", "to")
	VALUES (3, 7);
-------------------------------------------------------------------------------------------------------
