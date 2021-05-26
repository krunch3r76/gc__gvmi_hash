# gc__gvmi_hash

The provided script (gc__gvmi_hash.py) solves the problem where a Requestor had published the vm (gvmi) image, and it had printed the hash to which the requestor.py script is keyed, and the key has been forgotten or the Requestor has become uncertain that a key in question corresponds to the image at hand. While the hash is simply the sha3_224 hash of the image, this hashing function is not ubiquitously available from shells at the time of this writing -- with that said, it is equivalent to invoking `openssl dgst -sha3-224 <gvmi-image>`. At any rate, the problem is solved here without any such runtime dependency or library/module external to the Python Standard Library.

The logic closely follows the that from the python package gvmkit-build (which is installed normally via pip in the Python virtual environment) in the repo.py file (viz def upload_image). The code from which this has been adapted may be viewed in the tarbell via https://pypi.org/project/gvmkit-build/#files.

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
Consider placing community scripts such as this in $HOME/.local/bin/golem-community or $env:UserProfile/bin/golem-community and adding it to your path. You may also consider adding a community scripts path to the environment variable PYTHONPATH and calling from gc__gvmi_hash import gc__gvmi_hash in order to utilize the function from within scripts, e.g. requestor.py.




primary function inputs,process,and outputs:
```
def gc__gvmi_hash(filename: str): # gc for golem community
MEBIBYTES=1024*1024 # one mebibyte ie megabyte, always a multiple of typical block sizes 4096,8192
# input: path to file as string, optional unbuffered read size
# pre: file is readable, MEBIBYTES defined
# process:
#   open gvmi image
#   on each chunk
#       add to hasher
# output: hash as string
# post: none
# notes: additional details of the hashlib implementation may be discoverable via https://www.openssl.org/docs/manmaster/man3/EVP_DigestInit.html
```
