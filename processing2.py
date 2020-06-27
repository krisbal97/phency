from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import networkx
import obonet

database = open('../hpo.txt', 'r')
graph = obonet.read_obo(database)
inFile = open("clinvarXML2.tsv", "r")
#inFile = open("pokus1.tsv", "r")
outFile1 = open("clinvarXML3.tsv", "w")
outFile2 = open("clinvarXML_for_annotsv.tsv", "w")


wasUsed = {"disease_finding": (["HPO_terms"], "Explicits"), "Keratocystic odontogenic tumors of jaws": (["HP:0000164", "HP:0100649", "HP:0010603", "HP:0000118", "HP:0000001", "HP:0000234", "HP:0000152", "HP:0000271", "HP:0031816", "HP:0100612", "HP:0000163", "HP:0002664", "HP:0000153", "HP:0011793"], "HP:0010603")} 
name_to_id = {data.get('name'): id_ for id_, data in graph.nodes(data = True)}
all_names = [name for name in name_to_id]
unwanted = ["Global developmental delay", "Developmental delay AND/OR other significant developmental or morphological phenotypes"]

def subgraph(phenotype): 
    termID = name_to_id[process.extractOne(phenotype, all_names)[0]]
    subg = networkx.descendants(graph, termID)
    subg.add(termID)
    return (subg, termID)

def list_to_string(l):
    if l[0]==1:
        return str(l)
    else:
        newString = l.pop()
        for term in l:
            newString += ";" + term
        return newString

def pheno_to_string(p):
    if len(p[0])==1:
        return p
    else:
        newString = p.pop()
        for term in p:
            newString += "|" + term
    return newString


for line in inFile:
    columns = line.rstrip().split('\t')
    allPheno = columns[3].strip().split("|")
    phenotypes = ""
    bigSubgraph = ""
    allExplicit = ""
    for pheno in allPheno:
        if pheno not in unwanted:
            phenotypes += pheno +"|"
            if pheno not in wasUsed: 
                returned = subgraph(pheno)
                returnedTerms = returned[0]
                explicitTerm = returned[1]
                wasUsed[pheno] = (returnedTerms, explicitTerm)
                bigSubgraph += ";".join(map(str, returnedTerms)) +";"
                allExplicit += explicitTerm +";"
            else:
                bigSubgraph += ";".join(map(str, wasUsed[pheno][0])) + ";"
                allExplicit += wasUsed[pheno][1] +";"
    if bigSubgraph:
        p = phenotypes[:-1]
        s = bigSubgraph[:-1]
        e = allExplicit[:-1]
        newLine = "\t".join(map(str, columns[:3])) +"\t"+ p  +"\t"+ s +"\t"+ e +"\t"+ columns[4] +"\t"+ columns[5]
        outFile1.write(newLine + "\n")
        outFile2.write(columns[2] +"\t"+ columns[4] +"\t"+ columns[5] +"\t"+ "DEL" +"\n")
database.close()
inFile.close()
outFile1.close()
outFile2.close()

