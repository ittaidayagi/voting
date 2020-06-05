from clientHandler import clientHandler
import uuid
import socket
import threading


class SocketHandler():

    def __init__(self):
        self.server_ip = "192.168.8.13"
        self.server_port = 4545
        self.number_of_sessions = 2
        self.sessions = {}
        self.users_count = 1

    def on_new_connection(self,client_socket, addr):

        session_uuid = uuid.uuid4()
        self.sessions[session_uuid] = client_socket
        clientHandler(addr[0], session_uuid,self)

    def close_socket(self, session_uuid):

        session = self.sessions[session_uuid]
        session.close()
        print "closed"

    def communicate_with_client(self, session_uuid, msg):

        session = self.sessions[session_uuid]
        session.send(msg)
        session.settimeout(1)
        try: return session.recv(1024)
        except: return None

    def wait_for_connections(self):

        print 'Server started!'
        print 'Waiting for clients...'
        sock = socket.socket()
        sock.bind((self.server_ip, self.server_port))
        sock.listen(self.number_of_sessions)
        users_count = self.number_of_sessions
        threads = []
        for num in range(users_count):
            conn, addr = sock.accept()
            print addr
            thread = threading.Thread(target=self.on_new_connection,args=(conn,addr))
            threads.append(thread)
            thread.start()
        sock.close()



