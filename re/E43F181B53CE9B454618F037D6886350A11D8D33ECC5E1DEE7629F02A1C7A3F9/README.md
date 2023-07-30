# Initial Analysis
Opon opening this in DIE (detect it easy), I saw that this was coded in assembly (I'm pretty sure the crackme said that as well).
The first thing we see when we open it with ida is the start function, like usual, this is not the main function, the main function is actually dialogfunc.
What we see in the disassembly is several options, none of them are important, we just care about the password check. 
# The password check
![74595940843ed61b5d6bcb4ec2f18546](https://github.com/Boberttt/notes/assets/104478197/db5714c5-c62b-4774-bb8a-45749c0eba0c)


Before we attempt to reverse this monstrosity, let's try to find a easier way of making a keygen.
At the end of the function itself we can see a strcmp:
![0797f79415a2ad8e00bffd640aacb623](https://github.com/Boberttt/notes/assets/104478197/6f552833-fb43-4137-bcfa-4b4aae2eb96f)

When debugging this, we can see that it compares a weird value and our inputted password, it doesn't change based off password, and remains the same for each username, meaning we can possibly turn the file itself into a keygen…
# Patch2Keygen
When you get it right, this gets called:
![d534c75ec592bbd42b09f72eb1b48fc2](https://github.com/Boberttt/notes/assets/104478197/6e090ca8-79f3-4045-9a9e-7ca29808ddef)

Through patching, we can get this to be called every time, and instead of printing a congrats message, we print the password for the given username, here's the patched binary:
![173a65246a977be09cc2de584976f7a0](https://github.com/Boberttt/notes/assets/104478197/d73c959f-7721-467b-aa54-d2e929cf3786)

The arrow points to the password that's pushed onto the stack, you can also see that there's no way for you to get the bad boy message, in theory you can use the bad boy function but what if the user accidently inputs a correct password (joking ofc, I have no idea why I did this)?

This would've been a very hard crackme if I actually reversed it, but I didn't need to. 
