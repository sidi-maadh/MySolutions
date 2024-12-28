#include <string>

std::string repeat_str(size_t repeat, const std::string& str) {
  
  std::string result = "";
  for (int i = 0; i < repeat; i++)
  {
    result += str;
  }
  
  return result;
}
