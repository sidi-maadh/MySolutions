#include <string>

std::string sum_str(const std::string& a, const std::string& b) {
    
  std::string num1 = a.empty() ? "0" : a;
  std::string num2 = b.empty() ? "0" : b;
  
  int result = 0;
  int n1 = std::stoi(num1);
  int n2 = std::stoi(num2);
    
  result = n1 + n2;
    
  return std::to_string(result);

}
