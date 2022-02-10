import re

def arithmetic_arranger(problems, display_answers=False):

  # print("Number of Problems:", len(problems))
  # print("List of Problems:", problems, "\n")

  if len(problems)>5:
    return "Error: Too many problems."

  line_one = ""
  line_two = ""
  line_three = ""
  line_four = ""
  space_between_problems = 4*" "

  for problem in problems:
    positions = problem.split(" ")
    first_value = positions[0]
    operator = positions[1]
    second_value = positions[2]

# START OF CHECKING RULES
    if operator != "+":
      if operator != "-":
        return "Error: Operator must be '+' or '-'."
    if re.search('[a-z]', first_value, re.IGNORECASE) != None:
      return "Error: Numbers must only contain digits."
    if re.search('[a-z]', second_value, re.IGNORECASE) != None:
      return "Error: Numbers must only contain digits."
    if len(first_value) > 4:
      return "Error: Numbers cannot be more than four digits."
    if len(second_value) > 4:
      return "Error: Numbers cannot be more than four digits."
# END OF CHECHING RULES

    # print("First Value:", first_value, "Operator:", operator, "Second Value:", second_value)
   
    if operator == "+":
      result = int(first_value) + int(second_value)
    if operator == "-":
      result = int(first_value) - int(second_value)

# DISPLAYS ANSWERS IF SECOND ARGUMENT IS TRUE
    if display_answers:
      if problem == problems[-1]:
        # print("Result:", result)
        longest_answer = max( len(str(first_value)), len(str(second_value)) )
        longest_answer = longest_answer + 2
        # print("Problem Length", longest_answer)
        line_one += ((longest_answer - len(first_value)) * " ") + first_value

        line_two += operator + " "
        line_two += (((longest_answer -2) - len(second_value)) * " ") + second_value

        line_three += (longest_answer*"-")

        line_four += ((longest_answer - len(str(result))) * " ") + str(result)


      else:
        # print("Result:", result)
        longest_answer = max( len(str(first_value)), len(str(second_value)) )
        longest_answer = longest_answer + 2
        # print("Problem Length", longest_answer)
        line_one += ((longest_answer - len(first_value)) * " ") + first_value
        line_one += space_between_problems

        line_two += operator + " "
        line_two += (((longest_answer -2) - len(second_value)) * " ") + second_value
        line_two += space_between_problems

        line_three += (longest_answer*"-")
        line_three += space_between_problems

        line_four += ((longest_answer - len(str(result))) * " ") + str(result)
        line_four += space_between_problems


# DISPLAYS PROBLEMS WITHOUT ANSWERS IF THERE ISN'T SECOND ARGUMENT
    else:
      if problem == problems[-1]:
        # print("Result:", result)
        longest_answer = max( len(str(first_value)), len(str(second_value)) )
        longest_answer = longest_answer + 2
        # print("Problem Length", longest_answer)
        line_one += ((longest_answer - len(first_value)) * " ") + first_value

        line_two += operator + " "
        line_two += (((longest_answer -2) - len(second_value)) * " ") + second_value

        line_three += (longest_answer*"-")

      else:
        # print("Result:", result)
        longest_answer = max( len(str(first_value)), len(str(second_value)) )
        longest_answer = longest_answer + 2
        # print("Problem Length", longest_answer)
        line_one += ((longest_answer - len(first_value)) * " ") + first_value
        line_one += space_between_problems

        line_two += operator + " "
        line_two += (((longest_answer -2) - len(second_value)) * " ") + second_value
        line_two += space_between_problems

        line_three += (longest_answer*"-")
        line_three += space_between_problems

  # print(line_one)
  # print(line_two)
  # print(line_three)
  # print(line_four)

  if display_answers:
    output = line_one + "\n" + line_two + "\n" + line_three + "\n" + line_four
  else: 
    output = line_one + "\n" + line_two + "\n" + line_three
  print(output)
  return output
