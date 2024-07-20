# create_database_and_tables.py

import psycopg2
from database.db_config import config

def create_connection():
    params = config()
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    return conn

def execute_sql_file(cursor, filepath):
    with open(filepath, 'r') as file:
        sql_commands = file.read()
        cursor.execute(sql_commands)

if __name__ == '__main__':
    try:
        # Connexion à la base de données pour créer les tables
        conn = create_connection()
        cursor = conn.cursor()
        
        # Chemin vers le fichier SQL
        sql_filepath = 'database/create_tables.sql'
        
        # Exécution du fichier SQL pour créer les tables
        execute_sql_file(cursor, sql_filepath)
        
        cursor.close()
        conn.close()
        
        print("Tables créées avec succès.")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
