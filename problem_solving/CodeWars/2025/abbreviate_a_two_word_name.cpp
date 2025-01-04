#include <string>

std::string abbrevName(std::string name)
{
  std::string result = "";
  
  result = toupper( name[0] );
  result += ".";
  result += toupper( name[ name.find(" ") + 1 ] );
  
  return result;
}
