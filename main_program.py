import zmq


class TimeConverterClient:
    def __init__(self, address="tcp://localhost:5555"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(address)
        self.default_format = self.get_default_time_format()

    def send_request(self, request):
        self.socket.send_string(request)
        return self.socket.recv_string()

    def set_default_time_format(self, time_format):
        response = self.send_request(f"set_default_time_format {time_format}")
        self.default_format = time_format
        return response

    def get_default_time_format(self):
        return self.send_request("get_default_time_format")

    def convert_time(self, time_str, time_format="default"):
        return self.send_request(f"{time_str} {time_format}")


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
    client = TimeConverterClient()

    print("Main Program for Time Conversion")
    print_help()

    while True:
        user_input = input("Enter command ('help' for commands): ").strip()
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'help':
            print_help()
        elif user_input.startswith("set_default_time_format"):
            _, time_format = user_input.split()
            response = client.set_default_time_format(time_format)
            print(response)
        elif user_input.startswith("get_default_time_format"):
            response = client.get_default_time_format()
            print(f"Default time format: {response}")
        else:
            try:
                time_str, time_format = user_input.rsplit(' ', 1)
            except ValueError:
                print("Invalid command format. Please use '<time_string> <format>'")
                continue
            response = client.convert_time(time_str, time_format)
            print(f"Converted time: {response}")


if __name__ == "__main__":
    main()
