#
# Oracle SE Team Italy
# with special thnks to SuperBrack
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
    "user": "ocid1.user.oc1..aaaaaaaa74jcujsv5usad4sc747bfzvomn3tzcjxixxauy476u2eo5jg4nfa",
    "key_file": "/Users/lsaetta/Progetti/rgs/oci_api_key.pem",
    "fingerprint": "75:34:ba:e8:90:a5:ef:87:b5:ae:79:2a:85:a7:b5:38",
    "tenancy": "ocid1.tenancy.oc1..aaaaaaaa36syckdxnimtf5a4jvfsoe7ddyycboniocrumqga2joxlvzc6wsq",
    "region": "eu-frankfurt-1"
}

# controlla command line params
def controlla_params():
    # verifica parametri input
    N_PARAMS = 3 # numero atteso parametri
    n_params = len(sys.argv)

    if (n_params < (N_PARAMS + 1)):
        print("Usage: upload.py bucket_name local_file_path file_name")

        sys.exit(-1)
    else:
        print("Running with: ")
        print("Bucket name: {}".format(sys.argv[1]))
        print("File path: {}".format(sys.argv[2]))
        print("File name: {}".format(sys.argv[3]))
        print("")

#
# Main
#
print("")

controlla_params()

validate_config(config)

print("Validazione configurazione OK")

bucket_name = sys.argv[1]
FILE_PATH = sys.argv[2]
FILE_NAME = sys.argv[3]

object_storage_client = ObjectStorageClient(config)

# get the namespace
namespace = object_storage_client.get_namespace().data

print('Uploading file {} ...'.format(FILE_NAME))

object_storage_client.put_object(namespace, bucket_name, FILE_NAME, io.open(os.path.join(Path(FILE_PATH), FILE_NAME),'rb'))

print("Upload completato !")
print("")

