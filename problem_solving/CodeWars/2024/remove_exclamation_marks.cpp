#include <string>

std::string removeExclamationMarks(std::string str) {
  std::string clean = "";
  for (int i = 0; i < str.length(); i++)
  {
    if (str[i] != '!')
    {
      clean += str[i];
    }
  }
  return clean;
}
