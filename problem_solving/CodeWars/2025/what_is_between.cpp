#include <vector>

std::vector<int> between(int start, int end) {

  std::vector<int> nums;
  
  for ( int i = start; i <= end; i++ ) 
  {
    nums.push_back(i);
  }
  
  return nums;

}  
