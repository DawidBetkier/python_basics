"""DNA na RNA"""

DNA_RNA = {
    'G':'C',
    'C':'G',
    'T':'A',
    'A':'U',

}

def transcribe_rna(dna):
    rna = ''
    for i in dna:
        rna += DNA_RNA[i]
    return rna

def validate_dna(dna):
    return set(dna).issubset(set('GCTA'))

def main():
    while True:
        my_dna = input('Type DNA sequence: ')
        if not validate_dna(my_dna):
            answer = input('Invalid DNA sequence, try again (y/n)? ')
            if answer.lower() != 'y':
                break
            continue
        rna = transcribe_rna(my_dna)
        print(f'Transcribed RNA: {rna}')

if __name__ == '__main__':
    main()

