import classes
import random
def getRandomLine(linename, numTrains):
    tilex = random.randrange(0, 50)
    tiley = random.randrange(0, 50)
    start = classes.Tile(tilex, tiley, linename)
    ans = [start]
    for i in range(random.randrange(15, 100)):
        binaryFlip = random.randrange(0, 2)
        if binaryFlip == 0:
            tilex += 1
        else:
            tiley += 1
        if (tilex < 100 and tiley < 100):
            ans.append(classes.Tile(tilex, tiley, linename))
        else:
            break
    return classes.Line(ans, linename, numTrains)
def genMap(lineNames, numTrains, numLines):
    ans = []
    for i in range(numLines):
        ans.append(getRandomLine(lineNames[i], numTrains[i]))
    return classes.Map(ans)
ln = ["red", "blue", "brown", "purple", "green", "pink"]
nt = [random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10)]