import hashlib
import hmac
import random

def get_mines(server_seed, client_seed, nonce, mines_count=3):
    hash_input = f"{server_seed}:{nonce}:{client_seed}"
    hash_result = hmac.new(b'', hash_input.encode(), hashlib.sha256).hexdigest()

    tiles = list(range(1, 26))
    random.seed(hash_result)
    random.shuffle(tiles)

    mine_tiles = tiles[:mines_count]
    safe_tiles = tiles[mines_count:]
    
    return mine_tiles, safe_tiles
