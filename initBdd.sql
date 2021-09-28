CREATE TABLE Entreprise(
id int PRIMARY KEY NOT NULL AUTO INCREMENT,
name varchar(50) NOT NULL,
logo varchar(150),
dateCreation Date,
dateLastModif Date,
size int,
ceo int
);

CREATE TABLE Salarie(
id int PRIMARY KEY NOT NULL AUTO INCREMENT,
name varchar(30),
firstName varchar(30),
age int,
mail varchar(30),
function varchar(30),
workgroup varchar(30),
login varchar(15),
passwd varchar(50),
appAdmin boolean,
dateCreation Date,
dateLastModif Date,
id_entreprise int
);

ALTER TABLE Salarie(
ADD FOREIGN KEY(id_entreprise) REFERENCES Entreprise(id);
);