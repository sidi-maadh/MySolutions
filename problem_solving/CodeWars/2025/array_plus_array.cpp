#include <vector>

int arrayPlusArray(std::vector<int> a, std::vector<int> b) {
  
  int arr1 = 0;
  int arr2 = 0;
  
  for ( auto x: a )
  {
    arr1 += x;
  }
  for ( auto y: b)
  {
    arr2 += y;
  }
  
  return arr1 + arr2; // something went wrong
}
