#
# Oracle SE Team Italy
# with special thnks to SuperBrack
#
# 16/03/2019: modified to support multiple file uploading
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
    "user": "ocid1.XXXXX",
    "key_file": "/Users/lsaetta/Progetti/xxx/oci_api_key.pem",
    "fingerprint": "75:YYYYY",
    "tenancy": "ocid1.ZZZZ",
    "region": "eu-frankfurt-1"
}

# controlla command line params
def controlla_params():
    # verifica parametri input
    N_PARAMS = 3 # numero atteso parametri
    n_params = len(sys.argv)

    if (n_params < (N_PARAMS + 1)):
        print("Usage: upload.py bucket_name local_file_path file_names")
        # file_names could be a list separated by comma (eg: file1,file2)

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

# parse file_names
FILE_NAMES = sys.argv[3].split(",") 

object_storage_client = ObjectStorageClient(config)

# get the namespace
namespace = object_storage_client.get_namespace().data

print("")

for FILE_NAME in FILE_NAMES:
    print('Uploading file {} ...'.format(FILE_NAME))

    object_storage_client.put_object(namespace, bucket_name, FILE_NAME, io.open(os.path.join(Path(FILE_PATH), FILE_NAME),'rb'))

    print("Upload completato !")
    print("")

