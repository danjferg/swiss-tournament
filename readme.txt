Tournament Results
by Daniel Ferguson 09/02/2015

This project provides a method to run a swiss-style game tournament.
It has a database that can be used to register players, create match pairs, 
store match results and show player standings.

Modules used:
  standard library
  psycopg2

To run this project you must have git, virtualbox and vagrant installed. The
project uses a virtual machine (VM) to run the database and python code. You
must also be connected to the internet in order for vagrant to obtain and 
update the vm image. When the virtual machine starts it automatically creates
the database and tables needed for the project.

To get started, do the following:

1. Extract the project files.
2. Open git and navigate to the vagrant folder.
3. Type "vagrant up" to turn on the VM.
4. Type "vagrant ssh" to connect to the VM.
5. Type "cd /vagrant/tournament" to browse to the tournament folder.
6. Run "python tournament_test.py" to run the test script.
7. Check the printed result from step six for the message,
	"Success!  All tests pass!" to ensure proper function.
8. Type "exit" to quit the VM.
9. Type "vagrant halt" to stop the VM.