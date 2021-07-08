import java.util.Arrays;
import java.util.Scanner;

public class Binary {
    public static void main(String [] args){
        int f,l,m;
        int flag=0;
        int[] array={1,2,4,5,6,7,8,9,20};
        System.out.println(Arrays.toString(array));
        f=0;
        l=array.length-1;


        Scanner input = new Scanner(System.in);
        System.out.print("Enter your number: ");
        int c=input.nextInt();
        m=(f+l)/2;

        while (f<=l) {
            if (array[m] == c) {
                flag=1;
                System.out.println("Found at index " + m);
                break;
            } else if (array[m] > c) {
                l = m - 1;
            } else if (array[m] < c) {
                f = m + 1;
            }
            m=(f+l)/2;
        }
        if (f>l){
            System.out.println("Item not found");
        }

    }
}
