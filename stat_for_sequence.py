allFound = 0
atLeastOne = 0
nothing = 0

f = open("cnvs_big.tsv", "r")
inFile1 = f.readlines()
inFile1.pop(0)
l=len(inFile1)
inFile2 = inFile1.copy()
f.close()
outFile1 = open("big_seq_stat.tsv", "w")
outFile2 = open("big_seq_stat.txt", "w")
i=0
for line1 in inFile1:
    i+=1
    columns = line1.split('\t')
    myChromosome = columns[2]
    myStart = int(columns[6])
    myEnd = int(columns[7])
    myID = columns[0]
    myExp = columns[5].split(";")
    found = []
    for line2 in inFile2:
        columns2 = line2.split('\t')
        chromosome = columns2[2]
        start = int(columns2[6])
        end = int(columns2[7])
        entryID = columns2[0]
        terms = columns2[4].split(";")
        if not entryID==myID and myChromosome==chromosome and not end<myStart and not start>myEnd:
            for e in myExp:
                if e in terms:
                    found.append(e)
                    myExp.remove(e)
        if not myExp:
            allFound +=1
            break
    if found:
        atLeastOne +=1
    else:
        nothing +=1
    outFile1.write("\t".join(map(str, columns[:-1])) + "\t" + ";".join(map(str, found)) +"\n")
    if i%17==00:
        print("Hotovo: "+str(i*100/l)+"%\n")
outFile2.write("Number of CNV, where all phenotypes were found: " + str(allFound) +"\n")
outFile2.write("Number of CNV, where at least one  phenotype was found: " + str(atLeastOne) +"\n")
outFile2.write("Number of CNV, where no phenotype was found: " + str(nothing) +"\n")
outFile1.close()
outFile2.close()
