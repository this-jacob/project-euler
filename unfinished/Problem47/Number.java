import java.util.*;

public class Number{

    private int value;
    private int modVal;
    private int primePoint = 1;
    private List<Integer> primeFactors = new ArrayList<>();

    public Number(int n){
        value = n;
        modVal = value;
        primeFactorize();
        simplify();
    }

    public void primeFactorize(){
        if (this.isPrime(modVal)){
            primeFactors.add(modVal);
            return;
        }

        boolean flag = false;

        //find the next prime that goes into it
        do {
            primePoint++;

            if (modVal % primePoint == 0){
                modVal /= primePoint;
                primeFactors.add(primePoint);
                primePoint = 1;
                flag = true;
            }
        } while(!flag);

        //keep going until it's done
        this.primeFactorize();
    }

    public void simplify(){

        List<Integer> a = new ArrayList<>();

        for (int i = 0; i < primeFactors.size(); i++){
            if (!a.contains(primeFactors.get(i))){
                a.add((Integer)primeFactors.get(i));
            }
        }

        if (a.contains(1)){
            a.remove(1);
        }

        primeFactors = a;
        a = null;
    }

    public static boolean isPrime(int n){
        for (int i = 2; i < Math.sqrt(n) + 1; i++){
            if (n % i == 0){
                return false;
            }
        }
        return true;
    }

    public List<Integer> getPrimeFactors(){
        return primeFactors;
    }
}
