#include "stdio.h"
#include "string.h"

int main(){
    char arr[6][10]={"hello","success","succeed","successfull"};
    char a[10];
    scanf("%s",a);
    int len=6;
    int wordlen=strlen(a);
    for (int i=0;i<len;i++){
        int x=strlen(arr[i]);
        if(wordlen<x){
            int c=0;
            for(int j=0;j<wordlen;j++){
                if(arr[i][j]!=a[j]){
                    c=1;
                    break;
                }
            }
            if(c==0){
                
                int l=strlen(a);
                int o=strlen(arr[i]);
                int cost=0;
                int v=0;
                if(l>o){
                    cost+=l-o;
                    v=o;
                }
                else{
                    cost+=o-l;
                    int v=l;
                }
                for (int t=0;t<v;t++){
                    if(a[t]!=arr[i][t]){
                        cost++;
                    }
                }
                printf("Word is%s Cost is %d\n",arr[i],cost);

            }
        }
    }
}