#!/usr/bin/env python3

import psycopg2


def abrir_banco():
    pg = psycopg2.connect('dbname=news')
    return pg


def fechar_banco(conexao):
    conexao.close()


def artigos_populares():
    pg = abrir_banco()
    c = pg.cursor()
    c.execute("SELECT articles.title, count(log.path) AS total FROM log INNER JOIN \
              articles ON log.path = '/article/' || articles.slug GROUP BY \
              articles.title ORDER BY total DESC LIMIT 3")
    artigos = c.fetchall()
    print('Artigos mais populares')
    for art in artigos:
        print("%s - %s views" % (art[0], art[1]))
    pg.close()


def autores_populares():
    pg = abrir_banco()
    c = pg.cursor()
    c.execute("SELECT authors.name, count(log.path) AS total FROM authors\
                JOIN articles ON authors.id = articles.author\
                JOIN log ON log.path = '/article/' || articles.slug\
                GROUP BY authors.name ORDER BY total DESC")
    autor = c.fetchall()
    print('Autores mais visualizados')
    for aut in autor:
        print("%s - %s views" % (aut[0], aut[1]))

    pg.close()


def porcentagem():
    pg = abrir_banco()
    c = pg.cursor()
    c.execute("CREATE VIEW erro AS SELECT to_char(time, 'Mon DD, YYYY') as data, \
                count(time) as totalerro \
                FROM log WHERE status LIKE '404%'\
                GROUP BY data ORDER BY data ASC")

    c.execute("CREATE VIEW nerro AS SELECT to_char(time, 'Mon DD, YYYY') as data, \
                count(time) as totalnerro \
                FROM log GROUP BY data ORDER BY data ASC")

    c.execute("SELECT erro.data, ROUND(100.0 * erro.totalerro / nerro.totalnerro, 2)\
                FROM erro JOIN nerro ON nerro.data = erro.data\
                WHERE ROUND(100.0 * erro.totalerro / nerro.totalnerro, 2) > 1\
                ORDER BY ROUND DESC")
    result = c.fetchall()
    print('Dia com percentual de mais erros de acesso')
    for final in result:
        print(final[0] + ' - ' + str(final[1]) + '% errors')


artigos_populares()
autores_populares()
porcentagem()
