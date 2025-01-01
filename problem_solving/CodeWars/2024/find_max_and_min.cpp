#include <vector>
using namespace std;

int min(vector<int> list) {
  
    int min_values = list[0];
    for (int i = 0; i < list.size(); i++) 
    {
      if (min_values > list[i]) 
      {
        min_values = list[i];
      }
    }
  
    return min_values;
}

int max(vector<int> list){
  
  int max_values = list[0];
  for (int i = 0; i < list.size(); i++) 
    {
      if (max_values < list[i]) 
      {
        max_values = list[i];
      }
    }
    return max_values;
}
