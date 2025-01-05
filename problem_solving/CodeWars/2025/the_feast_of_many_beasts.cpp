#include <string>

bool feast(std::string beast, std::string dish){

  return beast[0] == dish[0] && beast[ beast.size() - 1 ] == dish[ dish.size() - 1 ] ? true : false;

}
