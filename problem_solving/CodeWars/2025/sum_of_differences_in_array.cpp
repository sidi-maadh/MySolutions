#include <vector>
#include <algorithm>

using namespace std;

int sumOfDifferences(vector<int> arr) {
    int result = 0;
  
    sort( arr.rbegin(), arr.rend() );
    
    if ( arr.size() <= 1 )
    {
      result = 0;
    }
    else 
    {
      for (int i = 0; i < arr.size() - 1; i++) 
      {
        result += arr[i] - arr[i + 1];
      }
    }
    
    return result;
}

