import math

class Rectangle:
  width = 0
  height = 0
  def __init__(self,w,h):
    self.width = w
    self.height = h

  def set_width(self,w):
    self.width = w

  def set_height(self,h):
    self.height = h
    
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    str = ''
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    for i in range(0,self.height):
      str += '*'*self.width + '\n'
    return str  

  def get_amount_inside(self, shape ):
    if shape.width > self.width or shape.height > self.height:
      return 0
    return math.floor((self.width / shape.width ) * (self.height / shape.height ))

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    

class Square(Rectangle):

  def __init__(self,l):
    self.width = l
    self.height = l

  def set_side(self,l):
    self.width = l
    self.height = l

  def set_width(self,l):
    self.set_side(l)

  def set_height(self,l):
    self.set_side(l)

  def __str__(self):
    return f"Square(side={self.width})"
