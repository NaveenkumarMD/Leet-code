#include "stdio.h"
#include "math.h"
int finddistance(x1,x2,y1,y2){
    return sqrt(pow(x2-x1,2)+pow(y2-y1,2));
}
int main(){
    int arr[4][2]={{5,2},{13,4},{6,2},{4,8}};
    int len=sizeof(arr)/sizeof(arr[0]);
    int exploded[4]={0};
    int s=0;
    for (int i = 0; i <3; i++){
        for (int j=i+1; j<4;j++){
            if(finddistance(arr[i][0],arr[j][0],arr[i][1],arr[j][1])<5){
                exploded[i]=1;
                exploded[j]=1;
            }
        }
    }
    for (int i=0;i<4;i++){
        if (exploded[i]==0)s++;
    }
    for (int i=0;i<4;i++){
        if (exploded[i]==1)
            printf("First attempt %d %d\n",arr[i][0],arr[i][1]);
    }
    for (int i=0;i<4;i++){
        if (exploded[i]==0)
            printf("Other attempt %d %d\n",arr[i][0],arr[i][1]);
    }
    printf("Cannon can be fired at %d",s+1);
    
    return 0;
}