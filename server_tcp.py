import socket
import torch
import numpy as np

TCP_IP = ""
TCP_PORT = 8765
TCP_BUFFER_EXPECTED_SIZE = 3*3*512*512  # MB
TCP_BUFFER_SIZE = TCP_BUFFER_EXPECTED_SIZE // 16
SAVE_FOLDER = "received_img"


def start_tcp_server(host, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections (max 1 connection in this example)
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        try:
            # Receive the data in chunks (adjust buffer size as needed)
            received_data = b""
            total_received = 0

            while total_received < TCP_BUFFER_EXPECTED_SIZE:
                data_chunk = client_socket.recv(TCP_BUFFER_SIZE)
                if not data_chunk:
                    break
                received_data += data_chunk.rstrip()
                total_received += len(data_chunk)

            print(f"Received {total_received} bytes of data")

            # Save the received data to a file
            file = open(f"{SAVE_FOLDER}/tensor", "wb")
            file.write(received_data)
            tensor = torch.tensor(np.frombuffer(received_data, dtype=np.uint8), dtype=torch.uint8).to(torch.device("cpu"))
            tensor.toPILImage().save(f"{SAVE_FOLDER}/test.jpg")

        except Exception as e:
            print(f"Error receiving data: {e}")
        finally:
            # Close the connection
            client_socket.close()


if __name__ == "__main__":
    # Set the host and port to your desired values
    start_tcp_server(TCP_IP, TCP_PORT)
