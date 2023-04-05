# IdralwelJsonVisualiser
#### By Ofghanirre ~ Antonin JEAN

------

### Description:
Python script that let you display with pydot a graph showcasing the inclusions and processing of an adventure / quest 
at JSON Idralwel's format.

- Place your files containing the Adventure well formatted for Idralwel in a folder and give the latter as argument to the
script

### Utilisation Console :
```txt
[Idralwel Json Visualiser]
usage: main.py [-h] [-f FOLDER] [-o OUTPUT] [-v] [--pdf] [--dot] [--png]                                                          
                                                                                                                                  
Idralwel Json Visualiser let you create and store dot graph out of special JSON formatted Adventure based off the Idralwel Project
                                                                                                                                  
options:                                                                                                                          
  -h, --help            show this help message and exit                                                                           
  -f FOLDER, --folder FOLDER                                                                                                      
                        The Adventure folder to search from, needs to have a quest folder and Dialogs folder in it                
  -o OUTPUT, --output OUTPUT                                                                                                      
                        The output file name to create (do not include extension)                                                 
  -v, --vertical        The output graph will be vertical, default horizontal                                                     
  --pdf                 Output a pdf file                                                                                         
  --dot                 Output a dot file                                                                                         
  --png                 Output a png file     
  ```

