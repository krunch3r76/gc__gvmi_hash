# gc__gvmi_hash

The provided script solves the problem where a Requestor had published the vm (gvmi) image, and it had printed the hash to which the requestor.py script is keyed, and the key has been forgotten or the Requestor has become uncertain that a key in question corresponds to the image at hand. While the hash is simply the sha3_224 hash of the image, this hashing function is not ubiquitously available from shells at the time of this writing -- with that said, it is equivalent to invoking `openssl dgst -sha3-224 <gvmi-image>`. At any rate, the problem is solved here without any such runtime dependency or library/module external to the Python Standard Library.

The logic closely follows the logic from the python package gvmkit-build (which is installed normally via pip in the Python virtual environment) in the repo.py file (viz def upload_image). The code from which this has been adapted may be viewed in the tarbell via https://pypi.org/project/gvmkit-build/#files.

Usage:
```
git clone https://github.com/krunch3r76/gc__gvmi_hash.git
python3 gc__gvmi_hash/gc__gvmi_hash.py <gvmi-image>
```

Recommendations:
Consider placing community scripts such as this in $HOME/.local/bin/golem-community or $env:UserProfile/bin/golem-community and adding it to your path.



Inputs,Process,Outputs:
MEBIBYTES=1024*1024 # one mebibyte ie megabyte, always a multiple of typical block sizes 4096,8192
 input: path to file as string, optional unbuffered read size
 pre: file is readable, MEBIBYTES defined
 process:
   open gvmi image
   on each chunk
       add to hasher
 output: hash as string
 post: none
 notes: additional details of the hashlib implementation may be discoverable via https://www.openssl.org/docs/manmaster/man3/EVP_DigestInit.html
