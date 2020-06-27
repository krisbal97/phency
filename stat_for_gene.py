allFound = 0
atLeastOne = 0
nothing = 0

inFile1 = open("cnvs_big.tsv", "r")
next(inFile1)
f2 = open("genes_to_phenotype4.tsv", "r")
inFile2 = f2.readlines()
inFile2.pop(0)
f2.close()
outFile1 = open("big_gene_stat.tsv", "w")
outFile2 = open("big_gene_stat.txt", "w")

def findGenes(genes, expl):
    mg=0
    g=0
    myGene = genes[mg]
    gene = inFile2[g].split('\t')[0].strip()
    wasFound = []
    while True:
        if myGene<gene:
            if mg==len(genes)-1:
                break
            mg+=1
            myGene = genes[mg]
        elif myGene==gene:
            for e in expl:
                if e in inFile2[g].split('\t')[3].strip().split(';'):
                    wasFound.append(e)
                    expl.remove(e)
                    break
            if g==len(inFile2)-1:
                break
            g+=1
            gene = inFile2[g].split('\t')[0].strip()
        else:
            if g==len(inFile2)-1:
                break
            g+=1
            gene = inFile2[g].split('\t')[0].strip()
        if not expl or g==len(inFile2)-1 or mg==len(genes)-1:
            break
    return (wasFound, bool(expl)) 

for line1 in inFile1:
    columns = line1.split('\t')
    expl = columns[5].strip().split(';')
    genes = columns[8].strip().split('/')
    if genes:
        returned = findGenes(genes, expl)
        if returned[0]:
            atLeastOne +=1
        else:
            nothing +=1
        if not returned[1]:
            allFound +=1
        outFile1.write(line1.strip() + "\t" + ";".join(map(str, returned[0])) +"\n")
    else: 
        outFile1.write(line1)
outFile2.write("Number of CNV, where all phenotypes were found: " + str(allFound) +"\n")
outFile2.write("Number of CNV, where at least one  phenotype was found: " + str(atLeastOne) +"\n")
outFile2.write("Number of CNV, where no phenotype was found: " + str(nothing) +"\n")
outFile1.close()
outFile2.close()
