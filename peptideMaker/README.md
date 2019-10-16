# peptideMaker

## About peptideMaker ##

peptideMaker runs FoldX in order to generate mutations on PDB files. It is focused on modifying peptides bound to the MHC complex.
Before running peptideMaker, please make sure that you have the following dependencies installed on your computer:

1) subprocess
2) os
3) multiprocessing / Pool
4) shutil

### Running command ###

peptideMaker is coded in python3, once you have checked carefully the instructions below, you can run it by a simple:

``python3 peptideMaker.py
``
### Getting Foldx ###

FoldX licence is free for academic purposes. You can find the Registration process in the following link:

Foldx academic license: http://foldxsuite.crg.eu/academic-license-info

### I have Foldx, what shall I do now ###

Now that you have installed Foldx, you need some files to work with:

1) A file contianing one column, each row being a peptide that you want to model.
2) A PDB template file to generate the model.
3) A rotabase path of Foldx (should be in the foldx intallation folder, it is called **rotabase.txt**)

### Additionally comments ###

4) Multiprocessing is allowed, so you can tune the "processors" variable according to your ressources and needs.
5) Foldx needs a format sequence to mutate, example: "AL1P, FL2W;". This means: 

	5.1) From the PDB file I am working with, please mutate Alanine (A) from position 1 in the chain L into a Proline (P).
	
	5.2) Moreover, please mutate Phenilalanine (F) from position 2 in the chain L into a Triptophan (W). Note the semicolon at the end, it is important.
