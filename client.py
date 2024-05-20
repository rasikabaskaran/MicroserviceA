import zmq


def print_help():
    print("""
Commands:
1. Convert Time with Specific Format:
   <time_string> <format>
   Example: '14:30 12' or '02:30 PM 24'

2. Set Default Time Format:
   set_default_time_format <format>
   Example: 'set_default_time_format 12'

3. Convert Time Using Default Format:
   <time_string> default
   Example: '14:30 default'

4. Get Default Time Format:
   get_default_time_format
   Example: 'get_default_time_format'

5. Exit Client:
   exit
   Example: 'exit'
""")


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print("Time Conversion Client")
    print_help()

    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        socket.send_string(command)
        response = socket.recv_string()
        print(f"Response: {response}")


if __name__ == "__main__":
    main()
