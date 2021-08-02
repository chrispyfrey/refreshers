public class Fib {
    private static void fib(int n) {
        System.out.println(1);
        System.out.println(1);
        f(1, 1, n);
    }

    private static void f(int x1, int x2, int n) {
        if (x1 + x2 < n) {
            System.out.println(x1 + x2);
            f(x2, x1 + x2, n);
        }
    }

    public static void main(String[] args) {
        fib(1000);
    }
}
