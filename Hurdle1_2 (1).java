import java.io.*;
import java.util.*;

public class Hurdle1_2
{
	//method definition to remove the duplicates from a given list of integers
	public static ArrayList<Integer> removeDuplicates(ArrayList<Integer> inputList)
	{
		ArrayList<Integer> outputList = new ArrayList<Integer>();
		TreeSet<Integer> ts = new TreeSet<Integer>();

		//adding the elements of the given list into the TreeSet
		for(int in : inputList)
			ts.add(in);

		//taking the elements from the TreeSet and adding into the output list
		Iterator<Integer> iterator = ts.iterator();
		while(iterator.hasNext())
			outputList.add(iterator.next());

		return outputList;
	}


	//method definition to check whether a given number is Prime or not
	public static boolean isPrime(int number)
	{
		int count=0;
		boolean output = false;
		for(int i=1; i<=number; i++)
		{
			if(number%i == 0)
				count++;
		}

		if(count == 2)
			output = true;

		return output;
	}

	//method definition to find all the Prime Factors of a given number
	public static ArrayList<Integer> allPrimeFactors(int number)
	{
		ArrayList<Integer> primeFactorsList = new ArrayList<Integer>();
		for(int i=2; i<=number; i++)
		{
			if(number%i==0 && isPrime(i)==true)
				primeFactorsList.add(i);
		}

		return primeFactorsList;
	}

	//method definition to perform the two types of queries
	public static void query1(String q, int []arr)
	{
		//extracting all the individual values
		int l = Integer.parseInt(q.split(" ")[1]);
		int r = Integer.parseInt(q.split(" ")[2]);
		int x = Integer.parseInt(q.split(" ")[3]);

		//performing the task of this query
		if(r<l)
			System.out.println("Wrong Inputs!!!");
		else
		{
			for(int i=l; i<=r; i++)
				arr[i] = x;
		}
	}


	public static int query2(String q,int []arr, int K)
	{
		//extracting all the individual values
		int l = Integer.parseInt(q.split(" ")[1]);
		int r = Integer.parseInt(q.split(" ")[2]);


		//finding all the prime factors of K
		ArrayList<Integer> primesOfK = allPrimeFactors(K);

		//finding out the prime factors of the array elements
		ArrayList<Integer> totalPrimes = new ArrayList<Integer>();
		for(int k=l; k<=r; k++)
		{
			ArrayList<Integer> li = allPrimeFactors(arr[k]);
			for(int i : li)
				totalPrimes.add(i);
		}
		//System.out.println("Total Primes: " + totalPrimes);

		//removing all the duplicates in totalPrimes list of elements
		ArrayList<Integer> totalPrimes_noDuplicates = removeDuplicates(totalPrimes);

		//finding all the common elements 
		totalPrimes_noDuplicates.retainAll(primesOfK);
		//System.out.println("Total Primes Without Duplicates: " + totalPrimes_noDuplicates);
		return totalPrimes_noDuplicates.size();

	}


	public static void main(String []args) throws IOException
	{
		//creating an integer array of infinte length
		int []input_array = new int[8];

		//initialising it with zero at first
		for(int i=0; i<input_array.length; i++)
			input_array[i] = 0;

		//taking the inputs from the user
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String inputLine = br.readLine();

		//extracting the value of K
		int K = Integer.parseInt(inputLine.split(" ")[0]);

		//extracting the value of Q
		int Q = Integer.parseInt(inputLine.split(" ")[1]);

		//taking the next Q queries
		ArrayList<String> queryList = new ArrayList<String>();
		for(int j=0; j<Q; j++)
		{
			queryList.add(br.readLine());
		}

		//displaying the query list
		System.out.println("The query list is: " + queryList);

		//performing all the actions of the query list
		for(String str : queryList)
		{
			if(str.startsWith("!"))
			{
				//executing Query 1
				query1(str, input_array);
			}
			else if(str.startsWith("?"))
			{
				//executing Query 2
				int result = query2(str, input_array, K);
				System.out.println(result);
			}

		}
	}
}