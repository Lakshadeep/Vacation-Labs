#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void print_function(int num);
int main()
{
    int num;
    printf("Enter number upto which you want to print numbers\n");
    scanf("%d",&num);

    print_function(num);

    return 0;
}
void print_function(int num){
    int div3_check,div5_check,i=0;

    for(i=0;i<num+1;i++){
        div3_check = i%3;
        div5_check = i%5;

        if(div3_check ==0 && div5_check == 0){
            printf("Whazaa\n");
        }
        else{
            if(div3_check == 0){
                printf("Hip\n");
            }
            else if(div5_check == 0){
                printf("Hop\n");
            }
            else{
                printf("%d\n",i);
            }


        }


        }


}
