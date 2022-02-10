function convertToRoman(num) {
    let value = num
    let numerals = ""
  
  while (num > 0){
    console.log("Current value of num: " + num)
    if (num - 1000 >= 0)
    {
      numerals += "M"
      num -= 1000
      console.log("Added 'M'")
      continue;
    }
    if (num - 900 >= 0)
    {
      numerals += "CM"
      num -= 900
      console.log("Added 'CM'")
      continue;
    }  
    if (num - 500 >= 0)
    {
      numerals += "D"
      num -= 500
      console.log("Added 'D'")
      continue;
    }
    if (num - 400 >= 0)
    {
      numerals += "CD"
      num -= 400
      console.log("Added 'CD'")
      continue;
    }
    if (num - 100 >= 0)
    {
      numerals += "C"
      num -= 100
      console.log("Added 'C'")
      continue;
    }
    if (num - 90 >= 0)
    {
      numerals += "XC"
      num -= 90
      console.log("Added 'XC'")
      continue;
    }
    if (num - 50 >= 0)
    {
      numerals += "L"
      num -= 50
      console.log("Added 'L'")
      continue;
    }
    if (num - 40 >=0)
    {
      numerals += "XL"
      num -= 40
      console.log("Added 'XL'")
      continue;
    }
    if (num - 10 >= 0)
    {
      numerals += "X"
      num -= 10
      console.log("Added 'X'")
      continue;
    } 
    if (num - 9 >= 0)
    {
      numerals += "IX"
      num -= 9
      console.log("Added 'IX'")
      continue;
    }
    if (num - 5 >= 0)
    {
      numerals += "V"
      num -= 5
      console.log("Added 'V'")
      continue;
    }
    if (num - 4 >= 0)
    {
      numerals += "IV"
      num -= 4
      console.log("Added 'IV'")
      continue;
    }
    if (num - 1 >= 0)
    {
      numerals += "I"
      num -= 1
      console.log("Added 'I'")
      continue;
    }
  
  }
  console.log("\nFINISHED\nInitial value: " + value + "\nRoman Numeral: " + numerals)
  return numerals
  }
  
  convertToRoman(36);