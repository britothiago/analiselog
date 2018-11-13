## ANÁLISE DE LOGS

Este projeto é um exercício realizado para a Udacity do Nanodegree de Desevolvimento Web Fullstack.

Este deverá ser capaz de responder às seguintes questões:

1. Quais são os três artigos mais populares de todos os tempos?

2. Quem são os autores de artigos mais populares de todos os tempos?

3. Em quais dias mais de 1% das requisições resultaram em erros? 

## INSTALAÇÃO

Clone o repositório para baixar os arquivos na mesma pasta, suba o arquivo SQL no postgre e execute as funções para obter os resultados.

`$ git clone https://github.com/britothiago/analiselog.git`

Para executar as funções, basta retirar as funções dos comentários.

*Recomenda-se a utilização da versão 3.5.2 do Python*

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

