class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    shape = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    for column in range(self.height):
      for row in range(self.width):
        shape += "*"
      shape += "\n"
    return shape

  def get_amount_inside(self, other_shape):
    min_occurences_list = []
    min_occurences_list.append(self.width // other_shape.width)
    min_occurences_list.append(self.height // other_shape.height)
    return min_occurences_list[0]*min_occurences_list[1]

  def __str__(self):
      return (("Rectangle(width={0}, height={1})").format(self.width, self.height))

class Square(Rectangle):

  def __init__(self, length):
    self.width = length
    self.height = length

  def set_side(self,length):
    self.width = length
    self.height = length

  def __str__(self):
    return "Square(side={})".format(self.width)