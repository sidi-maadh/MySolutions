int past(int h, int m, int s) {

  int OneSeconde = 1000;
  int OneMinute = 60 * OneSeconde;
  int OneHeure = 60 * OneMinute;
   
  return (h * OneHeure) + (m * OneMinute) + (s * OneSeconde);  
}
