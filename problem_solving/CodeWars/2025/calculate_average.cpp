#include <vector>

double calcAverage(const std::vector<int>& values){

  
  double total = 0;
  
  for(int i : values) {
    total += i;
  }
  return total / values.size();

}
