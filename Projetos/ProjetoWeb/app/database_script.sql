CREATE DATABASE pmvshopDB;
USE pmvshopDB;

DROP TABLE discos;
DROP TABLE users; -- Reseta a tabela aki


CREATE TABLE IF NOT EXISTS discos (
id_disco INT AUTO_INCREMENT  NOT NULL,
nome_album VARCHAR(60) NOT NULL,
ano_lancamento YEAR NOT NULL,
artista VARCHAR(50) NOT NULL,
genero VARCHAR(50) NOT NULL,
PRIMARY KEY (id_disco)
);


-- NÃO FAZER INSERT MANUAL NESTA TABELA
-- não vai funcionar pq a senha tá com hash
CREATE TABLE IF NOT EXISTS users (
    usersName VARCHAR(128) NOT NULL,
	usersId VARCHAR(11) NOT NULL, -- CPF 
    usersEmail VARCHAR(128) NOT NULL,
    usersPwd VARCHAR(128) NOT NULL,
    PRIMARY KEY (usersId)
);

INSERT INTO discos(nome_album,ano_lancamento,artista,genero) VALUES 
("Metallica","1992","Metallica","Heavy Metal"),
("Back in Black","1980","AC/DC","Heavy Metal"),
("Wiped Out!","2015","The Neighbourhood","Alternative "),
("Hard To Imagine The Neighbourhood Ever Changing","2018","The Neighbourhood","Alternative"),
("My Head Is An Animal","2012","Of Monsters and Men","Indie"),
("CASTLE","2022","Dios","Alternative"),
("BIPOLAR","2022","Tatsuya Kitani","Rock"),
("DEMAGOG","2020","Tatsuya Kitani","Rock"),
("Bunka","2017","Eve","Rock"),
("MOVE - The 2nd Album","2017","Taemin","R&B"),
("Songs From The Big Chair","1985","Tears For Fears","Rock"),
("All the Right Reasons","2005","Nickelback","Rock"),
("Brothers in Arms","1985","Dire Straits","Rock"),
("Out Of Time","1991","R.E.M","Rock"),
("Slippery When Wet","1986","Bon Jovi","Heavy Metal"),
("Optimist","2021","FINNEAS","Alternative"),
("Currents","2015","Tame Impala","Alternative"),
("Melophobia","2013","Cage The Elephant","Alternative"),
("The Movie Star","2019","BewhY","Hip-Hop/rap"),
("Don't Forget About me, Demos","2018","Dominic Fike","Alternative"),
("Blurry Face","2015","21 pilots","Indie pop"),
("Favorite Worst Nightmare","2007","Artic Monkeys","Alternative"),
("Abbey Road","1969","The Beatles","Rock"),
("The Works","1984","Queen","Rock"),
("<COPINGMECHANISM>","2022","WILLOW","Rock");

SELECT * FROM discos;
SELECT * FROM users;
