# gc__gvmi_hash
Summary: computes the hash of a gvmi image file. 

Problem:
A Requestor is required to provide the hash of the gvmi image pushed to the Golem network repo in its requestor script. However, this key is only printed once after pushing the image and verifying the script has been updated with the correct key is neither currently documented nor facilitated with the executables provided by the gvmkit-build Python package.

The provided gv__gvmi_hash.py solves this problem by hashing the input image file on demand with no additional dependencies than that already satisfied by the provider installation -- namely the Python Standard Library + OpenSSL libraries.

--Note: to understand better what problem this script solves, it is recommended the reader follow the Provider Flash Tutorial (Python) at https://handbook.golem.network/requestor-tutorials/flash-tutorial-of-requestor-development. --


Credits:
Adapted from the source code in the Python package gvmkit-build, which is viewable in the tarbell via https://pypi.org/project/gvmkit-build/#files (file: repo.py, function: upload_image).



Usage:
```
git clone https://github.com/krunch3r76/gc__gvmi_hash.git
python3 gc__gvmi_hash/gc__gvmi_hash.py <gvmi-image>
```

Example:
```
(cracker-venv) krunch3r@crystalcavern:~/hash-cracker$ python3 gc__gvmi_hash/gc__gvmi_hash.py *.gvmi
SHA3-224(docker-hash-cracker-latest-363b2e9df2.gvmi)= e1a95ab266977b857ae1c59942ebc7384a72359840b452c2e5293737
SHA3-224(docker-hash-cracker-latest-e93d21fba0.gvmi)= 4c9778760794a5fa6b8461ed2654c09cbc20f16edd3ec687c3289db8
```

Recommendations:
Consider placing community scripts such as this in $HOME/.local/bin/golem-community or $env:UserProfile/bin/golem-community and adding it to your path. You may also consider adding said community scripts path to the environment variable PYTHONPATH and calling from gc__gvmi_hash import gc__gvmi_hash in order to utilize the function from within scripts, e.g. requestor.py.

TODO: provide hints on adding community scripts into the Python venv instead.



primary function inputs,process,and outputs:
```
def gc__gvmi_hash(filename: str): # gc for golem community
MEBIBYTES=1024*1024 # one mebibyte ie megabyte, always a multiple of typical block sizes 4096,8192
# input: path to file as string
# pre: file is readable, MEBIBYTES defined
# process:
#   open gvmi image
#   on each chunk
#       send to hasher
#   query hasher
# output: hash as string
# post: none
# notes: additional details of the hashlib implementation may be discoverable via https://www.openssl.org/docs/manmaster/man3/EVP_DigestInit.html
```

Reflections:
The code can be reduced to just a few lines if the image is slurped into memory in one gulp as opposed to "chunking." However, without delving into the details of the OpenSSL hash algorithm, it reduces memory usage by never storing in memory at most two copies of the entire VM image at one time. Furthermore, OpenSSL could be calculating the hash based on a previous state per chunk and discarding prior chunks, or may do so in the future. An inspection of the OpenSSL code could validate this or future revisions could become more efficient at chunking. Therefore, reduced memory complexity from chunking should offer cost-savings on virtual servers and more efficient processing on other memory constrained devices.

TODO: move MEBIBYTES definition inside of function
