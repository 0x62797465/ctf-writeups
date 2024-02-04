## Initial analysis:
.exe, so it's for Windows (obviosly). DIE says it's C/C++. It does not look packed due to important strings being unobfuscated.
Let's find main, from our first look we can't find much:\
![image](https://github.com/Boberttt/notes/assets/104478197/302f2dfb-9247-45c5-b979-3e1ba44d5c5f)
![image](https://github.com/Boberttt/notes/assets/104478197/0ebd5a70-3422-455e-90ba-bb681cf4cda1)
![image](https://github.com/Boberttt/notes/assets/104478197/b3f0d319-5b3f-4811-9bfd-4f47bf73305f)

Well, how shall we approach this? As I said before, many strings are unobfuscated, so it's as simple as going to the strings tab, finding an interesting string, and looking for cross references:
![image](https://github.com/Boberttt/notes/assets/104478197/3eecac94-b705-4f50-a3ab-6a8510321645)

## Main
As seen in the previos picture, it's pretty simple (in high level IL at least). Our objective is to patch it so that we always win, there's three+ ways we can do this:
1. Patch the game victory to always happen
2. Modify registers so the if condition is always triggered for the game victory
3. Path the game so that the loss will never happen

Let's go with three:
Before:
![image](https://github.com/Boberttt/notes/assets/104478197/0b62318a-bbb5-445f-ad8f-ba097b6905c3)
During:
![image](https://github.com/Boberttt/notes/assets/104478197/2c33ad2d-357b-435e-bd4a-28480c8037dc)
After:
![image](https://github.com/Boberttt/notes/assets/104478197/a5772593-cae0-4f24-958a-dd54bd2f0032)

Now let's see if our implementation worked:
![image](https://github.com/Boberttt/notes/assets/104478197/af3fb83c-1d48-4f1f-b2ed-e8175cbc90f1)

Overall, this was pretty easy:
50s - opening and loading the binary
3min - analyzing and patching the binary
13mins - trying to make my VM not crash the binary, fail, and run it in triage instead
