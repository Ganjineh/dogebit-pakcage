import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dogebit.explorers import blockchain
from .base import BaseCoin


class Bitcoin(BaseCoin):
    coin_symbol = "DOGE"
    display_name = "Bitcoin"
    segwit_supported = True
    magicbyte = 0
    script_magicbyte = 5
    explorer = blockchain
    testnet_overrides = {
        'display_name': "Bitcoin Testnet",
        'coin_symbol': "BTCTEST",
        'magicbyte': 111,
        'script_magicbyte': 196
    }