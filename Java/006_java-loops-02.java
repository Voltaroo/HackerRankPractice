// Java Loops II
import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] argh) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int temp = 0;
            String res = "";
            for (int j = 0; j < n; j++) {
                for (int k = 0; k <= j; k++)
                    temp += (Math.pow(2, k) * b);
                res += (a + temp) + " ";
                temp = 0;
            }
            System.out.println(res);
        }
        in.close();
    }
}