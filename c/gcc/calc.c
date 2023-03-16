#include <stdio.h>
#include "libmy.h"

void main() {
  int x, y;
  printf("input two numbers : ");
  scanf("%d %d", &x, &y);
  printf("%d + %d = %d\n", x, y, plus(x, y));
  printf("%d - %d = %d\n", x, y, minus(x, y));
}
