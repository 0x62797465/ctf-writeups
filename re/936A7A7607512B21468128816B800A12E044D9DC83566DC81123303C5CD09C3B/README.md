## Intitial Analysis
Once we open the binary in ida, we're imidiatly at main, so we wont have to find the entry point, we also see things such as "?cout@std@@3V?\$basic_ostream@DU?$char_traits@D@std@@@1@A" which mean this is probably C++.
### The function itself:
```assembly
sub     rsp, 48h
mov     rax, cs:__security_cookie
xor     rax, rsp
mov     [rsp+48h+var_18], rax
lea     rcx, ConsoleTitle ; "CrackMe | Lizz | by Lucas0001"
call    cs:SetConsoleTitleW
mov     rcx, cs:?cout@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A ; std::basic_ostream<char,std::char_traits<char>> std::cout
lea     rdx, aWelcomeBraveHa ; "Welcome, brave hacker, to the ultimate "...
call    sub_1400014A0
mov     rcx, rax
lea     rdx, sub_140001670
call    cs:??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z ; std::basic_ostream<char,std::char_traits<char>>::operator<<(std::basic_ostream<char,std::char_traits<char>> & (*)(std::basic_ostream<char,std::char_traits<char>> &))
mov     rcx, cs:?cout@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A ; std::basic_ostream<char,std::char_traits<char>> std::cout
lea     rdx, aToProveYourSki ; "To prove your skills, you must crack th"...
call    sub_1400014A0
mov     rcx, rax
lea     rdx, sub_140001670
call    cs:??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z ; std::basic_ostream<char,std::char_traits<char>>::operator<<(std::basic_ostream<char,std::char_traits<char>> & (*)(std::basic_ostream<char,std::char_traits<char>> &))
mov     rcx, cs:?cout@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A ; std::basic_ostream<char,std::char_traits<char>> std::cout
lea     rdx, aEnterThePasswo ; "Enter the password: "
call    sub_1400014A0
mov     rcx, cs:?cin@std@@3V?$basic_istream@DU?$char_traits@D@std@@@1@A ; std::basic_istream<char,std::char_traits<char>> std::cin
lea     r8, [rsp+48h+var_28]
call    sub_140001740
lea     rcx, [rsp+48h+var_28]
mov     rax, 0FFFFFFFFFFFFFFFFh
```
At first this may look like a lot, but it's really not. Ida has automaticly demangled the calls for us, so we can see that the program is just setting the console title, printing a bunch of things using cout, and taking input via cin.
The most important thing we can take away from this is:
```assembly
lea     r8, [rsp+48h+var_28]]
```
and
```assembly
lea     rcx, [rsp+48h+var_28]
```
The first lea is right before the cin call, and the second is right after. So we can infer that the user-input is going to be located at rsp+0x48+var_28 and it's going to be pointed to by rcx.
## The password check
The first function right after the main function is:
```assembly
loc_140001236:
inc     rax
cmp     byte ptr [rcx+rax], 0
jnz     short loc_140001236
```
This is a simple, small function, all it does is get the length of the input. It does this by incrementing the part of the string 0x00 gets compared to, if the compare results in the ZF set (byte ptr [rcx+rax] == 0) it exits the loop with the length inside rax.
The next thing we see is:
```assembly
cmp     eax, 8
jnz     short loc_1400012B3 ; loc_1400012B3 is the "wrong" function
```
This compares the length, if it's not 8, it jumps to the wrong function.
If the ZF does get set, the next instructions that'll be executed are:
```assembly
xor     eax, eax
mov     edx, 41h ; 'A'
nop     dword ptr [rax+rax+00h]
```
This clears eax and moves the char 'A' into edx. 
The next function we have is:
```assembly
loc_140001250:
movsx   ecx, [rsp+rax+48h+var_28] ; This moves the data in rsp+rax+48+var_28 (the user input + rax) into ecx, and 0 extends ecx
cmp     ecx, edx                  ; edx, due to the above function, is 'A', and ecx is a char from the user input
jnz     short wrong               ; if the two aren't equal, you're wrong
inc     edx                       ; edx++
inc     rax                       ; rax++
cmp     rax, 8                    ; rax-8 but just setting flags
jl      short loc_140001250       ; if the result of rax-8 is < 0, loop the function
```
This'll repeat until either the wrong function gets called or rax is > 8, in which case it'll print the success message. 
## How do we solve this?
Well, first we need a bit more understanding of the code, here's some pesudo code:
```c 
char var = 'A';
int len = 8;
int count = 0;
do {
    if (input[count] ≠ var) {
        goto bad;
    }
    count++;
    var++;
} while (count <= 8)
```
What we need to do is find an input that starts with A (because we know input[0] == 'A'), and increaments the next char by one 7 more times (because we know the strlen is 8).
Here I've made some code to produce an input for me:
```c
#include <stdio.h>
int main () {
	int v7 = 0;
	int v8 = 65;
	while (1) {
		printf("%c", v8);
		++v8;
		++v7;
		if (v7 >= 8) {
			break;
		}
	}
}
```
The output is… drumroll please… "ABCDEFGH"
Thanks for reading my overexplained solution to this very simple crackme :D
