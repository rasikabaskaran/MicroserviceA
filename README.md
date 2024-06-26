# Time Format Converter Microservice

## Overview
This microservice provides functionality for converting between different time formats, including 12-hour and 24-hour formats. 

Utilizing the ZeroMQ messaging framework, the microservice establishes efficient communication channels between client and server components. This lightweight and scalable architecture ensures fast and reliable data exchange, making it suitable for integration into a wide range of software systems.

**Note:**
To execute the microservice, use Python 3. If your system defaults to Python 2, replace `python` with `python3` in the commands.

### Files
- server.py: This file contains the server program that implements the microservice. It listens for incoming requests, processes them, and sends back responses.
- main_program.py: This file is designed to help integrate the microservice into your own code. It provides a class-based interface for interacting with the microservice, making it easier to incorporate into other projects.
- client.py: This file contains the client program that demonstrates how to make requests to the microservice and receive responses (tested program for video).

### Supported Commands

1. **Convert Time with Specific Format:** Convert a time string to a specific format.
2. **Set Default Time Format:** Set the default time format preference.
3. **Convert Time Using Default Format:** Convert a time string using the default format.
4. **Get Default Time Format:** Retrieve the current default time format setting.
5. **Exit Program:** Close the application.


## How to Programmatically REQUEST Data

To request time format conversion from the microservice, follow these steps:

1. **Connect to the Microservice**: Open a terminal window and navigate to the directory containing the microservice files.

2. **Start the Microservice Server**: Run the server script by executing the following command:
   python3 server.py

3. **Send Request**: In a separate terminal window, run the main program script and specify the command and parameters as follows:
   python3 main_program.py

   **Convert Time with Specific Format**: Use the following command format: 
   - python3 main_program.py "time_string" format
   - Example: To convert "12:30 PM" to 24-hour format, use:
   - '12:30 PM 24'
   
   **Set Default Time Format**: Use the following command format: 
   - python3 main_program.py set_default_time_format format
   - Example: To set the default time format to 12-hour or 24-hour, use:
   - 'set_default_time_format 12' or 'set_default_time_format 24'
 
   **Convert Time Using Default Format**: Use the following command format:
   - python3 main_program.py "time_string" default
   -  Example: To convert "12:30 PM" using the default format, use:
   - '12:30 PM default'
   - Expected response: 12:30 if set to 24, 12:30 PM if set to 12

   **Get Default Time Format**: Use the following command:
    - python3 main_program.py get_default_time_format
    - Example: To check the default time format:
    - 'get_default_time_format'

   **Exit Program**: To exit, use:
    - python3 main_program.py exit
    - Example: To exit:
    - 'exit'

## How to Programmatically RECEIVE Data
To receive time format conversion requests and send back responses, follow these steps:

1. **Start the Microservice Server**: Open a terminal window and navigate to the directory containing the microservice files and establish a connection to the microservice using ZeroMQ.

2. **Run the Server**: Execute the following command to start the microservice server:
 python3 server.py

3. **Process Requests**: As clients send requests specifying the desired operation and parameters, the server will automatically process them and send back responses.

4. **Response**: Send back a response message containing the requested data starting with 'Response:'


Example call:

```python
import zmq

# Connect to the ZeroMQ socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Example request to the microservice
socket.send_string("12:30 PM default")
response = socket.recv_string()
print("Response from microservice:", response)
```


## UML Sequence Diagram
Here's a UML sequence diagram illustrating how requesting and receiving data works:

![UML Diagram](UML%20-%20S2.6.jpeg)
