#include <string>

std::string correct(std::string str){
    
  for ( int i = 0; i < str.length(); i++ )
  {
    if ( str[i] == '0') {
      str[i] = 'O';
    }
      
    else if ( str[i] == '1' ) {
      str[i] = 'I';
    }
      
    else if ( str[i] == '5' ) {
      str[i] = 'S';
    }
  }
  
  return str;
}
