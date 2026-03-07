import java.util.Scanner;

class Solution {
    public static String reverseString(String s) {
        String rev = "";
        int l = s.length();
        for (int i = 0; i < l; i++) {
            char ch = s.charAt(i);
            rev = ch + rev;
        }
        return rev;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        System.out.println(reverseString(input));
    }
}