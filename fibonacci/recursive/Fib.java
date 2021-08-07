public class Fib {
    static void fib(int n) {
        f(1, 1, n);
    }

    static void f(int x1, int x2, int n) {
        if (x1 + x2 < n) {
            System.out.println(x1 + x2);
            f(x2, x1 + x2, n);
        }
    }

    public static void main(String[] args) {
        fib(1000);
    }
}
