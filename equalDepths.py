import networkx
import obonet

database = open('hpo.txt', 'r')
graph = obonet.read_obo(database)
database.close()

#inFile = open("cnvs_plus_genes.tsv", "r")
inFile = open("cnvs_plus_genes.tsv", "r")
next(inFile)
outFile = open("equalDepths.txt", "w")
i=0
ed=0
for line in inFile:
    i+=1
    columns = line.strip().split('\t')
    expl = columns[5].strip().split(";")
    subgraph = columns[4].strip().split(";")
    myGraph = graph.subgraph(subgraph)
    #print(myGraph.nodes())
    depths = []
    for e in expl:
        #print(networkx.has_path(myGraph, e,'HP:0000001'))
        d = networkx.shortest_path(myGraph, source=e, target='HP:0000001')
        #print(d)
        if d in depths:
            ed+=1
            outFile.write(str(i) + "\t" + columns[0] + "\n")
            break
        else:
            depths.append(d)
outFile.write("Number of cnv with explicit terms in equal depth is: " + str(ed)+ "\n")
inFile.close()
outFile.close()
