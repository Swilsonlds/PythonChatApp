# PythonChatApp

# Overview

This program is a basic python chatroom that allows multiple clients to communicate with each on a LAN using TCP. In order to use the program, one must first run the "server.py" script to start the server. After this, the "client.py" script can be run on any PC on the LAN to join the chatroom.

[Software Demo Video](https://youtu.be/EK_lOShl4r4)

# Network Communication

As mentioned above, I opted for a client to server model for this project instead of a peer to peer connection. The chatroom uses TCP and operates at port 5051. The messages are encoded using utf-8.



# Development Environment

I created this program in the Visual Studio Code IDE and used the python programming language. I also made use of the "socket" and "threading" python libraries.

# Useful Websites

* [Python Sockets Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc)
* [Python Chatroom Tutorial](https://www.youtube.com/watch?v=3UOyky9sEQY)
* [Python Sockets Documentation](https://docs.python.org/3/library/socket.html)


# Future Work

* Color code the text based on the user who sent it
* Fix bug where upon receiving a message while typing, the un-sent portion of the message is overwritten.
* Refactor the program to run on my public IP address