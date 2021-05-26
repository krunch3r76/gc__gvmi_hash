# gvmi_image_hash

The problem solves the problem when after a Requestor has published the vm (gvmi) image, and it prints the hash to which the requestor.py script is keyed, but the key is forgotten or the Requestor is unsure whether it corresponds to the image at hand. While the hash is simply the sha3_224 hash of the image, this hashing function is not ubiquitously available from shells at the time of this writing. However, it is equivalent to invoking `openssl dgst -sha3-224 <gvmi-image>`. Nevertheloss, the script solves the problem without any runtime dependency or dependency external to the Python standard library.

The logic closely follows the logic from the python package gvmkit-build (which is installed normally via pip in the Python virtual environment) in the repo.py file (viz def upload_image). The code from which this has been adapted may be viewed in the tarbell via https://pypi.org/project/gvmkit-build/#files.

Usage:

`python3 gvmi_image_hash.py <gvmi-image>`

