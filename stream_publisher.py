#
# Oracle SE Team Italy
# (L.S.)
# send a ingle msg to a Stream on OCI
#
import oci
import os
import io
import sys
from pathlib import Path
from oci.config import validate_config
from oci.streaming import StreamClient
from oci.streaming.models import PutMessagesDetails
from oci.streaming.models import PutMessagesDetailsEntry
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

# check command line params
def check_params():
    N_PARAMS = 2 # expected # of params
    n_params = len(sys.argv)

    if (n_params < (N_PARAMS + 1)):
        print("Usage: stream_publisher.py key str_message")
        print("")

        sys.exit(-1)
    else:
        print("Running with: ")
        print("Key {}".format(sys.argv[1]))
        print("Message {}".format(sys.argv[2]))
        print("")

def encode_string(str):
    return base64.b64encode(bytes(str, 'utf-8')).decode('utf-8')

#
# Main
#
print("")

check_params()

validate_config(config)

print("Validate config OK")

# send 1 msg
stream_id = "ocid1.stream.oc1.eu-frankfurt-1.aaaaaaaafsxpk4zdonaed3d27s5jwhazylryizrqmbd4ihnsgbbkpj3k6saa"
client = StreamClient(config)

n_mess = 1
key1 = encode_string(sys.argv[1])
value1 = encode_string(sys.argv[2])

message1 = PutMessagesDetailsEntry(key=key1, value=value1)

# build list of messages
messages = [message1]

message_details = PutMessagesDetails(messages=messages)

client.put_messages(stream_id, put_messages_details=message_details)

print("Message published")
print("")


