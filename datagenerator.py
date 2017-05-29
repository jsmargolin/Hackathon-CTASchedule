import random
import classes
import mapgenerator
class Stop:
    def __init__(self, x, y, time, color):
        self.x = x
        self.y = y
        self.time = time
        self.color = color
#makes a readable user from a list of transfer stops
def makeUser(stops, timeOff):
    ans = ""
    for stop in stops:
        ans += str(stop.x) + " " + str(stop.y) + " " + str(stop.color) + " " + str(stop.time) + " "
    return ans + str(timeOff)
#makes one random transfer stop
def getRandomStop(map):
    tiles = map.getTiles()
    tile = random.choice(tiles)
    stop = Stop(tile.x, tile.y, random.randint(0, 2399), tile.lineName)
    return stop
#makes list of random stops sorted by time
def makeRandomStops(map, x):
    stops = []
    for i in range(x):
        stops.append(getRandomStop(map))
    stops.sort(key=lambda x: x.time)
    return stops
#makes a string of n random users
def makeRandomUsers(map, n):
    ans = ""
    for i in range(n - 1):
        stops = makeRandomStops(map, random.randrange(2, 8))
        ans += makeUser(stops, random.randrange(stops[len(stops) - 1].time, 2400)) + "\n"
    stops = makeRandomStops(map, random.randrange(2, 8))
    ans += makeUser(stops, random.randrange(stops[len(stops) - 1].time, 2400))
    return ans
def writeRandomUsers(filename, map, n):
    file = open(filename, 'w')
    file.write(makeRandomUsers(map, n))
ln = ["red", "blue", "brown", "purple", "green", "pink", "black", "orange", "yellow", "gray"]
nt = [random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10),
          random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10),
          random.randrange(3, 10), random.randrange(3, 10)]
themap = mapgenerator.genMap(ln, nt, 10)
#writeRandomUsers("userdata.txt", themap, 200)