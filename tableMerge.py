f1 = open("annotSV_selected.tsv", "r")
inFile1 = f1.readlines()
f1.close()
inFile2 = open("clinvarXML3.tsv", "r")
next(inFile2)
outFile = open("cnvs_big.tsv", "w")
outFile.write(""+"\t"+"RCV"+"\t"+"chr"+"\t"+"disease_finding"+"\t"+"HPO_terms"+"\t"+"Explicits"+"\t"+"start"+"\t"+"end"+"\t"+"genes\n")
geneTable = {"1":[], "2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[], "10":[], "11":[], "12":[], "13":[], "14":[], "15":[], "16":[], "17":[], "18":[], "19":[], "20":[], "21":[], "22":[], "X":[], "Y":[]}

for line in inFile1:
    chrom = str(line.split('\t')[0].strip())
    geneTable[chrom].append(line)

for line in inFile2:
    columns = line.split('\t')
    start = str(int(float(columns[6].strip())))
    end = str(int(float(columns[7].strip())))
    chrom = columns[2].strip()
    for row in geneTable[chrom]:
        columns2 = row.split('\t')
        if start==columns2[1].strip() and end==columns2[2].strip():
            outFile.write("\t".join(map(str, columns[:6])) +"\t"+ "\t".join(map(str, columns2[1:])))
            geneTable[chrom].remove(row)
            break

inFile2.close()
outFile.close()
