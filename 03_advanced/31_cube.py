# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

class Object():
   def __init__(self) -> None:
      pass

class Cube():
   def __init__(self) -> None:
      pass

   def translate(self, x, y, z):
      self.print_status("Translate", x, y, z)

   def rotate(self, x, y, z):
      self.print_status("Rotate", x, y, z)

   def scale(self, x, y, z):
      self.print_status("Scale", x, y, z)

   def color(self, r, g, b):
      self.print_status("Color", r, g, b)
   
   def print_status(self, func_name, arg1, arg2, arg3):
      if func_name == "Color":
         print(f"{func_name}:\n -> R: {arg1} | G: {arg2} | B: {arg3}\n")

      else:
         print(f"{func_name}:\n -> x: {arg1} | y: {arg2} | z: {arg3}\n")

   def update_transform(self, ttype:str, value:list):
      if ttype == "Translate":
         self.translate(value)

      elif ttype == "Rotate":
         self.rotate(value)

      elif ttype == "Scale":
         self.scale(value)


cube1 = Cube()
cube2 = Cube()
cube3 = Cube()

cube1.translate(912.432, 554.656, 876.369)
cube1.rotate(5, 0, 37)
cube1.scale(100, 50, 75)
cube1.color(120, 255, 33)
