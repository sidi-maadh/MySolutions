#include <utility>

std::pair<int, int> swap_values(std::pair<int, int> values) {
  
  // Meth 1
  int x = values.first;
  
  values.first = values.second;
  values.second = x;
  
  // Meth 2 : using Function 
  std::swap(values.first, values.second);
  
  return values;

}
