## IDA First Look
(Note that we will be using IDA free 8.3, which should not differentiate much from pro for our purposes).
Pros:
- Lumina server (yes IDA free has Lumina)
- Great highlighting/themes
- Decent flare support
- Dark mode!
Cons:
- Requires internet for using cloud decompiler.
## Ghidra First Look
(We'll be using Ghidra V10.3)
Pros:
- Decent flare support
- Dark mode!
- Awesome decompiler
- Awesome amount of arch support
- Plugin support
- Open source
Cons:
- Horrible graph view compared to almost every other tool.
## Binary Ninja First Look
(3.4 demo)
Pros:
- Awesome low/medium/high level IL
- Awesome offline decompiler
- Awesome dark mode
Cons:
- No project saving in demo
## Relyze First Look
(4.0.0)
Pros:
- Nice triage
- Decent decompiler
- Built in binary differ (pseudo code, graph, and disassembly)
Cons:
- Horrible graph view, though better than Ghidra
## Cutter First Look
(2.3.2)
Pros:
- Feature packed
- Rizin based (which is radare2 based) so it has great scripting
- 2 different decompilers
- Somewhat ok flirt support
- Likely/unlikely comments on conditional jumps for helping with quick analysis
- Awesome triage
- Great theme customization
- Open source!
Cons:
- Still under development, it still needs some time to be better. 
### Iaito First Look
(5.8.8)
Pros:
- Pretty much everything cutter has
Cons:
- It doesn't come with the ghidra decompiler, and the built in one doesn't have highlighting 
### Angr-management First Look
(9.2.68, let's be fair, this is more for symbolic execution than actual reversing)
Cons:
- Pretty slow analysis
- Crashed when I was trying to look at it
I'm not going to even through this in any tests, but I do have past experiences with it and it is great for doing quick symbolic execution. 
# Tests:
Our first test is going to be in the C language, pretty easy stuff for a decompiler.
## C
### Ida:
The graph view is awesome, we're instantly thrown into main, strings are in the comments, comments are made showing you what the argument is going to be for a function, and the decompilation is near perfect.
#### Ghidra:
The graph view is pretty bad, the decompiler output is decent (only bad thing is that it used var=var+1 instead of var++/++var), the disassembly seems to work really well with the decompiler (adding variable names and such), and all the disassembly is uppercase.
#### Binary Ninja:
The graph view is pretty good, the decompiler output is a bit bugged but understandable at the very least, the disassembly also works well with the IL/decompiler, there's verbose comments, and the dark theme is awesome.
#### Relyze:
The graph view is useable (though pretty bad, even on a small piece of code), the decompiler output is pretty bad, and the disassembly looks great.
#### Cutter:
The graph view is pretty good, the decompiler output is pretty bad, the disassembly is awesome though it does not compliment the decompiler, it has likely/unlikely comments for conditional jumps (and it seemed to get it right in this case), the theme is pretty good, it started at entry0 instead of main, it shows unsafe imports, it has an excelent triage, overall, a lot of features. 
#### Iaito:
It's so similar to cutter yet so horrible that I'm just going to eliminate it already. 
#### Conclusion (C test):
Ida won, with Ghidra following, then Binary ninja, then cutter, then relyze, then Iaito. 
## C++ test
This'll require some demangeling!
#### Ida:
Jumps straight to the main function, demangles most functions in comments to calls, great graph view, the decompilation is pretty bad (but useable, most function names aren't demangled), and the disassembly is ok!
#### Ghidra:
Jumps straight to the main function, demangles all functions (renames them), the graph view still sucks, decompilation is pretty good, the disassembly is pretty good as well!
#### BinaryNinja
Jumps straight to the main function, demangles all functions (renames them in medium level IL and higher, but adds comments for everything lower), the graph view is great, the decompilation is a bit mushed but it's useable (weird names but if you pay attention to things inside the parentheses you'll understand the code pretty well), the disassembly is pretty good.
#### Relyze
Doesn't jump to main, doesn't demangle functions (even in comments), the graph view is ugly, the decompilation is decent (for something without demangled functions), the disassembly looks good (for something without demangling).
#### Cutter
Doesn't jump to main, demangles functions (renames them), the graph view is ok, the decompilation is unreadable, and the disassembly is decent (but with my config the comments are overwhelming). 
#### Conclusion (C++ test):
BinaryNinja wins, Ghidra is a close follower, next Ida, next Cutter, and lastly Relyze. I'll be eliminating Relyze, while it has a great binary diffing feature, it has horrible graphing and lacks demangeling (which is a dealbreaker for most reverse engineers). 
## Go Test
#### Ida
Doesn't jump to main, the graph view manages to be as bad as possible for 3 blocks of code, the decompilation is horrible (as expected with go binaries), the disassembly is okish. 
#### Ghidra
Doesn't jump to main, I'm not even going to bother to use the graph view, the decompilation is horrible, the disassembly is pretty bad.
#### BinaryNinja
Doesn't jump to main, the graph view is ok, the decompilation is surprisingly better than ghidra and IDA (though it's not great), and the disassembly is better than ghidra though worse than IDA. 
#### Cutter
Cutter looses, doesn't jump to main, I can't even find main in the function lists or any of the strings. 
#### Conclusion (Go tests):
Ida wins by far, next binaryninja, afterwards ghidra, and lastly cutter. I'm eliminating Cutter, it's more of a toy than an actual RE framework, it's like radare2, so many cool features yet not a great core. Also it's open source so yeah, no funding at all.
## Rust
I have no experience with rust re, so I'm going in blind.
#### Ida
Jumps to the wrong main, loads the pdb file, demangles names in comments, the graph view is ok, the decompilation is bad (unuseable), the disassembly is pretty good.
#### Ghidra
Doesn't locate main, can't find main, ghidra sucks for rust ig.
#### Binaryninja
Jumps to the same main as ida, demangles some names, the decompilation is okish, the disassembly is decent.
#### Conclusion (Rust tests):
Without the pdb file, Binary ninja wins, followed by IDA, and lastly Ghidra which completely failed. With the pdb file, IDA wins. 
## Bonus: stripped C binary
#### Ida
no renaming, fails to find main
#### Binary ninja
no renaming, fails to find main
#### Ghidra
no renaming, fails to find main, decompiler crashes as well
# Conclusion:
#### BinaryNinja
1st place, it's core greatness is the IL, comments, looks, rust analysis, semi good go analysis, C++ analysis, and pretty good C analysis. For the price tag it's better than IDA. 
#### IDA
Second place, the amount of dev work done to this piece of software is insane, it manages to be feature packed without overwhelming the user or having a steep learning curve. Anyways, it has awesome C analysis, decent C++ analysis, and great GO analysis. 
#### Ghidra
Third place, great decompiler, pretty good disassembly. It still has some bugs making it unuseable at times, but it's pretty good. It's great at C++/C.
#### Why?
BinaryNinja and IDA are commercial products that costs hundreds (or in a lot of IDA's cases, thousands) of dollars, the dev teams have all the funding in the world (huge overexageration, but they do compared to the dev team of, let's say radare2). Ghidra is developed by the NSA, they have private funding as a version of Ghidra is used by the NSA (most likely).
Cutter is great, but it's not good with languages besides C, making it a bad option. This is because of the lack of motivation (aka money) for the dev team. 
Angr-management was never meant to be a fully fledged disassembly framework.
Relyze is centered around C/assembly, for some reason, making it a pretty bad option.
Iaito, same problem as cutter. 
