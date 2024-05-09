
import zmq

# SOCKETS SETUP

# Create context
context = zmq.Context()

# Connect to "Help" microservice socket (5000)
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5000")

# Create and send test list
test_list = [1,2,3,4]
print(f"Sending test list: {test_list}")

socket.send_json(test_list)

response = socket.recv_string()

print(f"Received response: {response}")