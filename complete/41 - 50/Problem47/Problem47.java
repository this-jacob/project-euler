import java.util.*;

public class Problem47{

    public static void main(String[] args){

        long startTime = System.currentTimeMillis();

        int index = 6;

        Number one = new Number(2);
        Number two = new Number(3);
        Number three = new Number(4);
        Number four = new Number(5);

        while (!allUnique(one, two, three, four)){
            one = two;
            two = three;
            three = four;
            four = new Number(index);
            index++;
        }

        System.out.println(index - 4);

        long endTime = System.currentTimeMillis();
        System.out.println(endTime - startTime);

    }

    public static boolean allUnique(Number a, Number b, Number c, Number d){

        if ((a.getPrimeFactors().size() == 4 && b.getPrimeFactors().size() == 4) && (c.getPrimeFactors().size() == 4 && d.getPrimeFactors().size() == 4)){
            return true;
        }

        return false;
    }
}
