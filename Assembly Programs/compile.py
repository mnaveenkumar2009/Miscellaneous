s=raw_input("please enter file name\n")

import os

os.system("nasm -f elf "+s+".asm")
os.system("ld -m elf_i386 -s -o "+s+" "+s+".o")
os.system("rm "+s+".o")
os.system("./"+s)
os.system("rm "+s)