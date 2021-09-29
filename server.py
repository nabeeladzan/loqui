from random import randint

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

clients = []

class Server(DatagramProtocol):
    def datagramReceived(self, datagram, addr):
        if addr not in clients:
            clients.append(addr)
        
        for i in clients:
            if i != addr:
                self.transport.write(datagram, i)
            print(clients)


if __name__ == '__main__':
    port = 21604
    print("Working on port: ", port)

    reactor.listenUDP(port, Server())
    reactor.run()