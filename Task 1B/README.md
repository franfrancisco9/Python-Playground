## TASK 1B: Simple Web-Server
So far, we have implemented a small CLI program to decrypt and encrypt messages. In this task we will extend this by implementing a simple backend for the encryption.

### Description: 
The Webinterface has two endpoints:

Use this to encrypt your message: 
`YOUR_URL/caesar/encrypt?message=THIS_IS_YOUR_PLAIN_TEXT`
and this to decrypt your messages:
`YOUR_URL/caesar/decrypt?message=THIS_IS_YOUR_CYPHER_TEXT`

Please refer to the description of _Task#1A_ for the two examples.

### Task
Write a backend using a programming language (make it as simple as possible without any big frameworks) of your choice that encrypts and decrypt messages using Caesar's cipher. The request contains a message to be processed and the response the processed message in text format. Encapsulate your code into a Docker image that contains all the necessary libaries and the program code. After starting the container the mentioned endpoints to encrypt and decrypt should be accessible. 
