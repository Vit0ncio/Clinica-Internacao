CREATE DATABASE estoque_almoxarifado;

USE estoque_almoxarifado;

CREATE TABLE IF NOT EXISTS funcionarios (
    id_funcionario INT PRIMARY KEY,
    nome_funcionario VARCHAR(100) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    pode_autorizar BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INT PRIMARY KEY,
    setor VARCHAR(50),
    id_solicitante INT NOT NULL,
    id_autorizador INT,

    CONSTRAINT fk_pedido_solicitante FOREIGN KEY (id_solicitante) REFERENCES funcionarios(id_funcionario),
    CONSTRAINT fk_pedido_autorizador FOREIGN KEY (id_autorizador) REFERENCES funcionarios(id_funcionario)
);

CREATE TABLE IF NOT EXISTS produtos (
    id_produto INT PRIMARY KEY,
    qtd_produto INT,
    nome_produto VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos_produtos (
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    qtd_solicitada INT NOT NULL,
    PRIMARY KEY (id_pedido, id_produto),
    CONSTRAINT fk_pp_pedido FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    CONSTRAINT fk_pp_produto FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- Inserção de dados

INSERT INTO funcionarios VALUES
(1, "João", "Encarregado", true),
(2, "Maria", "Funcionária do almoxarifado", false),
(3, "Carlos", "Cirurgião", false),
(4, "José", "Líder do setor 1", true),
(5, "Fernanda", "Enfermeira", false);

INSERT INTO produtos VALUES
(1, 23, "Seringa 100ui"),
(2, 12, "Band-aid (Caixa de 100 unidades)"),
(3, 3, "Soro Fisiológico (500ml)"),
(4, 48, "Luva de látex"),
(5, 6, "Máscara descartável");

INSERT INTO pedidos VALUES
(1, "Pronto-Socorro", 3, 1),
(2, "Sala 12", 5, 4),
(3, "Administração", 2, 1),
(4, "Sala de Radiologia", 5, 4),
(5, "Sala 15", 3, 1);

INSERT INTO pedidos_produtos VALUES
(1, 2, 10),
(2, 3, 1),
(3, 1, 5),
(4, 4, 18),
(5, 5, 2);

-- Consulta de dados
SELECT * FROM funcionarios;
SELECT * FROM produtos WHERE qtd_produto < 10;
SELECT * FROM pedidos_produtos ORDER BY qtd_solicitada;
SELECT MAX(qtd_produto) FROM produtos;
SELECT produtos.nome_produto, pedidos.id_pedido FROM pedidos_produtos INNER JOIN pedidos ON pedidos_produtos.id_pedido = pedidos.id_pedido INNER JOIN produtos ON pedidos_produtos.id_produto = produtos.id_produto;
SELECT produtos.nome_produto, pedidos.id_pedido FROM pedidos_produtos INNER JOIN pedidos ON pedidos_produtos.id_pedido = pedidos.id_pedido INNER JOIN produtos ON pedidos_produtos.id_produto = produtos.id_produto;
