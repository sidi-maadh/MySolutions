#include <cmath>

int centuryFromYear ( int year ) {
  
  // 1. Using if Condition :
  if ( year % 100 == 0 ) {
    
    return year / 100 ;
    
  }
  else {
    
    return year / 100 + 1 ;
    
  }
  
  // 2. Using Ternary Condition ;
  return year % 100 == 0 ? year / 100 : year / 100 + 1;

  // 3. Using Ceil Methode ;
  return std::ceil( year / 100 ) ;

}
