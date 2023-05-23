# EVM Wallets Booster

Script to automatically boost and warm up your wallets to increase the potential of getting different airdrop in Arbitrum, Arbitrum nova networks and Optimism.

This script swaps ETH => token in one of the three networks: Arbitrum, Arbitrum nova networks and Optimism.

## Configuring

1) In `config.py` change the values of the variables :


    CHAIN = the network you are working with (ARBITRUM | NOVA | OPTIMISM)
    
    FROM_AMOUNT = from what number eth swap
    
    TO_AMOUNT = to what number eth swap
    
    RNDM_AMOUNT = number of digits after the point
    
    SLEEP_FROM = sleep from (in seconds) between swap and the next purse
    
    SLEEP_TO = sleep to (in seconds) between swap and the next purse
    
    FROM_COIN = starting from which coins to buy (default 1)
    
    TO_COIN = up to which coins to buy (>= 1)
    
    RNDM_WALLETS = True if you want to randomize wallets
    
    COINS = coins can be added here, you need to specify address and symbol of coins, there are already added some tokens for normal warming up is enough


2) In the file `private_keys.txt` add private keys from the wallets


3) Install dependencies with `pip install -r requirements.txt`


4) Run `start.py` and wait for results