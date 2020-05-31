import os
from cryptography.hazmat.primitives.asymmetric import dsa, utils
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding

hashing_method = hashes.SHA256()

OUTPUT_PATH = "./output/log.txt"


def generate_keys():
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def printer(*value):
    print(*value, sep="")
    with open(OUTPUT_PATH, 'a') as f:
        print(*value, file=f)


def signer(private_key, digest):
    return private_key.sign(digest, utils.Prehashed(hashing_method))


def verifier(public_key, signature, data):
    try:
        public_key.verify(signature, data, utils.Prehashed(hashing_method))
        return True
    except:
        return False


def object_hash(object_value):
    hash_func = hashes.Hash(hashing_method, default_backend())
    hash_func.update(str(object_value).encode('utf-8'))
    return hash_func.finalize()
