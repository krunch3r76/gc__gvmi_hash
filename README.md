# gc__gvmi_hash
Summary: computes the hash of a gvmi image file

The provided script (gc__gvmi_hash.py) solves the problem where a Requestor had published the vm (gvmi) image but the key has been forgotten, or the Requestor has become uncertain that a key in question corresponds to the image at hand. Further, as it is not clearly documented or advertised which hashing algorithm is used by the Golem network, it provides a domain specific solution.

--Note: to understand what problem this script solves, it is recommended the reader follow the Provider Flash Tutorial (Python) at https://handbook.golem.network/requestor-tutorials/flash-tutorial-of-requestor-development. --

While the hash algorithm is simply the sha3_224 hash of the image, this hashing function is not ubiquitously available from shells at the time of this writing -- with that said, it is equivalent to invoking `openssl dgst -sha3-224 <gvmi-image>`. At any rate, the problem is solved here without OpenSSL executables or any other such runtime dependency or library/module external to the Python Standard Library + OpenSSL libraries.

Adapted from the source code in the Python package gvimkit-build, which is viewable in the tarbell via https://pypi.org/project/gvmkit-build/#files (file: repo.py, function: upload_image).



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
Consider placing community scripts such as this in $HOME/.local/bin/golem-community or $env:UserProfile/bin/golem-community and adding it to your path. You may also consider adding said community scripts path to the environment variable PYTHONPATH and calling from gc__gvmi_hash import gc__gvmi_hash in order to utilize the function from within scripts, e.g. requestor.py. TODO: provide hints on adding community scripts into the Python venv instead.




primary function inputs,process,and outputs:
```
def gc__gvmi_hash(filename: str): # gc for golem community
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
```
