function palindrome(str) {
    console.log("Initial value of string: " + str)
    str = str.replace(/[.,\/#!$%\^&\*;:{|}=\-_`~()]/g,"")
    console.log("String after punctuation removal: " + str)
    str = str.split("")
  
    // 0_0 (: /- :) 0-0
    for (let index in str){
      if (str[index] === " "){
        console.log("   Index of space in string: " + [index])
        str.splice(index,1)
        
      }
    }
    str = str.join("")
    let reverseStr = []
  
    for (let index = str.length -1;index >= 0 ;index--){
      reverseStr.push(str[index])
    }
      reverseStr = reverseStr.join("")
      console.log("Value of str: " + str)
      console.log("Value of reverseStr: " + reverseStr)
  
      if (str.toLowerCase() === reverseStr.toLowerCase()){
        console.log(" MATCHES \n")
        return true
      }
      else{
        console.log(" FAILED \n")
        return false
      }
  }

  palindrome("racecar")