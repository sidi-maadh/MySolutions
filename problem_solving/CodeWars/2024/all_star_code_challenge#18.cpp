#include <string>

unsigned int strCount(const std::string& word, char letter){
  
  int count = 0;
  for (auto i: word)
  {
    if (i == letter) {
      count += 1;
    }
  }
  
  
  return count; 
}
