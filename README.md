# DecoupeFEC ✂️

**Outil en ligne de commande ultra-simple pour découper un fichier FEC trop volumineux**  
(en plusieurs fichiers FEC valides, prêts à être importés dans un logiciel de comptabilité)

### Problème classique
Certains logiciels refusent les FEC de plus de 100 000 lignes ou 10 Mo → rejet à l'import.

### Solution : DecoupeFEC
Découpe ton fichier en autant de parties que nécessaire, **en gardant l'entête obligatoireible et le format exact**.

### Installation (5 secondes)

```bash
# Télécharge le script
curl -L -O https://raw.githubusercontent.com/TonPseudo/DecoupeFEC/main/DecoupeFEC.py

# Rend-le exécutable
chmod +x DecoupeFEC.py
