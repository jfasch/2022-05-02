#include <stdio.h>


int main(void)
{
    unsigned long maxlong = 18446744073709551615UL;
    maxlong += 1;
    printf("%lu\n", maxlong);
    return 0;
}
