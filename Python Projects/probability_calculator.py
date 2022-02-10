import copy #deepcopy copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.drawn_balls = list()
    self.contents = list()
    for argument in kwargs.items():
      for ball in range(argument[1]):
        self.contents.append(argument[0])
    #print("Sorted balls:",self.contents)

  def draw(self, amount_to_draw):
    if amount_to_draw > len(self.contents):
      return self.contents
    else:
      for iteration in range(amount_to_draw):
        random_index = random.randint(0,(len(self.contents)-1))
        #print("Index picked", random_index)
        self.drawn_balls.append(self.contents[random_index])
        del self.contents[random_index]
      #print("Drawn balls:", self.drawn_balls)
      return self.drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  correct_probability = 0
  for iteration in range(num_experiments):
    #print("\nNext iteration:")
    #print("Predicted balls:", expected_balls)
    copy_of_hat = copy.deepcopy(hat)
    copy_of_expected_balls = copy.deepcopy(expected_balls)
    No_of_balls = copy_of_hat.draw(num_balls_drawn)

    for ball in No_of_balls:
      if ball in copy_of_expected_balls:
        copy_of_expected_balls[ball] -=1

    not_drawn_predicted_ball = False
    for colour, value in copy_of_expected_balls.items():
      #print("Checking expected balls:", colour, value)
      if value > 0:
        not_drawn_predicted_ball = True
    if not_drawn_predicted_ball == False:
      correct_probability += 1
  #print("-"*50)
  #print(correct_probability/num_experiments)
  #print("-"*50)
  return correct_probability/num_experiments


