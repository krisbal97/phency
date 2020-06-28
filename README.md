# phency
Phenotype prediction from CNV data
In our work this codes and data are used. Manz command line commands were used as well, but are not mentioned here.  

cnvs_big.tsv
the data storing information about CNVs and their relation to phenotypes, genes etc.

complexGraph.py
Complex model, program, which returns graph of prediction of phenotype based on combination of Gene model and CNV overlap model
input: ID of CNV in our data, startposition on sequence, endposition, chromosome
output: complex_output.png storing the graph
To use this script, the files hpo.txt, cnvs_big.tsv and the file genes_to_phenotypes4.tsv (which can be obtained by concatenation of files genes_to_phenotypes4a.tsv and genes_to_phenotypes4b.tsv respectively) are required.
Since the only data we had were the cnvs_big.tsv, this script is in state to be able to process input from our data. Thus also the ID in input is required.

genes_to_phenotypes4a.tsv and genes_to_phenotypes4b.tsv
These filesa are ready to be concatenated to file genes_to_phenotypes4.tsv, since the file genes_to_phenotypes4.tsv was too large to be uploaded.

count_alpha.py
This script was used for statistics. It determines the value of alpha from files, storing the values of ratio of terms with higher score than score of explicit term to all terms in particular graph for each explicit term. 

equalDepths.py
This script counts the number of explicit terms which occured in the same depth of the one graph.

graphForGene.py
Gene model, program, which returns graph of prediction of phenotype based on affected genes
input: ID of CNV in our data, startposition on sequence, endposition, chromosome
output: gene_output.png storing the graph
To use this script, the files hpo.txt, cnvs_big.tsv and the file genes_to_phenotypes4.tsv (which can be obtained by concatenation of files genes_to_phenotypes4a.tsv and genes_to_phenotypes4b.tsv respectively) are required.
Since the only data we had were the cnvs_big.tsv, this script is in state to be able to process input from our data. Thus also the ID in input is required.

graphForSequence.py
CNV overlap model, program, which returns graph of prediction of phenotype based on overlps of CNVs
input: ID of CNV in our data, startposition on sequence, endposition, chromosome
output: cnv_output.png storing the graph
To use this script, the files hpo.txt, cnvs_big.tsv are needed.
Since the only data we had were the cnvs_big.tsv, this script is in state to be able to process input from our data. Thus also the ID in input is required.

hpo.txt
Our modified version of HPO database

metric.py
This script calculates the ratio between the terms with higher score than explicit terms to all terms in particular graph for particular alpha. Which alpha is used is determined bz using input file. This script was used for our statistics only, thus the used file can be set manualz in the script.

processing1.py
Script for processing the data from ClinVar database. In removes all unnecessary records and columns.

processing2.py
Script for next processing of our data. It removes record of phenotzpes Developmental delay and Global developmental delay.

stat_for_both.py
The statistic for the Complex model.
This script counts the number of cnvs, for wich
a) all its explicit terms could be found in output graph.
b) at least one of its explicit terms could be found in output graph.
c) none of its explicit terms could be found in output graph.

stat_for_gene.py
The statistic for the Gene model.
This script counts the number of cnvs, for wich
a) all its explicit terms could be found in output graph.
b) at least one of its explicit terms could be found in output graph.
c) none of its explicit terms could be found in output graph.

stat_for_sequence.py
The statistic for the CNV overlap model.
This script counts the number of cnvs, for wich
a) all its explicit terms could be found in output graph.
b) at least one of its explicit terms could be found in output graph.
c) none of its explicit terms could be found in output graph.

tableMerge.py
This script creates the cnvs_big.tsv table by merging the data of CNVs and the data of genes related to CNVs together.
