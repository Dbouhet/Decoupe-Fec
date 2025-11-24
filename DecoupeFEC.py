import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
import sys

# Pour ajouter une icône à l'exe (optionnel mais joli)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def decouper_fec(fichier_entree, nb_fichiers):
    base_nom, extension = os.path.splitext(os.path.basename(fichier_entree))
    dossier_sortie = os.path.dirname(fichier_entree)
    
    try:
        with open(fichier_entree, 'r', encoding='utf-8') as f:
            entete = f.readline()
            lignes = f.readlines()
    except UnicodeDecodeError:
        try:
            with open(fichier_entree, 'r', encoding='iso-8859-1') as f:
                entete = f.readline()
                lignes = f.readlines()
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lire le fichier :\n{e}")
            return
    
    total_lignes = len(lignes)
    if total_lignes == 0:
        messagebox.showinfo("Info", "Le fichier ne contient aucune écriture.")
        return
    
    lignes_par_fichier = total_lignes // nb_fichiers
    reste = total_lignes % nb_fichiers
    
    index_ligne = 0
    for i in range(nb_fichiers):
        lignes_cette_partie = lignes_par_fichier + (1 if i < reste else 0)
        fichier_sortie = os.path.join(dossier_sortie, f"{base_nom}_part{i+1}{extension}")
        
        with open(fichier_sortie, 'w', encoding='utf-8', newline='\n') as f_out:
            f_out.write(entete)
            f_out.writelines(lignes[index_ligne:index_ligne + lignes_cette_partie])
        
        index_ligne += lignes_cette_partie
    
    messagebox.showinfo("Succès", f"Découpage terminé !\n{nb_fichiers} fichiers créés dans le même dossier.")

# ====================== INTERFACE ======================
root = tk.Tk()
root.title("Découpe FEC - Outil autonome")
root.geometry("500x200")
root.resizable(False, False)

# Optionnel : icône (mets un fichier favicon.ico à côté du script si tu veux)
# root.iconbitmap(resource_path("favicon.ico"))

tk.Label(root, text="Découpeur de fichiers FEC volumineux", font=("Arial", 14, "bold")).pack(pady=20)
tk.Label(root, text="Cliquez ci-dessous pour sélectionner votre fichier FEC", font=("Arial", 10)).pack(pady=10)

def lancer():
    fichier = filedialog.askopenfilename(
        title="Sélectionnez votre fichier FEC",
        filetypes=[("Fichiers FEC", "*.fec *.txt"), ("Tous les fichiers", "*.*")]
    )
    if not fichier:
        return
    
    nb = simpledialog.askinteger("Nombre de parties", 
                                "En combien de fichiers voulez-vous découper ?\n(minimum 2)",
                                minvalue=2, maxvalue=500)
    if nb:
        decouper_fec(fichier, nb)

btn = tk.Button(root, text="Sélectionner le fichier FEC", font=("Arial", 12), bg="#4CAF50", fg="white", height=2, width=30, command=lancer)
btn.pack(pady=20)

root.mainloop()