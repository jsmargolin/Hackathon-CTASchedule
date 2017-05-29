import mapgenerator, PIL
from PIL import Image
class Tile:
    def __init__(self, x, y, line):
        #int
        self.x = x
        #int
        self.y = y
        #string
        self.lineName = line
class Line:
    def __init__(self, tiles, name, numTrains):
        #list of Tile
        self.tiles = tiles
        #string
        self.name = name
        #int
        self.numTrains = numTrains
    #returns list of tiles contained in Line
    def getTiles(self):
        ans = []
        for tile in self.tiles:
            ans.append(tile)
        return ans
class LineWithData(Line):
    def __init__(self, tiles, color, numTrains, userData):
        Line.__init__(self, tiles, color, numTrains)
        #list of UserOnLine
        self.userData = userData
class Map:
    def __init__(self, lines):
        #list of Line
        self.lines = lines
    #returns list of tiles in Map
    def getTiles(self):
        ans = []
        for line in self.lines:
            ans.extend(line.getTiles())
        return ans
    def getLine(self, name):
        for line in self.lines:
            if line.name == name:
                return line
    def drawMap(self, fileName):
        ans = PIL.Image.new("RGBA", (800, 800), "white")
        for line in self.lines:
            for tile in line.tiles:
                # place tiles on image
                ans.paste(line.name, (tile.x * 8, tile.y * 8, tile.x * 8 + 8, tile.y * 8 + 8))
        ans.save(fileName)
class User:
    def __init__(self, tileTransfers, timeTransfers, lineNames):
        #list of Tile
        self.tileTransfers = tileTransfers
        #list of Int
        self.timeTransfers = timeTransfers
        #list of string
        self.lineNames = lineNames
class UserOnLine:
    def __init__(self, lineName, tileOn, timeOn, tileOff, timeOff):
        #string
        self.lineName = lineName
        #Tile
        self.tileOn = tileOn
        #int
        self.timeOn = timeOn
        #Tile
        self.tileOff = tileOff
        #int
        self.timeOff = timeOff
class Train:
    def __init__(self, timeLeave, lineName):
        self.timeLeave = timeLeave
        self.lineName = lineName
class LineInfo:
    def __init__(self, trains, name):
        self.trains = trains
        self.name = name