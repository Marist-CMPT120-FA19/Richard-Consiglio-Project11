import math

class Sphere:
    def __init__(self,radius):
        self.radius = radius
        self.area = 0
        self.volumeR = 0

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r = self.radius         
        self.area = 4 * math.pi * (r * r)            
        return self.area

    def volume(self):
        r = self.radius         
        
        self.volumeR = (4/3) * math.pi * (r * r * r)
        return self.volumeR

def main():
    r = input("Enter the radius of your circle to calculate volume and area: ")
    r = int(r)
    radius = Sphere(r)
    v = radius.volume()
    a = radius.surfaceArea()

    print("The volume is: ", v, "meters cubed")
    print("The area is: ", a, "meters squared")

main()
