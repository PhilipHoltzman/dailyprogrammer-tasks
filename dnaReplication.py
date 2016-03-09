#!Python 3.5

# DNA Replication challenge from /r/dailyprogrammer

# bases adenine, thymine, guanine, cytosine. 
# paired as follows: A-T and G-C.

# It is your job to generate one side of the DNA strand and output
# the two DNA strands. Your program should take a DNA sequence 
# as input and return the complementary strand.

# Input Strand: A A T G C C T A T G G C

codons = {
	'TTT' : 'Phe',
	'TTC' : 'Phe',
	'TTA' : 'Leu',
	'TTG' : 'Leu',
	'CTT' : 'Leu',
	'CTC' : 'Leu',
	'CTA' : 'Leu',
	'CTG' : 'Leu',
	'ATT' : 'Ile',
	'ATC' : 'Ile',
	'ATA' : 'Ile',
	'ATG' : 'Met',
	'GTT' : 'Val',
	'GTC' : 'Val',
	'GTA' : 'Val',
	'GTG' : 'Val',
	'TCT' : 'Ser',
	'TCC' : 'Ser',
	'TCA' : 'Ser',
	'TCG' : 'Ser',
	'CCT' : 'Pro',
	'CCC' : 'Pro',
	'CCA' : 'Pro',
	'CCG' : 'Pro',
	'ACT' : 'Thr',
	'ACC' : 'Thr',
	'ACA' : 'Thr',
	'ACG' : 'Thr',
	'GCT' : 'Ala',
	'GCC' : 'Ala',
	'GCA' : 'Ala',
	'GCG' : 'Ala',
	'TAT' : 'Tyr',
	'TAC' : 'Tyr',
	'TAA' : 'STOP',
	'TAG' : 'STOP',
	'CAT' : 'His',
	'CAC' : 'His',
	'CAA' : 'Gln',
	'CAG' : 'Gln',
	'AAT' : 'Asn',
	'AAC' : 'Asn',
	'AAA' : 'Lys',
	'AAG' : 'Lys',
	'GAT' : 'Asp',
	'GAC' : 'Asp',
	'GAA' : 'Glu',
	'GAG' : 'Glu',
	'TGT' : 'Cys',
	'TGC' : 'Cys',
	'TGA' : 'STOP',
	'TGG' : 'Trp',
	'CGT' : 'Arg',
	'CGC' : 'Arg',
	'CGA' : 'Arg',
	'CGG' : 'Arg',
	'AGT' : 'Ser',
	'AGC' : 'Ser',
	'AGA' : 'Arg',
	'AGG' : 'Arg',
	'GGT' : 'Gly',
	'GGC' : 'Gly',
	'GGA' : 'Gly',
	'GGG' : 'Gly',
}




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


print('\n\n Initial Sequence Strand:\n\n ' + iStrand+ '\n')


print(' Complimentary Base Pair Sequence:\n\n ' + cStrand + '\n\n')

iSequence = 'ATGTTTCGAGGCTAA'

print('\n\n Initial DNA Sequence: ' + iSequence + '\n\n')

tSequence = ''

# Split strings to every 3rd letter and assign to parsed list of untranslated codons
pSequence = [iSequence[i:i+3] for i in range(0, len(iSequence), 3)]


# Loop through list translating individiual codons and writing to new variable
for i in pSequence:
	if i in codons.keys():
		tSequence += codons[i]

print(' Translated Codon Sequence: ' + tSequence + '\n\n' )
