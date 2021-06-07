Reflections:
The code can be reduced to just a few lines if the image is slurped into memory in one gulp as opposed to "chunking." However, it reduces memory usage by never storing in memory at most two copies of the entire VM image at one time. Furthermore, OpenSSL could be calculating the hash based on a previous state per chunk and discarding prior chunks, or may do so in the future. Therefore, reduced memory complexity from chunking offers cost-savings and performance benefits on memory constrained virtual servers or devices, and nominal read operation costs on any system.

