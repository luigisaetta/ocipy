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
from oci.identity import IdentityClient
from oci.identity.models import CreateUserDetails

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
    N_PARAMS = 1 # numero atteso parametri
    n_params = len(sys.argv)

    if (n_params < (N_PARAMS + 1)):
        print("Usage: create_user.py name")

        sys.exit(-1)
    else:
        print("Running with: ")
        print("Username: {}".format(sys.argv[1]))
        print("")

#
# Main
#
print("")

controlla_params()

validate_config(config)

print("Validate config OK")

username = sys.argv[1]

client = IdentityClient(config)

# set user details
details = CreateUserDetails(compartment_id = config.get("tenancy"), description = "ocipy_created", name = username)

client.create_user(details)

print("User created !")
print("")

