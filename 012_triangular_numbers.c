#include <stdio.h>
#include <math.h>

int count_factors(double n){
    int count = 0;
    for(double i = 1; i <= n/2; i = i + 1){
      if(fmod(n,i) == 0)
        count++;
    }
    return count+1;
}

double triangular(double n){
    return n*(n+1)/2;
}

int main()
{
    int max_factors = 0;
    double index = 1;
    int MAX_FACTORS = 500;
    int DELTA = 10;

    while(1==1){
        int factors_x = count_factors(index);
        int factors_x_1 = count_factors(index+1);
        int triangular_factors = factors_x * (factors_x_1 - 1) + 1;


        if(triangular_factors >= MAX_FACTORS){
            double triangular_number = triangular(index);
            int real_factors = count_factors(triangular_number);

            //Lets calculate the real divisors now
            if(real_factors >= MAX_FACTORS){
                printf("Number: %f\n", index);
                printf("Triangular Number: %f\n", triangular_number);
                printf("Factors: %d\n", real_factors);
                break;
            }
        }
        index+=1;
    }

    return 0;
}
