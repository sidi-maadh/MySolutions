int getRealFloor(int f) {
  
  int floor = 0;
  
  if ( f <= 0 ) {
    floor = f;
  }
  else if ( f < 13 ) {
    floor = f - 1;
  }
  else {
    floor = f - 2;
  }
  
  return floor ;
  
//   return f <= 0 ? floor = f : f == 15 ? floor = 13 : floor = f - 1; 
}
