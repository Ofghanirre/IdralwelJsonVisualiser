# IdralwelJsonVisualiser
Script python permettant d'afficher avec pydot un graphe représentant les inclusions et déroulés d'une aventure au format JSON Idralwel

Placer vos dossiers JSON formatté pour le programme Idralwel dans un dossier, et remplacer les chemins définis dans le `main.py` jusqu'au chemin des quest et des dialogues

Fournissez un dossier de sortie ainsi qu'un nom de fichier de sortie

par défaut la fonction `create_graph` donnera des exports au format:
- dot
- pdf
- png

vous pouvez désactiver ces exports en fournissant comme paramètre un ou deux booléens à la fonction `create_step_graph`
ex: 
```py
create_step_graph(stepParser, OUTPUT_NAME, pdf=False, png=False)`
```
Ne fournira donc qu'un output au format **dot**
