#include <vector>
int grow(std::vector<int> nums) {
  
  int result = 1;
  for (int i = 0; i < nums.size(); i++)
  {
    result *= nums[i];
  }
  
  return result;
    
}
