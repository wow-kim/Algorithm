import java.util.*;

public class Java_Stdin_and_Stdout_1 {

    public static void main(String[] args) {
        
        try (Scanner scan = new Scanner(System.in)) {
            while (scan.hasNext()) {
            System.out.println(scan.nextInt());
            }
        }
    }
}
