import hashlib

print(hashlib.sha256(str("Couch").encode('utf-8')).hexdigest())