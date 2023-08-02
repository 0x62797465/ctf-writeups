## Initial analysis:
It looks to be, not packed, and coded in c
Here's the main disassembly with my comments:
```assembly
push    rbp
mov     rbp, rsp
sub     rsp, 30h                                ; Normal function call stuff, ignore it
mov     rax, 626F676A61667062h                  ; https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',8,false)From_Hex('Auto')&input=NjI2RjY3NkE2MTY2NzA2Mjc3Njk this and the next two instructions move the string bpfajgobiw into [rbp+var_17]
mov     qword ptr [rbp+var_17], rax
mov     word ptr [rbp+var_17+8], 7769h          ; Note that this does not make sense, it's actually rbp+var_17-8 (ty ghidra)
mov     [rbp+var_17+0Ah], 0                     ; printf setup stuff
lea     rdi, format     ; "The magic string: "
mov     eax, 0                                  ; end of printf setup stuff
call    _printf                                 ; Print "The magic string: "
mov     [rbp+var_4], 0                          ; Set counter to 0
jmp     short loc_11B3
```
To be honest, I mostly used the decompiler of ida and ghidra, so here's IDA's, we'll talk about it later:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // ecx
  char v5[11]; // [rsp+3h] [rbp-2Dh]
  char v6[11]; // [rsp+Eh] [rbp-22h] BYREF
  char v7[19]; // [rsp+19h] [rbp-17h] BYREF
  int i; // [rsp+2Ch] [rbp-4h]

  strcpy(v7, "bpfajgobiw");
  printf("The magic string: ");
  for ( i = 0; i <= 9; ++i )
    __isoc99_scanf(" %c", &v6[i]);
  *(_DWORD *)&v7[15] = 0;
  while ( *(int *)&v7[15] <= 9 )
  {
    if ( *(int *)&v7[15] > 6 )
      v3 = *(_DWORD *)&v7[15] - 7;
    else
      v3 = *(_DWORD *)&v7[15] + 3;
    v5[v3] = v6[*(int *)&v7[15]];
    ++*(_DWORD *)&v7[15];
  }
  v6[10] = 0;
  v5[10] = 0;
  *(_DWORD *)&v7[11] = 0;
  while ( *(int *)&v7[11] <= 9 )
  {
    if ( v5[*(int *)&v7[11]] != v7[*(int *)&v7[11]] )
    {
      puts("Sorry, wrong input :(");
      return 0;
    }
    ++*(_DWORD *)&v7[11];
  }
  printf("Congratulations, correct flag!\nThe flag is: WatadCTF{%s}\n", v6);
  return 0;
}
```
The first for loop is taking in 9 chars (note: a char will be inputted like this " s" not this "s") and placing them into v6.
The next while loop is moving the chars around, here's what it's doing (v5 is the output, v6 is the input):
```c
v5[0] = v6[3];
v5[1] = v6[4];
v5[2] = v6[5];
v5[3] = v6[6];
v5[4] = v6[7];
v5[5] = v6[8];
v5[6] = v6[9];
v5[7] = v6[0];
v5[8] = v6[1];
v5[9] = v6[2];
```
After that we have a string compare loop, it's about the same as:
```c
strcmp(v5, "bpfajgobiw");
```
But let's go back to the encryption, here's an example:
```c
#include <stdio.h>
int main () {
  char v7[17] = {0};
  char v6[] = "0123456789\0";
  int v3 = 0;
  char v5[30] = {0};
  while (v7[15] <= 9 )
  {
    if (v7[15] > 6 )
      v3 = v7[15] - 7;
    else
      v3 = v7[15] + 3;
    v5[v3] = v6[v7[15]];
    ++v7[15];
  }
  printf("%s", v5);
}
```
The input being 0123456789, would make an output of 7890123456
So what it does is it moves the last 3 chars to the start, so in order to reverse it we move the first 3 chars to the end.
So bpfajgobiw reversed is: ajgobiwbpf
Is that an input that'd work? Nope!! We still need to add spaces before each char due to how scanf is used, so our real, working, input will be:
 a j g o b i w b p f
