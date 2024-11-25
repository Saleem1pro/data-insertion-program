import pandas as pd

def parse_file(file_path):
    """
    Parse le fichier en fonction de son extension et retourne les données triées.
    """
    try:
        # Déterminer le type de fichier par extension
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            data = pd.read_excel(file_path)
        elif file_path.endswith('.txt'):
            data = pd.read_csv(file_path, delimiter="\t")
        else:
            raise ValueError("Type de fichier non pris en charge.")
        
        # Tri des données en fonction d'une colonne (à ajuster selon votre logique)
        data = data.sort_values(by=data.columns[0])  # Tri par la première colonne
        return data
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None
