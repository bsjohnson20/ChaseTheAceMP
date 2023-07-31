from twisted.internet import reactor, protocol
from twisted.protocols import basic

class GameServerProtocol(basic.LineReceiver):
    def connectionMade(self):
        print("Client connected.")
        self.sendLine(b"Welcome to the game!")

    def connectionLost(self, reason):
        print("Client disconnected.")

    def lineReceived(self, line):
        # Process the received message from the client
        line = line.decode().strip()
        print(line)
        if line == "advance_stage":
            self.advance_game_stage()
        elif line.startswith("player_input"):
            input_data = line[len("player_input"):].strip()
            self.process_player_input(input_data)

    def advance_game_stage(self):
        # Update the game stage and send a message to the client
        game_stage = "new_game_stage"  # Replace this with the actual game stage
        self.sendLine(f"Game stage: {game_stage}".encode())

    def process_player_input(self, input_data):
        # Process the player's input and respond to it
        # Replace this with the actual processing logic
        response = f"Received your input: {input_data}"
        self.sendLine(response.encode())

class GameServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return GameServerProtocol()

if __name__ == "__main__":
    # Replace 8000 with the desired port number for your server
    reactor.listenTCP(8000, GameServerFactory())
    print("Server started. Listening on port 8000...")
    reactor.run()
