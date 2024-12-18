bool isDivisible(int n, int x, int y) {

  // 1. Using if Condiction
  if ( n % x == 0 && n % y == 0 ) {
    return true ;
  }
  else {
    return false ;
  }

  // 2. Using Ternary Conditional
  return n % x == 0 && n % y == 0 ? true : false ;
}
