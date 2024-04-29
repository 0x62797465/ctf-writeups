# Background
UMDCTF challenge, very hard in theory, only 9 people solved in the end. But... there was a  :cheese:
## Triage
(Rank_strings broke as of python3.12 being brought to arch). It's coded in C, no packer, requires you to connect to a server and enter your solution in order to get the flag. 
## RANDOM BULLSHIT GO!
When you interact with the program, it keeps taking in input via stdin, so, I thought, what if I press CTRL-D? Well, this: \
![image](https://github.com/Boberttt/notes/assets/104478197/65fc5368-9b66-4f0c-9452-3993c3bca9d0)

## But how do we use this on a server?
Well... you can't. EOF, in this situation, can only be activated via a closed socket, and if we close the socket, we won't be sent the flag :/\
But, if you look at ltrace, you'll see what happens when you send EOF:\
![image](https://github.com/Boberttt/notes/assets/104478197/572b74d7-aaef-44a8-af36-576e6c3c56ce)
It's just receiving a bunch of \n... 
## The solve
![image](https://github.com/Boberttt/notes/assets/104478197/4c5d5ad5-54c3-4d91-b15b-5ce2ad1ee9b9)

