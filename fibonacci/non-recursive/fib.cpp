#include <iostream>

void fib(int n);

int main() {
    fib(1000);
    return 0;
}

void fib(int n) {
    int x1 = 1;
    int x2 = 1;
    int x3 = 0;
    std::cout << x1 << std::endl;
    std::cout << x2 << std::endl;

    while (x1 + x2 < n) {
        std::cout << x1 + x2 << std::endl;
        x3 = x2;
        x2 += x1;
        x1 = x3;
    }
}
