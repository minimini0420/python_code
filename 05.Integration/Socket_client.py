import socket


def Main():
    host = 'localhost'
    port = 8888

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(" -> ")
    first_receive=True

    while message != 'q':
        mySocket.send(message.encode())
        # mySocket.send(message)
        # data = mySocket.recv(1024).decode()
        # 만약에 위 코드가 작동하지 않는 다면 아래 코드로 대체 할 것
        data = mySocket.recv(1024)
        print('Received from server: ' + str(data))
        if first_receive == True:
            purified_data= str(data)[2:].split('\\xff')[0]
            first_receive = False
        else:
            purified_data = str(data)[2:].split('\'')[0]

        print("정제된 데이터: "+purified_data)

        message = input(" -> ")

    mySocket.close()


if __name__ == '__main__':
    Main()