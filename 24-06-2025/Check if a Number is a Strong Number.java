

👉 A Strong number is a number in which the sum of the factorial of digits is equal to the number (e.g., 145 = 1! + 4! + 5!).

public class StrongNumber {
    public static void main(String[] args) {
        int num = 145, sum = 0, temp = num;
        while (temp != 0) {
            int digit = temp % 10;
            int fact = 1;
            for (int i = 1; i <= digit; i++) fact *= i;
            sum += fact;
            temp /= 10;
        }
        System.out.println(num + " is " + (sum == num ? "Strong" : "Not Strong"));
    }
}
