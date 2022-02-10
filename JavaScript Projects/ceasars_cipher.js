function rot13(str) {
    let convertedStr = []
    console.log(str)
    
    for (let index in str){
      if (str[index].match(/[a-z]/i)){
        if (str[index].charCodeAt() <=77){
          convertedStr.push(String.fromCharCode(str[index].charCodeAt(str[index]) + 13))
        }
        else if(str[index].charCodeAt() >=78){
          convertedStr.push(String.fromCharCode(str[index].charCodeAt(str[index]) - 13))
        }
      }
      else{
        convertedStr.push(str[index])
      }
    }
  convertedStr = convertedStr.join("")
  console.log(convertedStr)
  return convertedStr
  }
  rot13("SERR PBQR PNZC");