"""
Transcribe RNA
"""
transcription = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def transcribe_rna(dna):
    """
    Transcribe RNA
    :param dna:
    :return: rna
    """
    rna = ''
    for letter in dna:
        rna += transcription[letter]

    return rna


def validate_dna(dna):
    return set(dna).issubset(set('GCTA'))

def main():
    while True:
        my_dna = input('Type DNA sequence: ')
        my_dna = my_dna.upper() #zmiana danych na duże litery
        if not validate_dna(my_dna):
            answer = input('Invalid DNA sequence, try again ([y]/n) ')
            if answer.lower() != 'y':
                break
            continue
        rna = transcribe_rna(my_dna)
        print(f'Transcribed RNA: {rna}')
        return

if __name__ == '__main__':
    main()