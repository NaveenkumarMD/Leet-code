//UDP boradcast reciever client


#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>

int main()
{
	int sockfd;
	struct sockaddr_in servaddr;
	char buff[1024];
	int n;
	
	sockfd = socket(AF_INET,SOCK_DGRAM,0);
	
	bzero(&servaddr,sizeof(servaddr));
	servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(5000);

    bind(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr));

    while(1)
    {
    	n = recvfrom(sockfd,buff,1024,0,NULL,NULL);
    	buff[n] = '\0';
    	printf("%s\n",buff);
    }
    return 0;
    close(sockfd);
}
