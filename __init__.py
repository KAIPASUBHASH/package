def rectangle(length,breadth):
    return length*breadth
def triangle(base,height):
    return (base*height)/2
    
def cube(side):
    return side*side*side
def cuboid(length,breadth,height):
    return length*breadth*height
import geometry.area
import geometry.volume

print("Area of rectangle=" , geometry.area.rectangle(7,9))
print("Area of triangle=",geometry.area.triangle(9,5))

print("Area of cube=",geometry.volume.cube(3))
print("Area of cuboid=",geometry.volume.cuboid (3,4,8))    
