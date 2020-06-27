allFound = 0
atLeastOne = 0
nothing = 0

f1 = open("big_seq_stat.tsv", "r")
inFile1 = f1.readlines()
f1.close()
f2 = open("big_gene_stat.tsv", "r")
inFile2 = f2.readlines()
f2.close()
outFile1 = open("big_both_stat.tsv", "w")
outFile2 = open("big_both_stat.txt", "w")

numLines = len(inFile1)

for l in range (numLines):
    line1 = inFile1[l].strip().split('\t')
    line2 = inFile2[l].strip().split('\t')
    if len(line1)==9:
	#founded termes from seq.stat.
        wasFound1 = line1[8].strip().split(';')
        print("1: "+str(wasFound1)+"\n")
    else:
        wasFound1 = []
    if len(line2)==10:
	#founded score from gene stat.
        wasFound2 = line2[9].strip().split(';')
        print("2: "+str(wasFound2)+"\n")
    else:
        wasFound2 = []
    #explicit terms
    expl = line1[5].strip().split(';')
    #only unique terms are wanted
    wasFound=list(set(wasFound1+wasFound2))
    if "" in wasFound:
        wasFound.remove("")
    if wasFound:
        atLeastOne +=1
        if len(expl)==len(wasFound):
            expl.sort()
            wasFound.sort()
            if expl==wasFound:
                allFound +=1
    else:
        nothing +=1
    outFile1.write("\t".join(map(str, line1[:8])) +'\t'+ ";".join(map(str, wasFound)) +'\n')


outFile2.write("Number of CNV, where all phenotypes were found: " + str(allFound) +"\n")
outFile2.write("Number of CNV, where at least one  phenotype was found: " + str(atLeastOne) +"\n")
outFile2.write("Number of CNV, where no phenotype was found: " + str(nothing) +"\n")
outFile1.close()
outFile2.close()

