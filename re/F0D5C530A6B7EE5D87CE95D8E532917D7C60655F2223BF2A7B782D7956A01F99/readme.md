## Initial analysis/Get password
When we open the project in ida, we see that information has NOT been stripped.
First we see:
```assembly
lea     rax, format     ; "Welcome to Easy Crack Me" // Loads the address containg that string into rax
mov     rdi, rax        ; format // Moves the address into rdi, which uses an extra instruction, so this likely wasn't compiled with optomizations.
mov     eax, 0          ; Moves 0 into eax, eax specifies the number of vector registers (xmm registers) that will be used in printf, printf("%f", 1.0f) would yeild 1 in eax, printf("%f %f", 1.0f, 2.0f) would yeild 2 and so on.
call    _printf         ; And a call to printf, to print "Welcome to Easy Crack Me"
```
This can be easily decompiled:
```c
printf("Welcome to Easy Crack Me");
```

### Next we see:
```assembly
lea     rax, aWhatIsTheSecre ; "What is the Secret ?"
mov     rdi, rax        ; format
mov     eax, 0
call    _printf
```
I'm not going to add comments as it is very similar to the above piece of assembly, it prints data.

### This can also be easily decompiled:
```c
printf("What is the Secret ?");
```

### The piece of assembly code right after that is:
```assembly
lea     rax, [rbp+var_40] ; This is a undefined variable, which the result of the scanf call will be later moved into
mov     rsi, rax          ; more un-optomized code, rsi is the actual argument
lea     rax, a64s         ; "%64s" // The format specifier, in this case a string with the max length of 64 chars.
mov     rdi, rax          ; MORE un-optomized code (possibly), rdi is also the actual argument.
mov     eax, 0            ; Same idea as above, except there's no legit use for XMM registers in the scanf function from what I can tell
call    ___isoc99_scanf   ; Good oll scanf
```

### Decompiled:
```c
scanf("%64s", &var);
```

### Next piece of assembly:
```assembly
lea     rax, [rbp+var_40] ; var_40 is the variable previosly modified by scanf
mov     rdi, rax          ; rax moved into rdi (the actual argument)
call    checkPass         ; insanely awesome function that does what we're trying to reverse (check the password)
test    eax, eax          ; The test instruction does an & operation on the return value (eax), sets the ZF if the result is zero (/eax is zero), and it won't if eax contains a value > 0
jz      short lose        ; The jump will be taken if the ZF flag is set, so the return value needs to be a value.
```
### Decompiled:
```c
if (!(checkPass(&var)) {
	lose();
} else {
	win();
} 
```

### So far we have:
```c
printf("Welcome to Easy Crack Me");
printf("What is the Secret ?");
scanf("%64s", &var);
if (!(checkPass(&var))) {
	lose();
} else {
	win();
}
```
## The checkpass function

```assembly
push    rbp                 ; Push the address of the base of the previos function
mov     rbp, rsp            ; Move the top of the stack into the base pointer
mov     [rbp+var_8], rdi    ; Load our argument (rdi) into a local variable var_8
mov     rax, [rbp+var_8]    ; Move the address of the input aka rdi into rax
movzx   eax, byte ptr [rax] ; movzx aka mov zero extended will move the first byte (input = 0xd34db33f, first byte is 3f) of the content inside the address rax holds into eax and make everything else that wasn't modified in eax 0
cmp     al, 73h ; 's'       ; compare eax and 0x73
jnz     short loc_11CC      ; if it is not 0, jump to the return function
```

### Decompiled:
```c
if ('s' != var[0]) {
	return 0;
}
```

### Next piece we have is:
```assembly
mov     rax, [rbp+var_8]    ; mov the arg into rax
add     rax, 1              ; add one to the address
movzx   eax, byte ptr [rax] ; move the lower byte of the content inside of the address rax into eax
cmp     al, 75h ; 'u'       ; al-'u' without storing the result
jnz     short loc_11D3      ; if the zero flag is not set, jump to the return function
```

### Decompiled:
```c
if ('u' != var[1]) {
	return 'u'; // this may be a bug, I'll test it later
}
```

### This pattern keeps happening, so I'll just so you the rest of the decompiled part:
```c
if ('d' != var[2]) {
	return 'd';
}
if ('o' != var[3]) {
	return 'o';
}
if ('0' != var[4]) {
	return '0';
}
if ('x' != var[5]) {
	return 'x';
}
if ('1' != var[6]) {
	return '1';
}
if ('8' != var[7]) {
	return '8';
}
```

### Finally, we have the end of the function:
```assembly
mov eax, 1         ; Make the return value 1
jmp short loc_11D3 ; Jmp to the return function
loc_11D3:
pop rbp            ; pop the saved rbp base address back into rbp
retn               ; return
```

### Decompiled:
```c
return 1;
```

### Here's the complete function (decompiled):
```c
int checkPass(char var[]){
	if ('s' != var[0]) {
		return 0;
	}
	if ('u' != var[1]) {
		return 'u'; // this may be a bug, I'll test it later
	}
	if ('d' != var[2]) {
		return 'd';
	}
	if ('o' != var[3]) {
		return 'o';
	}
	if ('0' != var[4]) {
		return '0';
	}
	if ('x' != var[5]) {
		return 'x';
	}
	if ('1' != var[6]) {
		return '1';
	}
	if ('8' != var[7]) {
		return '8';
	}
	return 1;
}
```

### Main function:
```c
int main () {
	printf("Welcome to Easy Crack Me");
	printf("What is the Secret ?");
	scanf("%64s", &var);
	if (!(checkPass(var))) { // While the address does get sent to the function, it's read only, so we can pass the var itself.
		printf("Better luck next time :(");
	} else {
		printf("You are correct :)");
	}
	return 0;
}
```

### Finally, the complete working code (added \#include and var decleration):
```c
#include <stdio.h>
int checkPass(char var[]){
	if ('s' != var[0]) {
		return 0;
	}
	if ('u' != var[1]) {
		return 'u'; // this may be a bug, I'll test it later
	}
	if ('d' != var[2]) {
		return 'd';
	}
	if ('o' != var[3]) {
		return 'o';
	}
	if ('0' != var[4]) {
		return '0';
	}
	if ('x' != var[5]) {
		return 'x';
	}
	if ('1' != var[6]) {
		return '1';
	}
	if ('8' != var[7]) {
		return '8';
	}
	return 1;
}

int main () {
	char var[64];
	printf("Welcome to Easy Crack Me");
	printf("What is the Secret ?");
	scanf("%64s", &var);
	if (!(checkPass(var))) { // While the address does get sent to the function, it's read only, so we can pass the var itself.
		printf("Better luck next time :(");
	} else {
		printf("You are correct :)");
	}
	return 0;
}
```

### But what is the password?
Well, it seems to be, anything starting with s with any character besides u behind it. If you compile the above code "s" works just fine, that's because it's slightly different, in what exact way I'm not sure.
While the intended password may have been "sudo0x18", s* (wildcard) works.

### But why?
There's two whys, why did the author make this mistake and why does s+anything work?
### First: 
The author doesn't seem to be that experienced in coding, first off, they forgot to add the newline char, which I thought was a disassembler bug at first, but nope, it (the program) actually prints:
```Welcome to Easy Crack MeWhat is the Secret ?```
So they may have had some error prone coding methods.

### Why does this work?
Well as we saw before:
```assembly
push    rbp                 ; Push the address of the base of the previos function
mov     rbp, rsp            ; Move the top of the stack into the base pointer
mov     [rbp+var_8], rdi    ; Load our argument (rdi) into a local variable var_8
mov     rax, [rbp+var_8]    ; Move the address of the input aka rdi into rax
movzx   eax, byte ptr [rax] ; movzx aka mov zero extended will move the first byte (input = 0xd34db33f, first byte is 3f) of the content inside the address rax holds into eax and make everything else that wasn't modified in eax 0
cmp     al, 73h ; 's'       ; compare eax and 0x73
jnz     short loc_11CC      ; if it is not 0, jump to the return function
```

This code is secure, if the input is just "s", it will continue the checks, if it doesn't start with s, it returns 0 which would fail you. 
But here's the fun part:
```assembly
mov     rax, [rbp+var_8]    ; mov the arg into rax
add     rax, 1              ; add one to the address
movzx   eax, byte ptr [rax] ; move the lower byte of the content inside of the address rax into eax
cmp     al, 75h ; 'u'       ; al-'u' without storing the result
jnz     short loc_11D3      ; if the zero flag is not set, jump to the return function
```

If eax != u, it returns, but they don't zero out eax before returning, so if the user inputed sw, w would get compared with u, fail, and return 'w'. But if the input is just "s", it would get compared, fail, and since there's a null terminator in the eax register, it returns 0.
So the semi-correct decompilation would be:
```c
char bob;
if (var[0] != 's') {
	bob = 0;
	return bob;
}
bob = var[1]; 
if (var[1] != 'u') {
	return bob;
}
```

## TL;DR:
Password was meant to be sudo0x18, but it can be s* (wildcard).
