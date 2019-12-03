from collections import namedtuple

Point = namedtuple('Point',['x','y'])

class Path:
    def __init__(self):
        self.path = [Point(0,0)]

    def __repr__(self):
        return ', '.join([str(point) for point in self.path])

    def go_right(self,steps):
        current_point = self.path[-1]
        for step in range(1,steps+1):
            new_point = Point(current_point.x + step,current_point.y)
            self.path.append(new_point)

    def go_left(self, steps):
        current_point = self.path[-1]
        for step in range(1,steps+1):
            new_point = Point(current_point.x - step, current_point.y)
            self.path.append(new_point)

    def go_up(self, steps):
        current_point = self.path[-1]
        for step in range(1, steps+1):
            new_point = Point(current_point.x, current_point.y + step)
            self.path.append(new_point)

    def go_down(self, steps):
        current_point = self.path[-1]
        for step in range(1, steps+1):
            new_point = Point(current_point.x, current_point.y - step)
            self.path.append(new_point)

    def intersection_points(self, other_path):
        intersection_points = list()
        for point in other_path.path[1:]:
            if point in self.path:
                intersection_points.append(point)
        return intersection_points

    def create_path(self, listing):
        for instruction in listing:
            direction = instruction[0]
            steps = int(instruction[1:])

            if direction == "R":
                self.go_right(steps)
            elif direction == "L":
                self.go_left(steps)
            elif direction == "U":
                self.go_up(steps)
            elif direction == "D":
                self.go_down(steps)

def calculate_distance(point):
    return int(point.x + point.y)

def main():
    
    path_listing = []
    with open('input.txt','r') as fInput:
        for line in fInput.readlines():
            path_listing.append(line.strip().split(','))

    wire_one = Path()
    wire_two = Path()

    wire_one.create_path(path_listing[0])
    wire_two.create_path(path_listing[1])

    intersections = wire_one.intersection_points(wire_two)

    minimum_distance = calculate_distance(intersections[0])

    for intersection in intersections[1:]:
        distance = calculate_distance(intersection)
        if distance < minimum_distance:
            print(intersection)
            minimum_distance = distance

    print(f"Least distance: {minimum_distance}")
 
if __name__ == '__main__':
    main()

