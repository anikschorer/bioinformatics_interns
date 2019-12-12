#clarifies to the computer that python is the language
#!/usr/bin/env python3

#import librarys
import FileIO
import random
import OS
import string

#function makes repeat seq of DNA nucleotides
nuc_list = ["A","T","G",C"]
def repeat_seq(length):
    your_letters='ATCG'
    return ''.join((random.choice(your_letters) for i in range(length)))

repeat_seq1 = repeat_seq(30)
repeat_seq2 = repeat_seq(30)
repeat_seq3 = repeat_seq(30)
repeat_seq4 = repeat_seq(30)
repeat_seq5 = repeat_seq(30)


#function
def new_fasta():
#opens file  and is going to write what we tell it to - starts try block
	try:
		with open("pseudo_prote.fasta",w) as in_handle:
			in_handle.write(repeat_seq1,repeat_seq2, repeat_seq3, repeat_seq4, repeat_seq5)


#prints IOerror if it does not work
	except as IOError:
e		print"t_seq(length):
    your_letters='ATCG'
    return ''.join((random.choice(your_letters) for i in range(length)))IOError")
