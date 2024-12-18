function simpleMultiplication(number) {
  
  // 1. Using if Condition :
  if (number %2 == 0){
      return number * 8;
    }
  else {
    return number * 9;
  }
  
  // 2. Using Ternary Condition ;
  return number %2 == 0 ? number * 8 : number * 9;
  
}
