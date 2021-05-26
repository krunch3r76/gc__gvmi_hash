# gvmi_image_hash

The provided script solves the problem where a Requestor had published the vm (gvmi) image, and it had printed the hash to which the requestor.py script is keyed, the key has been forgotten or the Requestor has become uncertain that a key in question corresponds to the image at hand. While the hash is simply the sha3_224 hash of the image, this hashing function is not ubiquitously available from shells at the time of this writing -- with that said, it is equivalent to invoking `openssl dgst -sha3-224 <gvmi-image>`. At any rate, the problem is solved here without any such runtime dependency or library/module external to the Python Standard Library.

The logic closely follows the logic from the python package gvmkit-build (which is installed normally via pip in the Python virtual environment) in the repo.py file (viz def upload_image). The code from which this has been adapted may be viewed in the tarbell via https://pypi.org/project/gvmkit-build/#files.

Usage:

`python3 gvmi_image_hash.py <gvmi-image>`

