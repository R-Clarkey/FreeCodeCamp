function telephoneCheck(str) {


    if (str.match(/^[1]? ?([0-9]{3}|\([0-9]{3}\)) ?-?[0-9]{3}-? ?[0-9]{4}$/)){
      console.log("Matches: " + str)
      return true
    }
    else{
      console.log("Doesn't match: " + str)
      return false
    }
  
  }
  
  telephoneCheck("555-555-5555");