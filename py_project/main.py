import csv
import pyodbc

def read_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

def insert_data_to_db(connection_string, data):
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        for row in data:
            try:
                query = """
                    INSERT INTO employer (NumS, Nom, Localite)
                    VALUES (?, ?, ?)
                """
                cursor.execute(query, (row['NumS'], row['Nom'], row['Localite']))
            except Exception as e:
                print(f"Erreur lors de l'insertion : {e}")
                conn.rollback()
                return
        
        conn.commit()
        print("Données insérées avec succès.")
        conn.close()
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage : python main.py <DB_CONNECTION_STRING> <FILE_PATH>")
        sys.exit(1)

    connection_string = sys.argv[1]
    file_path = sys.argv[2]

    data = read_csv(file_path)
    if data:
        print("Données lues :")
        print(data)
        insert_data_to_db(connection_string, data)
