inFile1=open("alpha01extract.tsv", "r")
inFile2=open("alpha02extract.tsv", "r")
inFile3=open("alpha03extract.tsv", "r")
inFile4=open("alpha04extract.tsv", "r")
inFile5=open("alpha05extract.tsv", "r")
inFile6=open("alpha06extract.tsv", "r")
inFile7=open("alpha07extract.tsv", "r")
inFile8=open("alpha08extract.tsv", "r")
inFile9=open("alpha09extract.tsv", "r")
inFile10=open("alpha10extract.tsv", "r")
fileList=[]
fileList.append(inFile1.readlines().copy())
fileList.append(inFile2.readlines())
fileList.append(inFile3.readlines())
fileList.append(inFile4.readlines())
fileList.append(inFile5.readlines())
fileList.append(inFile6.readlines())
fileList.append(inFile7.readlines())
fileList.append(inFile8.readlines())
fileList.append(inFile9.readlines())
fileList.append(inFile10.readlines())

inFile1.close()
inFile2.close()
inFile3.close()
inFile4.close()
inFile5.close()
inFile6.close()
inFile7.close()
inFile8.close()
inFile9.close()
inFile10.close()

lf=len(fileList[0])
i=1
lastCNV=""
empty=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
alphaWin = empty.copy()
#list storing ratio for every alpha
ratios = empty.copy()
numOfTerms=0
col1=fileList[0][i].strip().split('\t')
lastCNV=col1[1]
while True:
    #col1 is list columns from one line in file1
    col1=fileList[0][i].strip().split('\t')
    if col1[1]==lastCNV and not col1[3]=="0":
        numOfTerms+=1
        ratios[0]+=float(col1[4])
        for j in range(9):
            ratios[j+1]+=float(fileList[j+1][i].strip().split('\t')[4])
        i+=1
    elif col1[1]==lastCNV:
        i+=1
    else:
        lastCNV=col1[1]
        for j in range(10):
            ratios[j]=ratios[j]/numOfTerms
        numOfTerms=0
        m=min(ratios) 
        winners = [x for x, y in enumerate(ratios) if y == m] 
        for x in winners:
            alphaWin[x]+=1
        ratios=empty.copy()
    if i%170==0:
        print(str(i*100/lf)+"% done")
    if i==lf-1:
        break
outFile=open("alpha_results.tsv", "w")
outFile.write("\t0.1\t0.2\t0.3\t0.4\t0.5\t0.6\t0.7\t0.8\t0.9\t1.0\n")
outFile.write("times\t"+"\t".join(map(str, alphaWin))+"\n")
outFile.close()
