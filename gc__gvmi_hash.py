#!/usr/bin/python3
#gc__gvmi_hash.py
import sys
import io
import hashlib
import os

# for __check_for_hash_link
import urllib.request
import http
import sys,os
import argparse


# inputs: the string hash of the image to check against, optional verbose switch
# pre: firewall permits outbound connections to golem.network
# process:
#   HEAD http request
# output:
#   0 on success
# post: stdout log on verbose setting
def __check_for_hash_link(image_hash: str, verbose=False):
    EC=0
    urls_to_try = ['yacn2.dev.golem.network:8000']
    for url in urls_to_try:
        if verbose:
            print(f"\nconnecting to {url}")
        url=f"http://yacn2.dev.golem.network:8000/image.{image_hash}.link"
        if verbose:
            print(f"\nCONNECTED!")
            print(f"sending HTTP HEAD request for {url}\n")
        req=urllib.request.Request(url, method="HEAD")
        res :http.client.HTTPResponse = None
        try:
            res = urllib.request.urlopen(req)
        except urllib.error.HTTPError:
            EC=1
        except urllib.error.URLError:
            EC=1
            print("Could not communicate with repository to check hash link. Check connectivity", file=sys.stderr)
            break
        if EC == 0:
            break
    return EC





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
    MEBIBYTES=1024*1024 # one mebibyte ie megabyte, always a multiple of typical block sizes 4096,8192
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
        print(f"Usage: {sys.argv[0]} <filename of gvmi image> ... | --check-hash-link <sha3-224 hash>")
        sys.exit(1)
    parser = argparse.ArgumentParser(description="description")
    image_hash :str = None
    parser.add_argument('--check-hash-link', type=str, help='the sha3-224 hash of the gvmi to check for')
    parser.add_argument('--check-hash-link-stdin', action='store_true')
    parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")

    args, gvmis = parser.parse_known_args()
    if args.check_hash_link_stdin:
        temp=sys.stdin.read().strip()
        args.check_hash_link=temp
    if args.check_hash_link:
        EC=__check_for_hash_link(args.check_hash_link, args.verbose)
        if EC == 0:
            print("The link exists on the central repository.")
        else:
            print("The link DOES NOT exist on the central repository.\n")
        sys.exit(EC)
    else:
        for thefilename in gvmis:
            if(os.path.isfile(thefilename)):
                print(f"SHA3-224({thefilename})" + '= ' + gc__gvmi_hash(thefilename))

