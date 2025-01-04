#include <string>

std::string makeUpperCase (const std::string& input_str)
{
  std::string result = "";
  
  for (auto i: input_str)
  {
    result += toupper(i);
  }
  
  return result;
}
