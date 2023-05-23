from swaps import *

if __name__ == "__main__":

    if RNDM_WALLETS:
        random.shuffle(KEYS_LIST)

    for private_key in KEYS_LIST:

        cprint(f'\n--------------- start : {private_key} ---------------', 'white')

        swaps(private_key, CHAIN)
