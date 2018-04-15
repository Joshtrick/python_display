#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>

void send_a_number(float a_float, int coord_or_not, int *sock);

int main()
{
  //create socket client
  struct sockaddr_in address;
  int sock = 0;
  struct sockaddr_in serv_addr;
  if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
  {
    printf("\n Socket creation error \n");
    return -1;
  }

  memset(&serv_addr, '0', sizeof(serv_addr));

  serv_addr.sin_family = AF_INET;
  serv_addr.sin_port = htons(50000);

  // Convert IPv4 and IPv6 addresses from text to binary form
  if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0)
  {
    printf("\nInvalid address/ Address not supported \n");
    return -1;
  }

  if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
  {
    printf("\nConnection Failed \n");
    return -1;
  }
  //copy and paste the above codes to create a socket, make sure you create only once.

  int i = 0;
  //send data part
  //I put an while example for one face detected.
  //argument 1: the floating point number you are going to send
  //argument 2: pick 0 to send the float number in the serial version,
  //pick 1 to send the coordinate.
  //argument 3: the socket - just leave it as it is, if you copy
  //and paste the codes above.
  while(1)
  {

    if(i == 0)
    {
      // send face number
      send_a_number(5.0, 0, &sock);
      //send coordinates
      send_a_number(0.1253, 1, &sock);
      send_a_number(0.1253, 1, &sock);
      send_a_number(0.5253, 1, &sock);
      send_a_number(0.5253, 1, &sock);
      i = 1;
    }
    else{
      // send face number
      send_a_number(15.0, 0, &sock);
      //send coordinates
      send_a_number(0.0000, 1, &sock);
      send_a_number(0.0000, 1, &sock);
      send_a_number(0.3352, 1, &sock);
      send_a_number(0.3684, 1, &sock);

      send_a_number(0.1, 1, &sock);
      send_a_number(0.056, 1, &sock);
      send_a_number(0.500, 1, &sock);
      send_a_number(0.323, 1, &sock);

      send_a_number(0.1253, 1, &sock);
      send_a_number(0.1253, 1, &sock);
      send_a_number(0.4423, 1, &sock);
      send_a_number(0.4852, 1, &sock);
      i = 0;
    }
  }


  // close the socket at the very end.
  close(sock);
  return 0;
}

void send_a_number(float a_float, int coord_or_not, int *sock)
{
  int float_to_int;
  if(coord_or_not == 1)
  {
    float_to_int = a_float*1000;
  }else
  {
    float_to_int = a_float/5;
  }

  char tmp_char[5] = "00000";
  char buffer[5] = "00000";
  sprintf(tmp_char, "%d", float_to_int);

  for(int i = 0; i < 5; i++)
  {
    if(tmp_char[i] == NULL)
    {
      printf("i = %d\n", i);
      switch(i)
      {
      case 1:
        sprintf(&buffer[4],  &tmp_char[i-1]);
        break;
      case 2:
        sprintf(&buffer[4],  &tmp_char[i-1]);
        sprintf(&buffer[3],  &tmp_char[i-2]);
        break;
      case 3:
        sprintf(&buffer[4],  &tmp_char[i-1]);
        sprintf(&buffer[3],  &tmp_char[i-2]);
        sprintf(&buffer[2],  &tmp_char[i-3]);
        break;
      default:
        break;
      }
      break;
    }
  }

  //printf("%s\n", tmp_char);
  //printf("%s\n", buffer);
  //printf("%d\n", strlen(buffer));

  send(*sock, buffer, strlen(buffer), 0);
}
