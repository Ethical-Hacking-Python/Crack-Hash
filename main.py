import argparse
import hashlib
from tqdm import tqdm
from colorama import Fore, Style, init

init()

hash_names = [
    'blake2b', 
    'blake2s', 
    'md5', 
    'sha1', 
    'sha224', 
    'sha256', 
    'sha384', 
    'sha3_224', 
    'sha3_256', 
    'sha3_384', 
    'sha3_512', 
    'sha512',
]


def crack_hash(hash, wordlist, hash_type=None):

    hash_fn = getattr(hashlib, hash_type, None)
    if hash_fn is None or hash_type not in hash_names:
        raise ValueError(f'{Fore.RED}[!]{Fore.LIGHTWHITE_EX} Invalid hash type: {hash_type}, supported are {hash_names}')
    total_lines = sum(1 for line in open(wordlist, 'r'))
    print(f"{Fore.LIGHTBLACK_EX}[*]{Fore.LIGHTWHITE_EX} Cracking hash {hash} using {hash_type} with a list of {total_lines} words.")
    with open(wordlist, 'r') as f:
        for line in tqdm(f, desc='Cracking hash', total=total_lines):
            if hash_fn(line.strip().encode()).hexdigest() == hash:
                return line
            

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('hash', help='The hash to crack.')
    parser.add_argument('wordlist', help='The path to the wordlist.')
    parser.add_argument('--hash-type', help='The hash type to use.', default='md5')
    args = parser.parse_args()

    print()
    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Found password:", crack_hash(args.hash, args.wordlist, args.hash_type))


