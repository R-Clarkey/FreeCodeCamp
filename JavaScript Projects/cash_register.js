function checkCashRegister(price, cash, cid) 

{

  let status;
  let cashRegisterTotal = 0;
  let change = [];
  let changeValue;
  let changeList = 
  {
  'ONE HUNDRED': 100.00, 'TWENTY': 20.00,  'TEN': 10.00 , 'FIVE': 5.00,
  'ONE': 1.00, 'QUARTER': .25, 'DIME': 0.10, 'NICKEL': 0.50, 'PENNY': .01
  };

  changeValue = cash-price



  for (let index = cid.length -1; index >=0; index--)
  {
    cashRegisterTotal += cid[index][1]
  }
//   console.log("\nTotal Change Required: $"+changeValue)
//   console.log("Total Amount Of Money In Till: $"+cashRegisterTotal.toFixed(2))

  if (changeValue == cashRegisterTotal.toFixed(2))
  {
    // console.log({status: "CLOSED", change: cid})
    return {status: "CLOSED", change: cid}
  }

  if (changeValue > cashRegisterTotal)
  {
    // console.log({status: "INSUFFICIENT_FUNDS", change: []})
    return {status: "INSUFFICIENT_FUNDS", change: []}
  }

    for (let index = cid.length -1; index >=0; index--)
  {
    // console.log("Index",index,"Checking:",cid[index])
    // console.log("Currency Unit",cid[index][0],"Value:",cid[index][1])
    while (changeValue > 0 && cid[index][1] > 0 && changeValue - changeList[cid[index][0]] >= 0)
    {
        changeValue = changeValue.toFixed(2)
      let roundedChange = changeValue
      // console.log(roundedChange)
      // console.log("Change Required: $"+changeValue.toFixed(2))
      // console.log("Current Currency Unit:",cid[index][0])
      // console.log(change.length)
      if (change.length == 0)
      {
        // console.log("Empty List")
        changeValue -= changeList[cid[index][0]]
        change.push([cid[index][0], changeList[cid[index][0]]])
        cid[index][1] = cid[index][1] - changeList[cid[index][0]]
        // console.log("Change Required After Subtraction: $"+changeValue)
        // console.log("Change Output",change,"\n")
      }
      else
      {
        let currencyInList = false
        for (let currencyUnit in change)
        {
          if (change[currencyUnit][0] == cid[index][0])
          {
            currencyInList = true
          }
        }
        if (currencyInList) // CURRENT CURRENCY UNIT ALREADY EXISTS
        {
          for (let currencyUnit in change)
          {
            if (change[currencyUnit][0] == cid[index][0])
            {
            changeValue -= changeList[cid[index][0]] 
            // console.log(changeValue)
            change[currencyUnit][1] = change[currencyUnit][1] + changeList[cid[index][0]]
            cid[index][1] = cid[index][1] - changeList[cid[index][0]]
            // console.log("Change Required After Subtraction: $"+changeValue)
            // console.log("Change Output",change,"\n")
            }
          }
        }
        else
        {
        changeValue -= changeList[cid[index][0]]
        change.push([cid[index][0], changeList[cid[index][0]]])
        cid[index][1] = cid[index][1] - changeList[cid[index][0]]
        // console.log("Change Required After Subtraction: $"+changeValue)
        // console.log("Change Output",change,"\n")
        }
      }
    } // WHILE END
  } // LOOP FOR CASH REGISTER    

    if (changeValue == 0) // ENOUGH CHANGE IN TILL
    {
      console.log({status: "OPEN", change: change})
      return {status: "OPEN", change: change}
    }
    else // MONEY IN TILL CANNOT MAKE UP CHANGE
    {
      console.log({status: "INSUFFICIENT_FUNDS", change: []})
      return {status: "INSUFFICIENT_FUNDS", change: []}
    }
}




checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);