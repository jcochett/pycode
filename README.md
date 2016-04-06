# ABOUT PYCODE
A repository for Python Code Examples I write.  This is a combination of projects which are listed below.  

# PROJECTS

## Encypted UDP Command Execution Client/Server
Sends commands to be executed via UDP.  Shares a secret key for the encryption which is hardcoded. 

Files:
- udp-client.py
- udp-server.py

Usage: 
'./udp-client.py IP PORT'
'./udp-server.py LOCALIP PORT'

Example:

Start the server
```
./udp-server.py 127.0.0.1 9000
Listening on port  9000 ... 

``` 

Start the client
``` 
./udp-client.py 127.0.0.1 9000
cmd> ls
udp-client.py
udp-server.py

cmd>       
``` 

## TCP client server example sending packed data
A simple client server that exchanges packed data via TCP
- tcp-packedclient.py
- tcp-packedserver.py

## TCP client/server example
A simple tcp client/server
- tcp-client.py
- tcp-server.py

## Make Python script for creating a new script in linux
Creates the file, adds the interpreter line, and changes linux permissions to execute
- mp.py

## Example code for walking a directory
- os-directory-walk.py

## Example code for a GUI in qt
- qt-gui-example.py

# GITHUB

## Create a new repository on the command line
Providing you in the directory with the code
```
echo "# pycode" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/jcochett/pycode.git
git push -u origin master
```

## Updating repository on the command line
Providing you in the directory with the code
```
git add .
git commit -m "updating code"
git push -u origin master
```

## Github Markdown Cheatsheet
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

