#include <string>

using namespace std; 

string sliceString (string str )
{
  
  string result = "";
  for (int i = 1; i < str.length() - 1; i++)
  {
    result += str[i];
  }

  return result ; 
}
