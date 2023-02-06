// Java Static Initializer Block
// Note: I used Java 8 instead of Java 7 ... technical issues
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner scan = new Scanner(System.in);
        int B = scan.nextInt();
        int H = scan.nextInt();
        scan.close();
        System.out.println(B > 0 && H > 0 ? B * H : "java.lang.Exception: Breadth and height must be positive");
    }
}