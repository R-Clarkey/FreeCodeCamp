class Category:

  def __init__(self, name):
      self.name = name
      self.ledger = list()

  def deposit(self, amount, description=""):
    # print("\nRunning 'deposit'")
    self.ledger.append({'amount' : amount, 'description' : description})
    # print("Current values in ledger list:",self.ledger)

  def withdraw(self, amount, description=""):
    # print("\nRunning 'withdraw'")
    if self.check_funds(amount):
      self.ledger.append({'amount' : -amount, 'description' : description})
      # print("Current values of ledger list:",self.ledger)
      return True
    else:
      return False

  def get_balance(self):
    # print("\nRunning 'get_balance'")
    balance = 0
    for value in self.ledger:
      balance += value["amount"]
    # print("Value of balance is:",balance)
    return balance

  def transfer(self, amount, category):
    # print("\nRunning 'transfer'")
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False
      
  def check_funds(self, amount):
    # print("\nRunning 'check_funds'")
    if amount > self.get_balance():
      return False
    else:
      return True


  def __str__(self):
    # print("\nRunning '__str__'")
    asterisks = 30 - len(self.name)
    output = ""
    output += ("*" * (asterisks // 2) + self.name + "*"*(asterisks //2) +"\n")
    for item in self.ledger:
      amount = item["amount"]
      description = item["description"]
      if len(description) > 23:
        description = description[:23]
      output += ("{:<23}{:>7.2f}\n".format(description, amount))
    output += ("Total: " + str(self.get_balance()))
    # print(output)
    return output




def create_spend_chart(categories):
  print("\n\n")
  print("_"*50)
  print()
  output = ""
  total_spending = 0
  output += "Percentage spent by category\n"
  print("Categories:")
  for category in categories:
    print("Category:", category.name)
    print("Category ledger:", category.ledger)
    for value in category.ledger:
      #print(value["amount"])
      if value["amount"] < 0:
        total_spending += value["amount"]
  print("\n")
  total_spending = str(total_spending)
  total_spending = total_spending[1:]
  total_spending = round(float(total_spending),2)
  print("TOTAL SPENDING of categories", total_spending)
  print("\n")
  for row in range(100,-10,-10):
    #print("Value of row", row)
    output += ("{:>3}| ".format(row))
    for category in categories:
      category_spending = 0
      for value in category.ledger:
        if value["amount"] < 0:
          category_spending += value["amount"]
      category_spending = str(category_spending)
      category_spending = category_spending[1:]
      category_spending = round(float(category_spending),2) 
      category_percentage = round(((category_spending/total_spending)*100))
      #print("Currently on:", category.name, "with percentage value of", category_percentage, "%")

      if category_percentage >= row:
        output += "o  "
      else:
        output += "   "


    output += "\n"
  output += (4*" ")
  output += "-"
  finding_longest_list = []
  for category in categories:
    output += 3*"-"
    finding_longest_list.append(len(category.name))
  output += "\n"

  for printingChr in range(max(finding_longest_list)):
    output += (" "*5)
    for category in categories:
      try:
        output += category.name[printingChr]
        output += "  "
      except:
        output += (" "*3)
    if printingChr != max(finding_longest_list)-1:
      output += "\n"



  print(output)
  print()
  return output











