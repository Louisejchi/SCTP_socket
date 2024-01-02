import iperf3

server = iperf3.Server()
server.bind_address = '0.0.0.0'
server.verbose = False
while True:
    server.run()
