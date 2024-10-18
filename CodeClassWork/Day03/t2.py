import os

# Create a pipe
read_end, write_end = os.pipe()

# Fork the process
pid = os.fork()

if pid > 0:  # Parent Process
    os.close(read_end)  # Close unused read end
    message = b'Hello from parent process!'
    os.write(write_end, message)  # Write message to the pipe
    os.close(write_end)  # Close the write end
else:  # Child Process
    os.close(write_end)  # Close unused write end
    os.wait()  # Wait for parent process to finish
    read_message = os.read(read_end, 1024)  # Read from the pipe
    print(f'Child process received: {read_message.decode()}')
    os.close(read_end)  # Close the read end
