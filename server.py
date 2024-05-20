import zmq
from datetime import datetime


def convert_time(time_str, to_format):
    try:
        # Check if time_str contains AM/PM
        if 'AM' in time_str or 'PM' in time_str:
            time_obj = datetime.strptime(time_str, '%I:%M %p')
        else:
            time_obj = datetime.strptime(time_str, '%H:%M')

        if to_format == '12':
            return time_obj.strftime('%I:%M %p')
        elif to_format == '24':
            return time_obj.strftime('%H:%M')
        else:
            return "Invalid format. Use '12' for 12-hour or '24' for 24-hour format."
    except ValueError:
        return "Invalid time format."


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    default_format = '24'  # Default to 24-hour format

    print("Server started, waiting for requests...")

    while True:
        try:
            message = socket.recv_string()
            print(f"Received request: {message}")

            if message.startswith("set_default_time_format"):
                _, default_format = message.split()
                response = f"Default time format set to {default_format}"
            elif message.startswith("get_default_time_format"):
                response = default_format
            else:
                parts = message.rsplit(' ', 1)
                if len(parts) < 2:
                    response = "Invalid request format. Expected '<time_string> <format>'"
                else:
                    time_str = parts[0]
                    to_format = parts[1]
                    if to_format.lower() == "default":
                        to_format = default_format
                    response = convert_time(time_str, to_format)

            print(f"Sending response: {response}")
            socket.send_string(response)
        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            socket.send_string(error_message)


if __name__ == "__main__":
    main()
