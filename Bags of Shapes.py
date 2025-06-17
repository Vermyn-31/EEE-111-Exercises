import math

# TODO: Set password here
test_pass = 'tatsulok_3'

# No need to change or amend this class!
class Shape:
    shape_type = 'shape'

    def __init__(self, **kwargs):
        self.area = 0
        
        self.perimeter = kwargs['perimeter'] if 'perimeter' in kwargs else 0
        self.area = kwargs['area'] if 'area' in kwargs else 0
        self.name = kwargs['name'] if 'name' in kwargs else 'shape'

    def __str__(self):
        return f'<Shape name={self.name} type={self.shape_type}>'

# No need to change or amend this class!
class Point(Shape):
    shape_type = 'point'

    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)

        self.x = x
        self.y = y

    def __setitem__(self, idx, val):
        if idx == 0:
            self.x = val
        elif idx == 1:
            self.y = val
        else:
            raise IndexError('Out of bounds')

    def __getitem__(self, idx):
        if idx == 0:
            return self.x
        elif idx == 1:
            return self.y
        else:
            raise IndexError('Out of bounds')

    def __str__(self):
        return f'({self.x}, {self.y})'

# FIXME: Fill in class Vector2D below
class Vector2D(Point):
    shape_type = 'vec2d'
    
    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)
    
    # Somebody has filled-in this part. :O
    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)

        self.perimeter = math.dist((x, y), (0, 0))
    
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return self + (other)
        elif type(other) is tuple or type(other) is list:
            return self + Vector2D(other[0], other[1])
    
    # Somebody has filled-in this part too! :O
    def __sub__(self, other):
          # Type dispatch
        if isinstance(other, Vector2D):
            return self + (-other)
        elif type(other) is tuple or type(other) is list:
            return self + Vector2D(-other[0], -other[1])
      
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    
    def __str__(self):
        return f'<{self.x}, {self.y}>'
    
    # ... and this one! :O
    def det(self, other):
        return self.x * other.y - self.y * other.x
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y

# FIXME: Fill in class LineSegment below
class LineSegment(Shape):
    shape_type = 'line_seg'
    
    # Who has been filling these parts? :O
    def __init__(self, start, end, **kwargs):
        super().__init__(**kwargs)

        # Type coercion
        if type(start) is tuple or type(start) is list:
            start = Point(start[0], start[1])
            
        if type(end) is tuple or type(end) is list:
            end = Point(end[0], end[1])
        
        self.start = start
        self.end = end
        self.perimeter = math.dist(self.start, self.end)
    
    def vector(self):
        return Vector2D(self.end.x - self.start.x, self.end.y - self.start.y)
    
    def __str__(self):
        return f"({self.start.x}, {self.start.y}) -> ({self.end.x}, {self.end.y})"
      
# FIXME: Amend class Polygon below
# Feel free to add more methods inside this
class Polygon(Shape):
    shape_type = 'poly'
    
    def __init__(self, points_list, **kwargs):
        super().__init__(**kwargs)
        self.points_list = points_list
        
        perimeter = 0
        for i in range(len(points_list)):
            p1 = self.points_list[i]
            p2 = self.points_list[(i + 1) % len(self.points_list)]
            perimeter += LineSegment(p1, p2).perimeter
        
        self.perimeter = perimeter
        
        
        area = 0
        if self.points_list[0] != self.points_list[-1]:
            self.points_list = self.points_list + self.points_list[:1]
        x = [ p[0] for p in self.points_list]
        y = [ p[1] for p in self.points_list]
        s = 0
        for i in range(len(self.points_list) - 1):
            s += x[i]*y[i+1] - x[i+1]*y[i]
            
        area = s/2
        self.area = abs(area)

# FIXME: Amend class BagOfShapes below
class BagOfShapes:
    # Stop helping the newbie, creepy code hacker! >:(
    def __init__(self, shapes=None, name='bag_of_shapes'):
        self.shapes = {} if type(shapes) is not dict else shapes
        self.name = name
    
    def add(self, shape):
        self.shapes[shape.name] = shape

    def remove(self, name):
        del self.shapes[name]

    def total_area(self):
        total_area = 0.0
        for shape in self.shapes.values():
            total_area += shape.area
        return total_area

    def total_perimeter(self):
        total_perimeter = 0.0
        for shape in self.shapes.values():
            total_perimeter += shape.perimeter
        return total_perimeter

    def __add__(self, other):
        new_bag = BagOfShapes(self.name + other.name)
        for shape in self.shapes.values():
            new_bag.add(shape)
        for shape in other.shapes.values():
            new_bag.add(shape)
        return new_bag

    def __len__(self):
        return len(self.shapes)

    def __getitem__(self, key):
        return self.shapes[key]

    def __setitem__(self, key, val):
        self.shapes[key] = val

    def __contains__(self, item):
        return item in self.shapes

# TODO: Add any additional class(es) below this comment
class Triangle(Polygon):
    shape_type = 'tri'
    def __init__(self, points_list, **kwargs):
        super().__init__(points_list, **kwargs)
        self.points_list = points_list.copy()

    def angle_type(self):
        sum_dist = []
        d1 = math.dist(self.points_list[-1],self.points_list[0])
        sum_dist.append(d1)
        d2 = math.dist(self.points_list[0],self.points_list[1])
        sum_dist.append(d2)
        d3 = math.dist(self.points_list[1],self.points_list[2])
        sum_dist.append(d3)
        
        c = max(sum_dist)
        sum_dist.remove(c)
        
        a = sum_dist[0]
        b = sum_dist[1]
        c = round(math.pow(c,2),2)
        if (math.pow(a,2) + math.pow(b,2)) == c:
            return 0
        elif (math.pow(a,2) + math.pow(b,2)) < c:
            return 1
        elif (math.pow(a,2) + math.pow(b,2)) > c:
            return -1
        
# NOTE: Do not change anything inside this main() function to
# make your life easier. :>
def main():
    n_testcases = int(input())

    for t in range(n_testcases):
        shape_bags = {}

        print(f'Case #{t + 1}:')

        n_commands = int(input())
        current_bag_key = ''

        for _ in range(n_commands):
            cmd_line = input().split()
            cmd = cmd_line[0]

            if cmd == 'create_bag':
                # CMD: create_bag bag_a
                # Create a BagOfShapes with name bag_a
                shape_bags[cmd_line[1]] = BagOfShapes(name=cmd_line[1])

                print(f'Create bag {cmd_line[1]}')
            elif cmd == 'select_bag':
                # CMD: select_bag bag_a
                # Select the BagOfShapes bag_a to manipulate
                current_bag_key = cmd_line[1]

                print(f'Select bag {cmd_line[1]}')
            elif cmd == 'bags_add':
                # CMD: bags_add bag_c bag_b bag_a
                # Merge BagOfShapes bag_b and bag_a, and that resulting
                # bag will become bag_c
                dest = cmd_line[1]
                a, b = cmd_line[2], cmd_line[3]

                shape_bags[dest] = shape_bags[a] + shape_bags[b]
                shape_bags[dest].name = dest

                print(f'Add bags {dest} <- {a} + {b}')
            elif cmd == 'add':
                # CMD: add shape_type shape_name args
                # Add a Shape of type shape_type and name shape_name to
                # the currently selected BagOfShapes. args contain the
                # parameters to the shapes for initialization.
                shape_type, shape_name = cmd_line[1], cmd_line[2]
                shape_args = [int(x) for x in cmd_line[3:]]
                shape = None

                if shape_type == 'point':
                    # ARGS: x y
                    # x and y coordinates of the Point
                    shape = Point(shape_args[0], shape_args[1], name=shape_name)
                elif shape_type == 'vec2d':
                    # ARGS: x y
                    # x and y coordinates of the Vector2D
                    shape = Vector2D(shape_args[0], shape_args[1], name=shape_name)
                elif shape_type == 'line_seg':
                    # ARGS: s_x s_y e_x e_y
                    # LineSegment with start Point s and end Point e
                    shape = LineSegment((shape_args[0], shape_args[1]), (shape_args[2], shape_args[3]), name=shape_name)
                elif shape_type == 'poly':
                    # ARGS: n x_0 y_0 x_1 y_1 ... x_n y_n
                    # List of n Points
                    # It is not guaranteed that the points are listed in
                    # ccw order
                    points_list = [Point(a, b) for a, b in zip(shape_args[1::2], shape_args[2::2])]
                    
                    shape = Polygon(points_list, name=shape_name)
                elif shape_type == 'tri' and 'Triangle' in globals():
                    # ARGS: x_0 y_0 x_1 y_1 x_2 y_2
                    # List of three Points forming a Triangle
                    # It is not guaranteed that the points are listed in
                    # ccw order
                    points_list = [Point(a, b) for a, b in zip(shape_args[0::2], shape_args[1::2])]

                    shape = Triangle(points_list, name=shape_name)
                elif shape_type == 'quad' and 'Quad' in globals():
                    # ARGS: x_0 y_0 x_1 y_1 x_2 y_2 x_3 y_3
                    # List of four Points forming a Quadrilateral
                    # It is not guaranteed that the points are listed in
                    # ccw order
                    points_list = [Point(a, b) for a, b in zip(shape_args[0::2], shape_args[1::2])]

                    shape = Quad(points_list, name=shape_name)
                elif shape_type == 'ellipse' and 'Ellipse' in globals():
                    # ARGS: a b
                    # Length of semi-major and minor axes, respectively
                    shape = Ellipse(shape_args[0], shape_args[1], name=shape_name)

                if isinstance(shape, Shape):
                    shape_bags[current_bag_key].add(shape)

                    print(f'Add shape {shape.name} of type {shape.shape_type} into bag {current_bag_key}')
                else:
                    print(f'Add shape None')
            elif cmd == 'remove':
                # CMD: remove shape_name
                # Remove a Shape with name shape_name from the
                # currently selected BagOfShapes
                shape_name = cmd_line[1]

                if shape_name in shape_bags[current_bag_key]:
                    shape_bags[current_bag_key].remove(shape_name)

                    print(f'Remove shape {cmd_line[1]} from bag {current_bag_key}')
                else:
                    print('Remove shape None')
            elif cmd == 'get':
                # CMD: get shape_name
                # Get a Shape with name shape_name from the
                # currently selected BagOfShapes
                shape_name = cmd_line[1]
                val = None

                if shape_name in shape_bags[current_bag_key]:
                    val = shape_bags[current_bag_key][shape_name]

                print(f'{shape_name}: {val}')
            elif cmd == 'get_shape_prop':
                # CMD: get_shape_prop shape_name shape_prop
                # Get Shape property shape_prop of Shape with name shape_name
                # from the currently selected BagOfShapes
                shape_name, prop_name = cmd_line[1], cmd_line[2]
                val = None

                if shape_name in shape_bags[current_bag_key]:
                    shape = shape_bags[current_bag_key][shape_name]
                    val = getattr(shape, prop_name)

                    if type(val) is float:
                        val = f'{val:.02f}'

                print(f'{shape_name}.{prop_name}: {val}')
            elif cmd == 'exec_shape_method':
                # CMD: exec_shape_method shape_name shape_method
                # Execute Shape method shape_method of Shape with name shape_name
                # from the currently selected BagOfShapes
                shape_name, method_name = cmd_line[1], cmd_line[2]
                val = None

                if shape_name in shape_bags[current_bag_key]:
                    shape = shape_bags[current_bag_key][shape_name]
                    val = getattr(shape, method_name)()

                    if type(val) is float:
                        val = f'{val:.02f}'

                print(f'{shape_name}.{method_name}(): {val}')
            elif len(current_bag_key) > 0:
                if cmd == 'len':
                    # CMD: len
                    # Get size of the currently selected BagOfShapes
                    print(f'Bag {current_bag_key} size: {len(shape_bags[current_bag_key])}')
                elif cmd == 'total_area':
                    # CMD: total_area
                    # Get total area of the currently selected BagOfShapes
                    print(f'Bag {current_bag_key} area: {shape_bags[current_bag_key].total_area():.2f}')
                elif cmd == 'total_perimeter':
                    # CMD: total_perimeter
                    # Get total perimeter of the currently selected BagOfShapes
                    print(f'Bag {current_bag_key} perimeter: {shape_bags[current_bag_key].total_perimeter():.2f}')

if __name__ == '__main__':
    main()
