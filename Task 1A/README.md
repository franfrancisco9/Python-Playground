## TASK 1A: Caesar Cipher

### Description
One of the most popular cryptographic functions back in the days is called the "Caesar Cipher". Around 2000 years ago Caesar used this cipher to encrypt messages he sent to his troops without revealing the information to his enemies.

The basic idea of this cipher is to replace every single character in the message with another letter in the alphabet. The schema for replacing these characters is simply shifting by four. For instance `D->A`, `C->Z`.

```
Plain:     DEFGHIJKLMNOPQRSTUVWXYZABC
Encrypted: ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

The plain message `HELLO` will be encrypted to `EBIIL`

The encrypted message can be decrypted by simply back-shifting every single letter by four.

### Task
Write a small program for the command line that implements the Caesar cipher. The program takes two parameters. 

  - _decrypt_ or _encrypt_. This parameter is used distinguish between the two modes of operation. 
  - a _message_ to be encrypted or decrypted. 

### Examples

```
user@maya:~$ ./caesar encrypt "HELLO"
EBIIL

user@maya:~$ ./caesar decrypt "EBIIL"
HELLO
```
