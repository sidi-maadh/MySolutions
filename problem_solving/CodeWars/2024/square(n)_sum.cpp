#include <vector>

int square_sum(const std::vector<int>& numbers)
{
  int result = 0;
  for (auto i : numbers)
  {
    result += i*i;
  }
  
  return result;
}
