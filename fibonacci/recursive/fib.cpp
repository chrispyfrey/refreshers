#include <iostream>

void fib(int n);
void f(int x1, int x2, int n);

int main() {
    fib(1000);
    return 0;
}

void fib(int n) {
    std::cout << 1 << std::endl;
    std::cout << 1 << std::endl;
    f(1, 1, n);
}

void f(int x1, int x2, int n) {
    if (x1 + x2 < n) {
        std::cout << x1 + x2 << std::endl;
        f(x2, x1 + x2, n);
    }
}