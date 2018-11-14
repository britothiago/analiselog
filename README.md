## ANÁLISE DE LOGS

Este projeto é um exercício realizado para a Udacity do Nanodegree de Desevolvimento Web Fullstack.

Este deverá ser capaz de responder às seguintes questões:

1. Quais são os três artigos mais populares de todos os tempos?

2. Quem são os autores de artigos mais populares de todos os tempos?

3. Em quais dias mais de 1% das requisições resultaram em erros? 

## INSTALAÇÃO

#### Banco de dados
Baixe os dados da tabela
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Você precisará descompactar este arquivo após o download. O arquivo dentro é chamado de newsdata.sql. Coloque este arquivo no diretório vagrant que é compartilhado com a máquina virtual.

#### Virtual Box
VirtualBox é o software que na verdade executa a máquina virtual. Você pode baixá-lo no virtualbox.org. Instale o plataform package para seu sistema operacional. Você não precisa do pacote de extensão ou do SDK. Você não precisa iniciar o VirtualBox após instalá-lo; Vagrant vai fazer isso.

#### Vagrant
Vagrant é o software que configura a VM e permite que você compartilhe arquivos entre seu computador host e o sistema de arquivos da VM. Baixe no vagrantup.com. Instale a versão de seu sistema operacional.

Clone o repositório `https://github.com/udacity/fullstack-nanodegree-vm` e obtenha o diretório contendo os arquivos da VM. Mude para este diretório no seu terminal com cd. Dentro, você encontrará outro diretório chamado vagrant. Altere o diretório para o diretório vagrant:

Clone o repositório com os dados da análise para baixar os arquivos na mesma do vagrant. Sugerimos que você crie uma subpasta. 
`https://github.com/britothiago/analiselog.git`

Dentro desta subpasta, descompacte o arquivo SQL. 

Execute o comando no terminal `vagrant up` para iniciar a maquina virtual e logo após, `vagrant ssh` para conectar.

Navegue até a subpasta e execute `psql -d news -f newsdata.sql`. Isso fará carregar os dados no banco de dados

Para acessar o banco, use o `psql -d news`


## ESTRUTURA

*A estrutura contém apenas três funções:*

#### artigos_populares()
- Contém uma query
- Apresenta em um lista organizada os artigos mais populares no topo

#### autores_populares()
- Contém uma query
- Apresenta em um lista descrecente dos autores mais populares

#### porcentagem()
- Contém uma query
- Contém duas views:

- view erro
`CREATE VIEW erro AS SELECT to_char(time, 'Mon DD, YYYY') as data, count(time) as totalerro FROM log WHERE status LIKE '404%' GROUP BY data ORDER BY data ASC`

- view nerro
`CREATE VIEW nerro AS SELECT to_char(time, 'Mon DD, YYYY') as data, count(time) as totalnerro FROM log GROUP BY data ORDER BY data ASC`

- Apresenta o dia que mais houve erros de respostas 
   

## DÚVIDAS
Caso você tenha dúvidas, não hesite em falar comigo:
* Linkedin: https://www.linkedin.com/in/thiagordebrito/
* Facebook: https://www.facebook.com/thiagorbrito
* E-mail: britotr@gmail.com

