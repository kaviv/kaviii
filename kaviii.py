#include<stdio.h>
int main()
{
	int b;
	scanf("%d",&b);
	if(b%2==0)
	{
		printf("Even");
	}
	else if(b<0)
	{
		printf("invalid");
	}
	else
	printf("Odd");
	return 0;
}
