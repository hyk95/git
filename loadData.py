import os
from Car import Car
from Node import Node
from Road import Road
basic_path = "./config"


def readAllData():
    car_path = os.path.join(basic_path, "car.txt")
    node_paht = os.path.join(basic_path, "cross.txt")
    road_paht = os.path.join(basic_path, "road.txt")
    Cars = []
    Nodes = []
    Roads = []
    with open(car_path, 'r') as car_file:
        for line in car_file.readlines():
            if line[0] == '#':
                continue
            line = [int(x) for x in line.replace("\n", "")[1:-1].split(",")]
            Cars.append(Car(*line))

    with open(node_paht, 'r') as car_file:
        for line in car_file.readlines():
            if line[0] == '#':
                continue
            line = [int(x) for x in line.replace("\n", "")[1:-1].split(",")]
            Nodes.append(Node(line[0], line[1:]))

    with open(road_paht, 'r') as car_file:
        for line in car_file.readlines():
            if line[0] == '#':
                continue
            line = [int(x) for x in line.replace("\n", "")[1:-1].split(",")]
            Roads.append(Road(*line))
    return Cars, Nodes, Roads


if __name__ == '__main__':
    print(readAllData())
