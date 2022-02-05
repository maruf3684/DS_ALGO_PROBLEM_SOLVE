import javax.print.event.PrintJobListener;

public class App {
    public static int count =0;
    public static void main(String[] args) throws Exception {
     
     System.out.println(find(5));
    }

    public static int find(int n){
        if(n==0){
      
            return 1;
        } 
        if(n<0){
            return 0;
        }

      return find(n-1)+find(n-2);
    }
}

