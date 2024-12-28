#include <string>

std::string no_space(const std::string& x)
{
  
  std::string result = "";
  for (int i = 0; i < x.length(); i++)
  {
    if (x[i] != ' '){
      result += x[i];
    }
  }
  
  return result;
}
