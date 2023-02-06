// Java Currency Formatter
import java.util.*;
import java.text.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        String in = NumberFormat.getCurrencyInstance(new Locale("en", "IN")).format(payment);
        String ch = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        String fr = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);

        // Write your code here.

        System.out.println("US: " + us);
        System.out.println("India: " + in);
        System.out.println("China: " + ch);
        System.out.println("France: " + fr);
    }
}