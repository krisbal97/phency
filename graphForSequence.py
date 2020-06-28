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

#myID = ""
myStart = 0
myEnd = 0
myChromosome = ""
myScore = {}

def calculateScore_seq(start, end):
    length = end-start+1
    overlapStart = max(myStart, start)
    overlapEnd = min(myEnd, end)
    overlapLength = overlapEnd-overlapStart+1
    return overlapLength/length

def findOverlap():
    ourData = open("cnvs_big.tsv", "r")
    next(ourData)
    for line in ourData:
        columns = line.split('\t')
        chromosome = columns[2].strip()
        start = int(columns[6])
        end = int(columns[7])
        entryID = columns[1].strip()
        #if not entryID==myID and myChromosome==chromosome and not end<myStart and not start>myEnd:
        if myChromosome==chromosome and not end<myStart and not start>myEnd:
            score = calculateScore_seq(start, end)
            terms = columns[4].strip().split(";")
            for term in terms:
                if term in myScore:
                    myScore[term] += score
                else:
                    myScore[term] = score
    ourData.close()

def setColors():
    maxScore = max(myScore.values())
    for term, score in myScore.items():
        x =1- score/maxScore
        c = Color(rgb=(0,x,1))
        gvGraph.get_node(term).attr['color'] = c.hex_l

print("Enter coordinates and chromosome:")
coor = input().strip().split(" ")
#myID = coor[0]
myStart = int(coor[0])
myEnd = int(coor[1])
myChromosome = coor[2]
findOverlap()
nodes = myScore.keys()
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
gvGraph.draw('cnv_output.png')
