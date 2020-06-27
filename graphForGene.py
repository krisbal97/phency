import networkx
import obonet
from networkx.drawing.nx_agraph import to_agraph
import graphviz as gv
from colour import Color

#url = 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'
#graph = obonet.read_obo(url)

# HPO database is saved in file hpo.txt, this was used to work without internet
database = open('hpo.txt', 'r')
graph = obonet.read_obo(database)
database.close()
id_to_name = {id_: data.get('name') for id_, data in graph.nodes(data = True)}

myID = ""
myStart = 0
myEnd = 0
myChromosome = ""
myScore = {}

def findGenes():
    ourData1 = open("cnvs_big.tsv", "r")
    next(ourData1)
    myGenes = []
    for line in ourData1:
        columns = line.split('\t')
        entryID = columns[1].strip()
        if entryID==myID:
            myGenes = columns[8].strip().split("/")
            ourData1.close()
            break
    newScore = affected(myGenes)
    return newScore

def affected(myGenes):
    newScore = {}
    ourData2 = open("genes_to_phenotype4.tsv", "r")
    inFile2 = ourData2.readlines()
    inFile2.pop(0)
    ourData2.close()
    mg=0
    g=0
    myGene = myGenes[mg]
    gene = inFile2[g].split('\t')[0].strip()
    while True:
        if myGene<gene: 
            if mg==len(myGenes)-1:
                break
            mg+=1
            myGene = myGenes[mg]
        elif myGene==gene:
            terms = inFile2[g].split("\t")[3].strip().split(";")
            for term in terms:
                if term in newScore:
                    newScore[term] +=(1-alpha)
                else:
                    newScore[term] =(1-alpha)
            if g==len(inFile2)-1:
                break
            g+=1
            gene = inFile2[g].split('\t')[0].strip()
        else:
            if g==len(inFile2)-1:
                break
            g+=1
            gene = inFile2[g].split('\t')[0].strip()
    return newScore

def setColors():
    maxScore = max(myScore.values())
    for term, score in myScore.items():
        x =1- score/maxScore
        c = Color(rgb=(0,x,1))
        gvGraph.get_node(term).attr['color'] = c.hex_l

print("Enter ID, coordinates and chromosome:")
coor = input().strip().split(" ")
myID = coor[0]
myStart = int(coor[1])
myEnd = int(coor[2])
myChromosome = coor[3]
#findGenes gives graph for only affected genes
myScore = findGenes()
nodes = myScore.keys()
if not nodes:
    print("There are no records in the data for this input.")
else:
    names = {term: id_to_name[term] for term in nodes}
    myGraph = graph.subgraph(nodes)
    gvGraph = to_agraph(myGraph)
    gvGraph.node_attr['style']='filled'
    gvGraph.node_attr['shape']='box'
    labels = {}
    for term, name in names.items():
        text = '['+ name +'; '+ str(myScore[term]) +']'
        gvGraph.get_node(term).attr['label'] = text
    setColors()
    gvGraph.layout('dot')
    gvGraph.draw('gene_output.png')
