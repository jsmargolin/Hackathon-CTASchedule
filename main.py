import classes, datagenerator, mapgenerator, random
def readFile(filename):
    file = open(filename, "r")
    return file.readlines()
def dataToUser(ud):
    words = ud.split(" ")
    for i in range(len(words)):
        if (i % 4 != 2):
            words[i] = int(words[i])
    tiles = []
    times = []
    lines = []
    for i in range((len(words) - 1) // 4):
        tiles.append(classes.Tile(words[4 * i], words[4 * i + 1], words[4 * i + 2]))
        times.append(words[4 * i + 3])
        lines.append(words[4 * i + 2])
    tiles.append(classes.Tile(words[len(words) - 4], words[len(words) - 3], "null"))
    times.append(words[len(words) - 1])
    lines.append("null")
    return classes.User(tiles, times, lines)
def getUsers(ud):
    ans = []
    for line in ud:
        ans.append(dataToUser(line))
    return ans
def lineData(users, line):
    usersOnTheLine = []
    for user in users:
        for i in range(len(user.lineNames) - 2):
            if user.lineNames[i] == line.name:
                usersOnTheLine.append(classes.UserOnLine(user.lineNames[i], user.tileTransfers[i], user.timeTransfers[i], user.tileTransfers[i + 1], user.timeTransfers[i + 1]))
    return usersOnTheLine
def makeDataMap(map, users):
    lines = []
    for line in map.lines:
        tiles = line.tiles
        name = line.name
        numTrains = line.numTrains
        ud = lineData(users, line)
        lines.append(classes.LineWithData(tiles, name, numTrains, ud))
    return classes.Map(lines)
#finds how long a user has to wait at a transfer
def waitTime(map, user, lineinfo):
    tile = user.tileOn
    time = user.timeOn
    startx = map.getLine(tile.lineName).tiles[0].x
    starty = map.getLine(tile.lineName).tiles[0].y
    offset = (int(tile.y) - int(starty)) + (int(tile.x) - int(startx))
    if time < lineinfo.trains[0].timeLeave + offset:
        train = 0
    elif time > lineinfo.trains[len(lineinfo.trains) - 1].timeLeave + offset:
        return 2400 - time
    else:
        for i in range(len(lineinfo.trains)):
            if (lineinfo.trains[i].timeLeave + offset >= time):
                train = i
                break;
    return lineinfo.trains[train].timeLeave + offset - time
def lineWaitTime(lineWithData, lineInfo, map):
    twt = 0
    for user in lineWithData.userData:
        twt += waitTime(map, user, lineInfo)
    return twt
def mapWaitTime(map, lineInfos):
    twt = 0
    for i in range(len(map.lines)):
        twt += lineWaitTime(map.lines[i], lineInfos[i], map)
    return twt
def optimizeLineDataHelper(reps, lineWithData, lineInfo, map, n):
    for i in range(reps):
        for train in lineInfo.trains:
            x = lineWaitTime(lineWithData, lineInfo, map)
            if train.timeLeave < 2399:
                train.timeLeave += n
            y  = lineWaitTime(lineWithData, lineInfo, map)
            if train.timeLeave > 2:
                train.timeLeave -= 2 * n
            z = lineWaitTime(lineWithData, lineInfo, map)
            if train.timeLeave < 2399:
                train.timeLeave += n
            while (y < x and train.timeLeave < 2400 - n):
                train.timeLeave += n
                x = y
                y = lineWaitTime(lineWithData, lineInfo, map)
            while (z < x and train.timeLeave > n):
                train.timeLeave -= n
                x = z
                z = lineWaitTime(lineWithData, lineInfo, map)
    return lineInfo
def superop(lineWithData, lineInfo, map, n):
    optimizeLineDataHelper(2 * n, lineWithData, lineInfo, map, 200)
    optimizeLineDataHelper(5 * n, lineWithData, lineInfo, map, 100)
    optimizeLineDataHelper(10 * n, lineWithData, lineInfo, map, 50)
    optimizeLineDataHelper(25 * n, lineWithData, lineInfo, map, 10)
    optimizeLineDataHelper(50 * n, lineWithData, lineInfo, map, 5)
    optimizeLineDataHelper(100 * n, lineWithData, lineInfo, map, 2)
    optimizeLineDataHelper(150 * n, lineWithData, lineInfo, map, 1)
    return lineInfo
def startingData(line):
    n = line.name
    lastindex = len(line.tiles) - 1
    trains = []
    for i in range(line.numTrains):
        trains.append(classes.Train((i + 1) * (2400 // (line.numTrains + 1)), line.name))
    return classes.LineInfo(trains, n)
def optimizeMap(map):
    lineSchedules = []
    for line in map.lines:
        sd = startingData(line)
        lineSchedules.append(superop(line, sd, map, 1))
    return lineSchedules
userdata = readFile("userdata.txt")
users = getUsers(userdata)
datamap = makeDataMap(datagenerator.themap, users)
#datamap.drawMap('map_drawing.jpg')
sd = []
for i in range(len(datamap.lines)):
    sd.append(startingData(datamap.lines[i]))
preWait = mapWaitTime(datamap, sd)
ls = optimizeMap(datamap)
postWait = (mapWaitTime(datamap, ls))
train_times = []
for li in ls:
    train_times.append(li.name + ": ")
    for i in range(len(li.trains)):
        train_times.append("Train " + str(i + 1) + ": " + str(li.trains[i].timeLeave))