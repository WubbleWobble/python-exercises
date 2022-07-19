# 1. Write a class called Rect that models a rectangle, taking and storing 
#    its width and height, so that the following tests pass

my_rect1 = Rect(5, 10)
assert my_rect1.width == 5
assert my_rect1.height == 10

# 2. Add a method called area() that calculates the rectangle's area, so that the following
#    tests pass

my_rect2 = Rect(7, 8)
my_rect3 = Rect(3, 4)
assert my_rect2.area() == 56
assert my_rect3.area() == 12

# 3. Add a method called perimeter() that calculates the rectangle's perimeter, so that the
#    following tests pass

my_rect4 = Rect(10, 5)
my_rect5 = Rect(3, 6)
assert my_rect4.perimeter() == 30
assert my_rect5.perimeter() == 18
