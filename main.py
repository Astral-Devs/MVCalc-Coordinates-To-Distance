from math import cos, sin, acos, pi, sqrt
import csv


# converts the latitude and longitude into spherical coordinates
def toSphereCoords(city):
    # splits the latitude and longitude
    phiArr = city[0].split(" ")
    thetaArr = city[1].split(" ")

    # check to see the direction and figure out theta and phi based on that
    if phiArr[2] == "S":
        phi = (int(phiArr[0]) + float(phiArr[1]) / 60) + 90
    else:
        phi = 90 - (int(phiArr[0]) + float(phiArr[1]) / 60)

    if thetaArr[2] == "W":
        theta = (int(thetaArr[0]) + float(thetaArr[1]) / 60) * (-1)
    else:
        theta = int(thetaArr[0]) + float(thetaArr[1]) / 60

    # returns the spherical coordinates
    return [3961, theta, phi]

def toSphereCoordsNormal(city):
    phiArr = city[0].split(" ")
    thetaArr = city[1].split(" ")

    if phiArr[1] == "S":
        phi = (float(phiArr[0])) + 90
    else:
        phi = 90 - (float(phiArr[0]))

    if thetaArr[1] == "W":
        theta = float(thetaArr[0]) * (-1)
    else:
        theta = float(thetaArr[0])

    # returns the spherical coordinates
    return [3961, theta, phi]


# Takes the spherical coordinates and transfers them to rectangular coordinates
def toRectCoords(sphereCoords):
    r = sphereCoords[0] # takes the radius
    theta = sphereCoords[1] * pi / 180 # converts theta into radians
    phi = sphereCoords[2] * pi / 180 # converts phi into radians

    # calculates the value of x, y, and z
    # sin and cos only accept radian values
    x = r * (sin(phi)) * (cos(theta))
    y = r * (sin(phi)) * (sin(theta))
    z = r * (cos(phi))

    # returns the rectangular coordinates
    return [x, y, z]


def calcAngle(city1, city2):
    # dots the two position vectors together
    #     dot = (city1[0] * city2[0]) + (city1[1] * city2[1]) + (city1[2] * city2[2])

    dot = 0
    for i in range (3):
        dot += city1[i]*city2[i]

    # converts the data into an angle
    angle = acos(dot / (pow(3961,2)))

    # converts angle into degrees
    angle = angle * 180 / pi

    # returns angle
    return angle


def calcDist(angle):
    # calculates the distance
    return 3961 * (angle * pi / 180)


# a list of all the cites, paired up to indicate which ones should be added
citiesListMins = [[["41 50 N", "87 37 W", "Chicago"], ["48 48 N", "2 20 E", "Paris"]],
              [["40 47 N", "73 58 W", "New York"], ["25 46 N", "80 12 W", "Miami"]],
              [["37 47 N", "122 26 W", "San Francisco"], ["12 0 S", "77 2 W", "Lima"]],
              [["42 21 N", "71 5 W", "Boston"], ["37 47 S", "144 58 E", "Melbourne"]]]

citiesListCoords = [[["29.4241 N","98.4936 W","San Antonio"],["47.6062 N","122.3321 W","Seattle"]],
                    [["33.4489 S","70.6693 W","Santiago"],["31.2304 N","121.4737 E", "Shanghai"]]
                    ]



city1Data = ["city", "sphericalCoords", "rectCoords"]
city2Data = ["city", "sphericalCoords", "rectCoords"]
currData = ["angle", "distance"]
element = ["city1", "city2", "data"]

# runs through the list of cities and print out the results
for pair in citiesListMins:
    city1Data[0] = pair[0][2]
    city2Data[0] = pair[1][2]

    city1Sphere = toSphereCoords(pair[0])
    city2Sphere = toSphereCoords(pair[1])
    city1Data[1] = city1Sphere
    city2Data[1] = city2Sphere

    city1Rect = toRectCoords(city1Sphere)
    city2Rect = toRectCoords(city2Sphere)
    city1Data[2] = city1Rect
    city2Data[2] = city2Rect

    angle = calcAngle(city1Rect, city2Rect)
    dist = calcDist(angle)
    currData[0] = angle
    currData[1] = dist

    element[0] = city1Data
    element[1] = city2Data
    element[2] = currData
    print(city1Data)
    print(city2Data)
    print("Distance: " + str(dist) + " Angle: " + str(angle))

for pair in citiesListCoords:
    city1Data[0] = pair[0][2]
    city2Data[0] = pair[1][2]

    city1Sphere = toSphereCoordsNormal(pair[0])
    city2Sphere = toSphereCoordsNormal(pair[1])
    city1Data[1] = city1Sphere
    city2Data[1] = city2Sphere

    city1Rect = toRectCoords(city1Sphere)
    city2Rect = toRectCoords(city2Sphere)
    city1Data[2] = city1Rect
    city2Data[2] = city2Rect

    angle = calcAngle(city1Rect, city2Rect)
    dist = calcDist(angle)
    currData[0] = angle
    currData[1] = dist

    element[0] = city1Data
    element[1] = city2Data
    element[2] = currData
    print(city1Data)
    print(city2Data)
    print("Distance: " + str(dist) + " Angle: " + str(angle))

print(11718.657277828788/500)
print(11718.657277828788//500)
print((11718.657277828788%500)/500*60)