import pyodbc

def insert_data(db_connection_string, data):
    """
    Insère les données triées dans la base de données.
    """
    try:
        # Connexion à la base de données via ODBC
        connection = pyodbc.connect(db_connection_string)
        cursor = connection.cursor()
        
        # Crée une requête d'insertion dynamique
        table_name = "employer"  # Nom de la table (à personnaliser)
        columns = ", ".join(data.columns)
        placeholders = ", ".join(["?"] * len(data.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        # Parcourir les données et insérer ligne par ligne
        for _, row in data.iterrows():
            cursor.execute(insert_query, tuple(row))
        
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Erreur lors de l'insertion dans la base de données : {e}")
