class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
  def set_width(self,width):
    self.width=width
  def set_height(self,height):
    self.height=height
  def get_area(self):
    return self.width*self.height
  def get_perimeter(self):
    return 2*self.width+2*self.height
  def get_diagonal(self):
    return(self.width**2+self.height**2)**0.5
  def get_picture(self):
    if self.width<=50 and self.height<=50:
      lines=''
      for val in range(self.height):
        for val in range(self.width):
          lines=lines+'*'
        lines=lines+'\n'
      return lines
    else:
      return "Too big for picture."
  def get_amount_inside(self,other_shape):
    capacity=int(self.get_area()/other_shape.get_area())
    return capacity
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
  def __init__(self,side):
    super().__init__(side,side)

  def set_side(self,side):
    self.width = side
    self.height = side

  def set_width(self,width):
    self.width=width
    self.height=width

  def set_height(self, height):
    self.width=height
    self.height=height 

  def __str__(self):
    return f"Square(side={self.width})"
