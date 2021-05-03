def hash_function(key):
    """
    Hash function ...
    """
    return 1


def find_slot(key):
    """
    key exist     -> Return current key's slot#
    key not exist -> Return the slot# into which key will be placed
    """
    slot = hash_function(key)
    start = slot
    while H[slot] and H[slot].key != key:
        slot = (slot + 1) % len(H)
        if slot == start:
            return "H is Full"
    return slot

def _set(key, value=None):
    slot = find_slot(key)
    if slot == "H is Full": # We need to increase size of H
        return None
    if H[slot]:
        H[slot].value = value
    else:
        H[slot].key, H[slot].value = key, value

if __name__=="__main__":
    H = []