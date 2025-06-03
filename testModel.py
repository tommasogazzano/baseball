from model.model import Model

m = Model()
m.getTeamsOfYear(2015)
m.buildGraph(2015)
m.printGraphDetails()

start = m.getRandomNode()
m.getBestPath(start)
path, score = m.getBestPathV2(start)
print(len(path), score)