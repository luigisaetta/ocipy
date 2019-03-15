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

# configuration for connection to Oracle OCI
# for user, tenancy you have to specify the OCID
# the key is the key (PEM) you have uploaded to your profile 
#
config = {
    "user": "ocid1.user.oc1..zzzzzzzzz",
    "key_file": "/Users/lsaetta/Progetti/xxxx/oci_api_key.pem",
    "fingerprint": "75:34:ZZZZ",
    "tenancy": "ocid1.tenancy.oc1..zzzzzzzzzz",
    "region": "eu-frankfurt-1"
}

# controlla command line params
def controlla_params():
    # verifica parametri input
    N_PARAMS = 1 # numero atteso parametri
    n_params = len(sys.argv)

    if (n_params < (N_PARAMS + 1)):
        print("Usage: list_files.py bucket_name")

        sys.exit(-1)
    else:
        print("Running with: ")
        print("Bucket name: {}".format(sys.argv[1]))
        print("")

#
# Main
#
print("")

controlla_params()

validate_config(config)

print("Validate config OK")

bucket_name = sys.argv[1]


object_storage_client = ObjectStorageClient(config)

# get the namespace
namespace = object_storage_client.get_namespace().data

response = object_storage_client.list_objects(namespace, bucket_name)

objectsList = response.data.objects

print()
print("Total # of files: {}".format(len(objectsList)))
print()

for o in objectsList:
    print(o.name)

print("")

