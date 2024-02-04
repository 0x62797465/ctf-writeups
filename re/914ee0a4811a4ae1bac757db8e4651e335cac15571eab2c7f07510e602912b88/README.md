## Initial analysis 
.exe, mingw 6.3.0 (according to strings+rank_strings), not packed, debug not stripped. 
## Objective
"Hi guys this is my first Crackme it may have some bugs ignore them. This is a simple game, your health is 100 when you press the enter key your health decreases by 10 reverse the logic so the health increases by 10 when ever the enter key is pressed!! enjoy :)"
## Implementation
![image](https://github.com/Boberttt/notes/assets/104478197/8c3bb885-3ce3-446c-892d-89490a29f8c9)
We can see that it subtracts 0xa from the health (circled decompilation), we're supposed to make it increase, here's the disassembly:\
![image](https://github.com/Boberttt/notes/assets/104478197/a6645423-04a6-4b7b-ba83-7d01662e3c30)
I guess we could just change the sub to add, right?
![image](https://github.com/Boberttt/notes/assets/104478197/e7400deb-e5e6-4f9c-b1e0-46d40cebca8f)
Uhh... yeah:
![image](https://github.com/Boberttt/notes/assets/104478197/570621b2-bbdb-46dd-8dd7-a14bfb9909a9)
## Conclusion
I have to stop documenting easy crackmes, I literally just went to https://crackmes.one/lasts/1 
## Crackme:
https://crackmes.one/crackme/65ae9d45eef082e477ff5f98
