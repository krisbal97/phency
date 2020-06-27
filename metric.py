inFile10=open("alpha08_and_score.tsv", "r")
file1=inFile10.readlines()
inFile10.close()
outFile=open("08metric_results.tsv", "w")
outFile.write("RCV\taverage_ratio\n")
lf=len(file1)
i=1
ratioSuma = 0
lastCNV=""
#list storing ratio for every alpha
ratios = 0
numOfTerms=0
col1=file1[i].strip().split('\t')
lastCNV=col1[1]
while True:
    #col1 is list of columns from one line in file1
    col1=file1[i].strip().split('\t')
    if col1[1]==lastCNV and not col1[3]=="0":
        numOfTerms+=1
        ratios+=float(col1[4])
        ratioSuma+=float(col1[4])
        i+=1
    elif col1[1]==lastCNV:
        i+=1
    else:
        outFile.write(lastCNV+"\t"+str(ratios/numOfTerms)+"\n")
        lastCNV=col1[1]
        numOfTerms=0
        ratios=0
    if i%1700==0:
        print(str(i*100/lf)+"% done")
    if i==lf-1:
        break
#print(ratioSuma/(lf-1)
outFile.close()

