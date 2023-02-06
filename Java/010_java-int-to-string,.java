// Java Int to String
// Java 15, also this might be a wrong solution since I didn't parse int to String at all ... works fine without it
// But basically String number = n + "" works there as well

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        System.out.println(n >= -100 && n <= 100 ? "Good job" : "Wrong answer");
    }
}