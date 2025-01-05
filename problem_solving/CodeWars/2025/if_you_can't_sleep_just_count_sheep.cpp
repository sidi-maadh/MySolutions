#include <string>

std::string countSheep(int number) {
    std::string result = "";
    
    if (number > 0) {
        for (int i = 1; i <= number; i++) {
            result += std::to_string(i) + " sheep...";
        }
    }
    
    return result;
}
