#include <iostream>

unsigned countBits( unsigned long long n ) {
    int count = 0;
    while (n > 0) {
        count += n & 1; // Add 1 if the last bit is set
        n >>= 1;       // Right-shift the bits by 1
    }
    return count;
}
