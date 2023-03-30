#include <stdio.h>

/* Exercise 1
int main()
{
    int n1 = 7, n2 = 5;
    n1 += n2; //n1 = n1 + n2

    n2 += 12; //n2 + 12
    printf("n2 += 12 : %d\n", n2);
    return 0;
}
*/

/* Exercise 2
int main()
{
    int num1 = 7;
    int num2, num3;

    num2 = ++num1;
    num3 = --num1;

    printf("num1 : %d\n", num1);
    printf("num2 : %d\n", num2);
    printf("num3 : %d\n", num3);
    return 0;
}
*/

/* Exercise 3
int main()
{
    int num1 = 7;
    int num2, num3;

    num2 = num1++;
    num3 = num1--;

    printf("num1 : %d\n", num1);
    printf("num2 : %d\n", num2);
    printf("num3 : %d\n", num3);

    return 0;
}
*/

/* Exercise 4
int main()
{
    int num1, num2;
    num1 = 7;
    num2 = (num1--) + 5;

    printf("num1 : %d\n", num1);
    printf("num2 : %d\n", num2);

    return 0;
}
*/

/* Exercise 5
int main()
{
    int x = 3;
    int y = 2;

    printf("%d\n", (x > y) ? x : y);
    printf("%d\n", (x < y) ? x : y);

    return 0;
}
*/

/* Exercise 6
int main()
{
    int x, y, result;
    printf("enter two integers: ");
    scanf("%d %d", &x, &y);

    result = x + y;
    printf("%d + %d = %d\n", x, y, result);

    result = x - y; 
    printf("%d - %d = %d\n", x, y, result);

    result = x * y;
    printf("%d * %d = %d\n", x, y, result);

    result = x / y;
    printf("%d / %d = %d\n", x, y, result);

    result = x % y;
    printf("%d %% %d = %d\n", x, y, result);

    return 0;
}
*/

/* Exercise 7
int main()
{
    int a = 1;
    int b = 0;

    if(a || (b==5)) {
        printf("b is %d\n", b);
    }
    if(a && (b=5)){
        printf("b is %d\n", b);
    }

    return 0;
}
*/

/* Exercise 8
int main()
{
    int a = 15, b = 3, c;
    scanf("%d %d %d", &a, &b, &c);

    c = (a > b) ? a : b; 

    printf("bigger one is %d\n", c);
    return 0;
}
*/

/* Exercise 9
int main()
{
    int a, b, c;
    scanf("%d %d", &a, &b);

    c = (a > b) ? 0 : 1; // 'a' on ASCII CODE is 97

    printf("%c is bigger than %c", 97+(c ? 1 : 0), 98+(c ? -1 : 0));

    return 0;
}
*/

/* Exercise 10
int main()
{

    char a = 7;

    printf("a XOR a is %d\n", a^a);
    printf("a XOR a XOR a is %d\n", a^a^a);

    return 0;
}
*/