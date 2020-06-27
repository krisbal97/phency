inFile = open("clinvarXML.tsv", "r")
outFile = open("clinvarXML2.tsv", "w")
for line in inFile: 
    columns = line.split('\t')
#only records with start and end position and without "not providing" phenotype
    if not columns[15].strip()=="" and not columns[17].strip()=="" and not columns[9].strip()=='not provided':        
        outFile.write(columns[0].strip() +"\t"+ columns[2].strip() +"\t"+ columns[3].strip() +"\t"+ columns[9].strip() +"\t"+ columns[15].strip() +"\t"+ columns[17].strip() +"\n")
inFile.close()
outFile.close()
