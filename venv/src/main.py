from clientHandler import clientHandler
from socketHandler import SocketHandler

def main():

    socket_handler = SocketHandler()
    socket_handler.wait_for_connections()

if __name__ == "__main__":
    main()