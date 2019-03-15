#
# Oracle SE Team Italy
# (L.S.)
#
import oci
import os
import io
import sys
from pathlib import Path
from oci.config import validate_config
from oci.object_storage import ObjectStorageClient
from oci.core import ComputeClient

# configuration for connection to Oracle OCI
# for user, tenancy you have to specify the OCID
# the key is the key (PEM) you have uploaded to your profile 
#
config = {
    "user": "ocid1.XXXX",
    "key_file": "/Users/lsaetta/Progetti/xxxx/oci_api_key.pem",
    "fingerprint": "75:34:YYYYY",
    "tenancy": "ocid1.tenancy.ZZZZZ",
    "region": "eu-frankfurt-1"
}

# controlla command line params
def controlla_params():
    # verifica parametri input
    N_PARAMS = 1 # numero atteso parametri
    n_params = len(sys.argv)

    if (n_params < (N_PARAMS + 1)):
        print("Usage: stop_instance.py ocid")

        sys.exit(-1)
    else:
        print("Running with: ")
        print("Instance OCID: {}".format(sys.argv[1]))
        print("")

#
# Main
#
print("")

controlla_params()

validate_config(config)

print("Validate config OK")

ocid = sys.argv[1]

client = ComputeClient(config)

print('Starting instance...')

client.instance_action(ocid, 'START')

print("Instance to be started !")
print("")

