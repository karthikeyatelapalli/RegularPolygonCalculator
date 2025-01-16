
# N-sided Polygon class definition and main function
'''
The RegularPolygon class is defined in this Python code, and the main method asks the user to input the polygon's
 number of sides and side lengths. The software then computes and displays the polygon's area and perimeter.
'''

import math
# Define the RegularPolygon class
class RegularPolygon:
    def __init__(self):
        self._num_sides = 0  # Number of sides
        self._side_len = 0.0  # Length of each side
        
    def set_num_sides(self, ns):
        self._num_sides = ns
        
    def set_side_len(self, sl):
        self._side_len = sl
        
    def get_num_sides(self):
        return self._num_sides
        
    def get_side_len(self):
        return self._side_len
    
    def perimeter(self):
        return self._num_sides * self._side_len
    # Calculates the area of the polygon
    def area(self):
        return (self._num_sides * self._side_len**2) / (4 * math.tan(math.pi/self._num_sides))
# Define the main function
def main():
    poly = RegularPolygon()
    # Asks the user to enter the number of sides
    ns = int(input("Enter the number of sides (>=3): "))
    while ns < 3:
        ns = int(input("Invalid entry. Re-enter the number of sides (>=3): "))
    poly.set_num_sides(ns)
    sl = float(input("Enter the length of each side (>= 0.1): "))
    while sl < 0.1:
        sl = float(input("Invalid entry. Re-enter the length of each sides (>= 0.1): "))
    poly.set_side_len(sl)
    print("The polygon has", poly.get_num_sides(), "sides. Each side is", poly.get_side_len(), "units in length.")
    print("The perimeter of the polygon is {:.3f} units and its area is {:.3f} square units.".format(poly.perimeter(), poly.area()))

if __name__ == "__main__":
    main()
