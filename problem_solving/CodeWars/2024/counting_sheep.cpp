#include <vector>

using namespace std; 

int count_sheep(vector<bool> arr) 
{
  
  int count = 0;
  for ( auto i : arr ) 
  {
    if ( i != 0)
    {
      count += 1;
    }
  }
  
  return count;
}

