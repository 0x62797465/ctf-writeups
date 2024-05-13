# Background
Jersey CTF challenge. Not really rev, more similar to misc. 
# Initial analysis
Godot binary, encrypted with some key.
# Finding the key
Using Google, I found this repo: https://github.com/char-ptr/gdke, when running it against the binary I got the key: bef8ffb43925db1a302c19645b8241cb51ba9032134e07ceb37ab5abeacc71c. This is hex encoded, and if you counted the chars (for some reason), it's *odd*. For people who are unfamiliar with hex, in order for it to be able to be decoded, you need an even amount of chars (if you have no separator, which in this case, we did have none). Looking into the source code for the key extractor repo, we find these signatures:
```
const SIGS: [&str; 5] = [
    // call into open_and_parse
    "E8 ? ? ? ? 85 C0 0F 84 ?  ?  ? ? 49 8B 8C 24 ?  ?  ?  ?", // 4.x (4.2.1)
    "E8 ? ? ? ? 89 44 24 50 83 7C 24 ? ?  0F 84 ?  ?  ?  ?  48 8B 44 24 ?", // 3.5.1
    "E8 ? ? ? ? 89 44 24 50 83 7C 24 ? ?  0F 84 ?  ?  ?  ?  48 8B 44 24 ?", // 3.5.1
    "E8 ? ? ? ? 8B D8 85 C0 0F 84 ? ? ?  ?  49 8B 04 24",      // 3.x
    "E8 ? ? ? ? 48 8B 4C 24 ? 89 C5 48 85 C9",                 // 4.3
];
```
Since compiling the repo is out of the question (I'm using linux and I don't want to set up everything), we can create a yara rule to find the address of the 4.x sigs:
```yara
rule FindKeyFunc
{
    strings:
        $hex_string = { E8 ?? ?? ?? ?? 85 C0 0F 84 ??  ??  ?? ?? 49 8B 8C 24 ??  ??  ??  ?? }

    condition:
        $hex_string
}
```
And run it with:
```
yara findkeyfunc.yara food-without-salt.exe -s
```
We get the output:
```
0x218217f:$hex_string: E8 8C A6 2A 00 85 C0 0F 84 8F 01 00 00 49 8B 8C 24 68 01 00 00
```
In Binary Ninja we can search for the string "E8 8C A6 2A 00 85 C0 0F 84 8F 01 00 00 49 8B 8C 24 68 01 00 00", and we find it's a function call located at 0x142182d7f:\
![image](https://github.com/Boberttt/ctf-writeups/assets/104478197/e7f2a497-f916-4481-960e-2271316b1fd7)\
### Finding the key (for real now)
If we open this IDA, set a breakpoint at 0x142182d7f, and run the binary, we can find a pointer to the key in r15:\
![image](https://github.com/Boberttt/ctf-writeups/assets/104478197/08d590ee-c29f-47c4-ab96-4ba9b81d945f)\
So finally we get: BEF8FFB43925DB1A302C19645B8241CB51BA90032134E07CEB37AB5ABEACC71C\
What was the bug in the key extractor function? Well, for bytes that start with 0 are not padded, so 03h would show up as 3. Fixed in this commit: https://github.com/char-ptr/gdke/commit/f33c8dbf43ee594b96d886323185a008d0c533a6
# Finding the flag
Using https://github.com/bruvzg/gdsdecomp we can dump the project, and using the godot engine editor (godot with -e), we can view the entire game:\
![image](https://github.com/Boberttt/ctf-writeups/assets/104478197/8f9df1da-cab3-4a58-bd6b-0cdd7fe8d656)
# The flag
SDCTF{Welc0m3_Back_Brack3ys}
# TL;DR
Bad "rev" challenge that required me to read rust (EW) and dump game files.
