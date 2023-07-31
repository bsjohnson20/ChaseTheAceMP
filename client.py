from time import sleep

from twisted.internet import reactor, protocol
from twisted.protocols import basic


class GameClientProtocol(basic.LineReceiver):
    def connectionMade(self):
        print("Connected to the server.")
        self.sendLine(b"advance_stage")

    def lineReceived(self, line):
        # Process the received message from the server
        message = line.decode()
        print("Received:", message)

        # Send player input back to the server (replace this with actual user input)
        player_input = input("Enter your input: ")
        self.sendLine(f"player_input {player_input}".encode())


class GameClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return GameClientProtocol()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()


if __name__ == "__main__":
    # Replace "localhost" with the IP address or hostname of your server
    # Replace 8000 with the port number on which the server is listening
    reactor.connectTCP("localhost", 8000, GameClientFactory())
    reactor.run()
