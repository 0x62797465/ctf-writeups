## Initial Analysis
Opon oppening the sample I'm greeted with a long analyses, that's fine. Whilst waiting I opened up the sample in DIE, nothing of interest, I use rank_strings and find this:\
![image](https://github.com/Boberttt/notes/assets/104478197/a961dea7-180d-4f54-99ef-c48cf540a98d)\
And since my disassembly didn't have any function names, I knew that this was a stripped golang binary. But fret not, as I went to plugin manager, and downloaded every golang related plugin I could find, resulting in total function recovery, and some nice emulated deobfuscated strings. This also has led to us finding main:\
![image](https://github.com/Boberttt/notes/assets/104478197/67c9646b-a5e3-42f1-8c3e-37310d091bed)
## Making our life easy with DynamoRIO
All we have to do:
1. Download DynamoRIO 8.0.1
2. Run the sample in a vm with the command: ./drrun -t drcov -- ./sample
3. Move the coverage to a USB
4. Revert the VM
5. Use BNCov
6. And bam
![image](https://github.com/Boberttt/notes/assets/104478197/bc688a41-3608-476c-84ca-84da3ad6cbf7)
