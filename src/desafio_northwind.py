import psycopg2
import pandas as pd


params = {
    "host": 'dbpostgres',
    "database": 'postgres',
    "user": 'postgres',
    "port": 5432,
    "password": 'postgrespwd'
}

def run_queries(params, commands):
    """ Runs the given query"""
    conn = None
    
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Run Queries one by one
        for command in commands:
            
            df = pd.read_sql_query(command, conn)
            df.to_csv('/usr/src/app/output.csv')
            

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Não alterar acima desta linhas
## --------------------------------------##
## Desafio

#1. Qual foi o melhor mês de vendas da Northwind?
query_1 = '''
       select *
       from categories
    '''


# Adicione todas as queries na lista abaixo
queries = [query_1]

#----------------------------------------##
# Não alterar abaixo desta linha

if __name__ == '__main__':
    run_queries(params, queries)
