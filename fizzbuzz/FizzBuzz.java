public class FizzBuzz {
    private static void fizzBuzz(int n) {
        for (int i = 1; i < n + 1; ++i) {
            System.out.print(i + " ");
            if (i % 3 == 0)
                System.out.print("fizz");
            if (i % 5 == 0)
                System.out.print("buzz");
            System.out.println("");
        }
    }
    public static void main(String[] args) {
        fizzBuzz(100);
    }
}
