import math

# contains each sample
class samples():

    A = [43.5, 39, 17.5]
    B = [47.5, 43, 9.5]
    C = [71.5, 21.5, 7]
    D = [48, 40, 12]
    E = [68.25, 22.75, 9]
    F = [75, 17.5, 7.5]

    all = [A, B, C, D, E, F]

# a list of each texture and its bounds, as well as labeled names
class textures():

    sand = [(90, 10), (85, 0), (100, 0)]
    loamySand = [(85, 15), (70, 0), (85, 0), (90, 10)]
    sandyLoam = [(80, 20), (52.5, 20), (52.5, 7.5), (42.5, 7.5), (50, 0), (70, 0), (85, 15)]
    sandyClayLoam = [(65, 35), (45, 35), (45, 27.5), (52.5, 20), (80, 20)]
    loam = [(45, 27.5), (22.5, 27.5), (42.5, 7.5), (52.5, 7.5), (52.5, 20)]
    siltLoam = [(22.5, 27.5), (0, 27.5), (0, 12.5), (7.5, 12.5), (20, 0), (50, 0)]
    silt = [(7.5, 12.5), (0, 12.5), (0, 0), (20, 0)]
    sandyClay = [(45, 55), (45, 35), (65, 35)]
    clayLoam = [(45, 40), (20, 40), (20, 27.5), (45, 27.5)]
    siltyClayLoam = [(20, 40), (0, 40), (0, 27.5), (20, 27.5)]
    clay = [(0, 100), (0, 60), (20, 40), (45, 40), (45, 55)]
    siltyClay = [(0, 60), (0, 40), (20, 40)]

    all = [sand, loamySand, sandyLoam, sandyClayLoam, loam, siltLoam, silt, sandyClay, clayLoam, siltyClayLoam, clay, siltyClay]
    names = ["sand", "loamySand", "sandyLoam", "sandyClayLoam", "loam", "siltLoam", "silt", "sandyClay", "clayLoam", "siltyClayLoam", "clay", "siltyClay"]

class functions():

    # determines if point C is on line segment AB
    def ccw(self, pointA, pointB, pointC):
        return (pointC[1] - pointA[1]) * (pointB[0] - pointA[0]) > (pointB[1] - pointA[1]) * (pointC[0] - pointA[0])

    # determines if line segments AB and CD intersect
    def intersection(self, line1, line2):
        A = line1[0]
        B = line1[1]
        C = line2[0]
        D = line2[1]
        return functions.ccw(self, A, C, D) != functions.ccw(self, B, C, D) and functions.ccw(self, A, B, C) != functions.ccw(self, A, B, D)

    # determines which region a given sample falls under
    def isInside(self, sample):
        sampleX = sample[0]
        sampleY = sample[2]
        tex = textures.all
        texLines = []
        for t in textures.all:
            newPoly = []
            for p in t:
                poly = tex.index(t)
                current = tex[poly].index(p)
                total = len(tex[poly])
                if current + 1 != total:
                    newPoly.append((p, tex[poly][current + 1]))
                else:
                    newPoly.append((p, tex[poly][0]))
            texLines.append(newPoly)
            pCount = 0
        for poly in texLines:
            points = 0
            for line in poly:
                inter = functions.intersection(self, line, [[sampleX, sampleY], [1000, 1000]])
                if inter:
                    points += 1
            if points % 2 != 0:
                return textures.names[pCount]
            pCount += 1


    # takes an integer and gives it an alphabetical label
    def numToLabel (self, value):
        letters = [
            "A", "B", "C", "D", "E",
            "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"
        ]
        text = ""
        valueTemp = -1
        valueTempTemp = -1
        while value > 25:
            valueTemp += 1
            value -= 26
        while valueTemp > 25:
            valueTempTemp += 1
            valueTemp -= 26
        if valueTempTemp >= 0:
            text = text + letters[valueTempTemp]
        if valueTemp >= 0:
            text = text + letters[valueTemp]
        text = text + letters[value]
        return text

    # makes samples fit on an equilateral triangle
    def fixPoints(self):
        samTemp = samples.all
        sam = []
        for s in samTemp:
            y = int((100 - s[2]) * 8)
            x = int(((100 - s[0]) * 8)+(y/2)-400)
            y = int(y*(math.sqrt(3)/2))+50
            sam.append((x, y))
        return sam

    # makes polygons fit on an equilateral triangle
    def fixValues(self):
        texTemp = textures.all
        tex = []
        for t in texTemp:
            pointsTemp = []
            for p in t:
                tNum = texTemp.index(t)
                pNum = texTemp[tNum].index(p)
                y = int((100 - p[1]) * 8)
                x = int(((100 - p[0]) * 8)+(y/2)-400)
                y = int(y*(math.sqrt(3)/2))+50
                pointsTemp.append([x, y])
            tex.append(pointsTemp)
        return tex