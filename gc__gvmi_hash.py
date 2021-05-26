#!/usr/bin/python3
#gc__gvmi_hash.py
import sys
import io
import hashlib
import os

MEBIBYTES=1024*1024 # one mebibyte ie megabyte, always a multiple of typical block sizes 4096,8192
# input: path to file as string
# pre: file is readable, MEBIBYTES defined
# process:
#   open gvmi image
#   on each chunk
#       add to hasher
# output: hash as string
# post: none
# notes: additional details of the hashlib implementation may be discoverable via https://www.openssl.org/docs/manmaster/man3/EVP_DigestInit.html
def gc__gvmi_hash(filename: str): # gc for golem community
    MAXCHUNK=8*MEBIBYTES # few read()'s on a e.g. 40MiB image, reasonable mem requirement of 8MiB...
    hash_hex=""
    try:
        with open(filename, "rb", buffering=False) as raw_binary_file_obj: # io.FileIO
            hasher = hashlib.sha3_224()
            raw_binary_file_obj.seek(0, io.SEEK_SET)

            chunk :bytes = raw_binary_file_obj.read(MAXCHUNK)
            while chunk:
                hasher.update(chunk) # hash chunk into the digest context
                chunk = raw_binary_file_obj.read(MAXCHUNK)

            hash_hex = hasher.hexdigest() # retrieve digest value and represent as a hex string

    except OSError:
        print(f"There was a problem attempting to read the image file: '{filename}'", file = sys.stderr);
        
    return hash_hex




# BEGIN main
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename of gvmi image> ...")
        exit(1)
    for i in range(1, len(sys.argv)):
        thefilename=sys.argv[i]
        if(os.path.isfile(thefilename)):
            print(f"SHA3-224({thefilename})" + '= ' + gc__gvmi_hash(thefilename))
