#include <stdio.h>

// Function definition matching the usage in main
void calcpay()
{
  void calcpay(float *pay, float rate, float hours)
  {
    if (hours <= 40)
    {
      *pay = rate * hours; // Regular pay for 40 hours or less
    }
    else
    {
      *pay = (rate * 40) + ((hours - 40) * rate * 1.5); // Overtime pay for hours above 40
    }
  }
}

#include <stdio.h>
int main()
{
  int empno;
  float rate, hours, pay;
  void calcpay();

  while (1)
  {
    if (scanf("%d %f %f", &empno, &rate, &hours) < 3)
      break;
    calcpay(&pay, rate, hours);
    printf("Employee=%d Rate=%.2f Hours=%.2f Pay=%.2f\n", empno, rate, hours, pay);
  }
}