public class Fib {
    private static void fib(int n) {
        int x1 = 1;
        int x2 = 1;
        int x3 = 0;
        System.out.println(x1);
        System.out.println(x2);

        while (x1 + x2 < n) {
            System.out.println(x1 + x2);
            x3 = x2;
            x2 += x1;
            x1 = x3;
        }

    }
    public static void main(String[] args) {
        fib(1000);
    }
}
