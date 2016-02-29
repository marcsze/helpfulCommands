Linux "Screen" commands (run program while computer is shut down)

Create a screen session:
screen

Create a screen session with a name associated with it:
screen -S <screen name>

List screen sessions
screen -list

Detach from current screen
Press Ctrl-A and then D

Reattach to screen using process ID (pid)
screen -r <pid>
	e.g. screen -r 1234

Reattach using a session name
screen -r <session name>
	e.g. screen -r mysession

More information about screen options
man screen

To kill a screen session
screen -S <session name> -p 0 -X quit