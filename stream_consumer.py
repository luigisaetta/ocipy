import oci
import os
import io
import time
import sys
from pathlib import Path
from oci.config import validate_config
from oci.streaming import StreamClient
from oci.streaming.models import CreateCursorDetails
import base64


# configuration for connection to Oracle OCI
# for user, tenancy you have to specify the OCID
# the key is the key (PEM) you have uploaded to your profile 
#
config = {
    "user": "ocid1.XXXXXX",
    "key_file": "/Users/lsaetta/Progetti/xxxx/oci_api_key.pem",
    "fingerprint": "75:34:XXXXXX",
    "tenancy": "ocid1.ZZZZZ",
    "region": "eu-frankfurt-1"
}

SLEEP_TIME = 2 # in sec.

# check command line params
def check_params():
    N_PARAMS = 1 # expected # of params
    n_params = len(sys.argv)

    if (n_params < (N_PARAMS + 1)):
        print("Usage: stream_subscriber.py partition_id")
        print("")

        sys.exit(-1)
    else:
        print("Running with: ")
        print("partition_id {}".format(sys.argv[1]))
        print("")

def decode(str):
    return base64.b64decode(str).decode('utf-8')

#
# Main
#
print("")

check_params()

validate_config(config)

print("Validate config OK")
print("")


partition_id = sys.argv[1]
stream_id = "ocid1.stream.oc1.eu-frankfurt-1.aaaaaaaafsxpk4zdonaed3d27s5jwhazylryizrqmbd4ihnsgbbkpj3k6saa"

# check on partition_id OK, on offset OK
cursor_details = CreateCursorDetails(partition = partition_id, type = "LATEST")

# initialize consumer
client = StreamClient(config)

print("*** GET cursor ")
response = client.create_cursor(stream_id = stream_id, create_cursor_details = cursor_details)

## extract cursor from response
cursor = response.data.value

# infinite READ loop...
while True:
    # print("*** GET messages ")
    response_mess = client.get_messages(stream_id = stream_id, cursor = cursor)

    # prepare for goimg forward
    # you need to pass  ***new*** cursor
    cursor = response_mess.headers['opc-next-cursor']

    print("*")

    if (len(response_mess.data) > 0):
        print("Messages: ")
        for mess in response_mess.data:
            print(decode(mess.value))

    # sleep before next loop
    time.sleep(SLEEP_TIME)

