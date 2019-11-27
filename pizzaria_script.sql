create database produtos_pizzaria;
use produtos_pizzaria;

#drop database produtos_pizzaria;


create table tbl_usuarios(
	cod_usuario int not null auto_increment,
    login_usuario varchar(15) not null,
    senha_usuario varchar(8) not null,
	nome_usuario varchar(50) not null,
	primary key(cod_usuario)
);

insert into tbl_usuarios (login_usuario, senha_usuario, nome_usuario)values
	("admin", "admin123", "Marcus Primo");
    
select * from tbl_usuarios;


create table tbl_tipos(
	cod_tipo int not null auto_increment,
    nome_tipo varchar(45) not null,
    primary key(cod_tipo)
);

insert into tbl_tipos (nome_tipo) values
	("Pizza Salgada Grande"),
	("Pizza Salgada Pequena"),
    ("Pizza Doce Grande"),
    ("Pizza Doce Pequena"),
    ("Sucos"),
    ("Refrigerantes"),
    ("Bebidas Alcoólicas"),
    ("Salgados"),
    ("Aperitivos");

select * from tbl_tipos;

create table tbl_produtos(
	cod_produto int not null auto_increment,
    nome_produto varchar(45) not null,
    validade_produto date not null,
    gasto_produto decimal(10,2) not null,
    venda_produto decimal(10,2) not null,
    quant_produto int not null,
    fk_usuarios int not null,
    fk_tipos int not null,
    primary key(cod_produto),
    foreign key(fk_usuarios) references tbl_usuarios(cod_usuario),
    foreign key(fk_tipos) references tbl_tipos(cod_tipo)
);

insert into tbl_produtos(nome_produto, validade_produto, gasto_produto, venda_produto, quant_produto, fk_usuarios, fk_tipos) values
	("Pizza Calabresa Grande", (now() + interval 3 day), 10.00, 25.00, 50, 1,1),
	("Coca-Cola", (now() + interval 8 month), 4.00, 7.00, 50, 1,6);
    
select * from tbl_produtos;

select tbl_produtos.nome_produto, tbl_produtos.validade_produto, tbl_tipos.nome_tipo, tbl_usuarios.nome_usuario from tbl_produtos
	join tbl_tipos on tbl_tipos.cod_tipo = tbl_produtos.fk_tipos
    join tbl_usuarios on tbl_usuarios.cod_usuario = tbl_produtos.fk_usuarios;


