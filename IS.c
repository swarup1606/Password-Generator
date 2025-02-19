#include<stdio.h>
#include<conio.h>
int main(){
int i,j,key,n;
int A[100];
clrscr();
printf("***INSERTION SORT***");
printf("\nEnter the size of array :");
scanf("%d",&n);
printf("\nEnter the elements: \n");
for(i=0;i<n;i++){
scanf("%d",&A[i]);
}
for(j=1;j<=n;j++){
key=A[j];
i=j-1;
while(i>0 && A[i]>key){
A[i+1]=A[i];
i=i-1;
}
A[i+1]=key;
}
printf("\nElements after sorting :");
for(i=0;i<n;i++){
printf("\n%d",A[i]);
}
return 0;
}