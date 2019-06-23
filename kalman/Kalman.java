import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Kalman {
    public static void main(String[] args) {
            List<Double> result = new ArrayList<>();
            double now = 0;
            double xPre = 0;
            double pPre = 0;
            double  sigmaW = 0;
            double sigmaV = 0;
            //引数指定　1 sigmaW , 2 sigmaV
            sigmaW = Integer.parseInt("5");
            sigmaV = Integer.parseInt("50");
            Scanner sc  = new Scanner(System.in);
            while(true){
                //System.out.println("type same number.");
                now = sc.nextDouble();
                if(now == -1){
                    break;
                }
                double xForecast = xPre;
                double pForecast = pPre + sigmaW;
                double KGain = pForecast/(pForecast + sigmaV);
                double  xFiltered = (xForecast + KGain*(now - xForecast));
                double pFiletered = (1-KGain) * pForecast;
                result.add(xFiltered);
                System.out.println(xFiltered);
                xPre = xFiltered;
                pPre = pFiletered;
            }
            System.out.println("end-------------------------------");
    }
}
