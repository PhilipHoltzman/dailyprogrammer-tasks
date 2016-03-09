#!Python 3.5
# DNA Replication challenge from /r/dailyprogrammer

# bases adenine, thymine, guanine, cytosine. 
# paired as follows: A-T and G-C.

# It is your job to generate one side of the DNA strand and output
# the two DNA strands. Your program should take a DNA sequence 
# as input and return the complementary strand.

# Input Strand: A A T G C C T A T G G C



print('\n\n..:DNA Replication Engine:.\n')

# initial strand
iStrand = 'AATGCCTATGGC'
# complimentary strand
cStrand = ''

for i in iStrand:
	if i == 'A':
		cStrand +='T'
	if i == 'T':
		cStrand +='A'
	if i == 'G':
		cStrand +='C'
	if i == 'C':
		cStrand +='G'


print('\n\nInitial Sequence Strand:\n\n ' + iStrand+ '\n')


print('Complimentary Base Pair Sequence:\n\n ' + cStrand + '\n\n')

