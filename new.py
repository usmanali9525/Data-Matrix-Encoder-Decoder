import socket
import time

# Replace with your printer's IP address and port
printer_ip = '192.168.10.21'
printer_port = 3002

try:
    
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the printer
    s.connect((printer_ip, printer_port))

    start_time = time.time()

    # Send the "Hello World" job to the printer
    s.send(b'^0=ET010896110309015=\r')
    s.send(b'^0?CC\r')
    print(s.recv(1024).decode().split("\t")[0][5:])
    
    end_time = time.time()
    total =  end_time - start_time
    print(total*1000)
except socket.error as e:
    print("Socket error:", e)

finally:
    # Close the socket
    s.close()