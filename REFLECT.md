Reflections:
The function for hashing (gc__gvmi_hash) can be reduced to just a few lines if the image is slurped into memory in one gulp as opposed to "chunking." However, it reduces memory usage by never storing in memory at most two copies of the entire VM image at one time. Furthermore, OpenSSL could be calculating the hash based on a previous state per chunk and discarding prior chunks, or may do so in the future. Therefore, reduced memory complexity from chunking offers cost-savings and performance benefits on memory constrained virtual servers or devices, and nominal read operation costs on any system. I am also considering making chunking a flag argument.


I struggled a bit with the decision to incorporate the option to query the Golem repository for the presence of a hash link because network connectivity is a cause for concern in security minded individuals. I am considering replacing the direct network connectivity with the output for a curl command instead.
