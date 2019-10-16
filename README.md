### This repository cointains different applications for Bioinformatic students

Located in different folders, some of them are Writen for jupyter notebooks, so the students can run it through Google Colab (https://colab.research.google.com).

#### jupyter_peptide_hla_predictor

This folder cointains all files needed to build a peptide-HLA binding predictor for the allele HLA-A\*02:01. Data cleaned from the IEDB (http://www.iedb.org/database_export_v3.php). The script is written in python3 jupyter notebook, and it cointains different annotations for each step that guides the user.

#### jupyter_pele_plotter

This folder cointains all files needed to compute the r-squared correlation of a series of PELE binding affinities. It is written in python3 jupyter notebook.

#### monte_carlo_compute_pi

This folder cointains all files needed for a Monte Carlo predictor in python3 and in cython. User can modify the number of runs in the main() function of the python script, to see how important is computing efficiency when the number of calculations increase. In the end, it prints an approximation of the pi-value, and the elapsed time for python3 and cython.
