import java.util.*;   
public class GFG
{ 
final static int MAXN = 1000001 ;   
static int spf[] = new int [MAXN];  
static void ()
   {  
      spf[1] = 1;  

        for (int i = 2; i < MAXN; i++)  
        spf[i] = i;  
           for (int i = 4; i < MAXN; i += 2)  
           spf[i] = 2;  
            for (int i = 3; i * i < MAXN; i++) 
           { 
              if (spf[i] ==i)
              {
                for (int j = i * i; j < MAXN; j += i)
                 if (spf[j] == j)  

                        spf[j] = i;  

            }  

        }  

    }  
   static int sumFactors(int arr[], int n)  
{  
       for(int i = 0 ; i < MAXN ; ++i) 
       for (int i = 0; i < n; ++i)  
        int sum = 0;  
       for (int i = 0; i < n; ++i) 
       {  
          int num = arr[i];  
          while (num != 1 && (int))
          {  
            num /= spf[num];  

            } 
                if (num == 1)  

                sum += arr[i];  

        }  
       return sum;  

    }  
     public static void main(String []args) 
   {  
      int arr[] = { 5, 11, 55, 25, 100 };  

        int n = arr.length ;   
System.out.println(sumFactors(arr, n)) ; 

    } 
}