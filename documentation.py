import os

def generate_documentation(directory, output_file):
    """
    Génère une documentation pour tous les fichiers .py dans un dossier donné.
    La documentation est sauvegardée dans un fichier texte.

    :param directory: Chemin du dossier contenant les fichiers .py
    :param output_file: Chemin du fichier texte de sortie
    """
    with open(output_file, 'w', encoding='utf-8') as doc_file:
        doc_file.write("Documentation des fichiers Python\n")
        doc_file.write("=" * 40 + "\n\n")
        
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    doc_file.write(f"Fichier : {file}\n")
                    doc_file.write("-" * 40 + "\n")
                    
                    with open(file_path, 'r', encoding='utf-8') as py_file:
                        lines = py_file.readlines()
                        for line in lines:
                            # Inclure uniquement les commentaires et les définitions de fonctions/classes
                            if line.strip().startswith("#") or line.strip().startswith("def ") or line.strip().startswith("class "):
                                doc_file.write(line)
                    
                    doc_file.write("\n\n")

# Chemin du dossier contenant les fichiers .py
directory = r"C:\Users\33767\Documents\gab\cours\université\L1\projet_fil_rouge"

# Chemin du fichier de sortie
output_file = os.path.join(directory, "documentation.txt")

# Générer la documentation
generate_documentation(directory, output_file)

print(f"La documentation a été générée dans le fichier : {output_file}")