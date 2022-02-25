//create a udp broadcast server to send "hello" to all clients in c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main(){
    //UDP Broadcast
    int sock;
    struct sockaddr_in addr;
    char buf[1024];
    int len;
    int broadcast = 1;

    //create the socket
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if(sock < 0){
        perror("socket");
        exit(1);
    }
    //set socket to broadcast
    if(setsockopt(sock, SOL_SOCKET, SO_BROADCAST, &broadcast, sizeof(broadcast)) < 0){
        perror("setsockopt");
        exit(1);
    }

    //fill in the address
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8888);
    addr.sin_addr.s_addr = htonl(INADDR_BROADCAST);

    //send the message
    while(1){
        printf("Enter message: ");
        fgets(buf, 1024, stdin);
        len = sendto(sock, buf, strlen(buf), 0, (struct sockaddr*)&addr, sizeof(addr));
        if(len < 0){
            perror("sendto");
            exit(1);
        }
    }
    close(sock);

}
