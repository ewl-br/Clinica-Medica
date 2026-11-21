CREATE TABLE pacientes (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	cpf CHAR(11) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	telefone VARCHAR(20) NOT NULL
);

INSERT INTO pacientes
(nome, cpf, data_nascimento, telefone)
VALUES
('Maria Silva', '12345678901', '1995-05-20', '81999999999')

SELECT * FROM pacientes
WHERE cpf = '12345678901';

UPDATE pacientes
SET nome = 'Maria de Oliveira'
WHERE cpf = '12345678901';

DELETE FROM pacientes
WHERE cpf = '98765432100'