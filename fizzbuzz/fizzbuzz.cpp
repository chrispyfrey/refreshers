#include <iostream>

void fizzBuzz(int n);

int main() {
    fizzBuzz(100);
}

void fizzBuzz(int n) {
    for (int i = 1; i < n + 1; ++i) {
        printf("%d ", i);
        if (i % 3 == 0)
            printf("fizz");
        if (i % 5 == 0)
            printf("buzz");
        printf("\n");
    }
}