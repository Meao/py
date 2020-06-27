import os
# import uuid

# print(uuid.uuid4())

class UUID(object):

    def __init__(self, byte_s=None, version=None):

        if byte_s is not None:
            # https://docs.python.org/3/library/stdtypes.html#int.from_bytes
            integer = int.from_bytes(byte_s, byteorder='big')
        if version is not None:
            # Set the variant to RFC 4122. https://librambutan.readthedocs.io/en/latest/lang/cpp/bitwisemath.html#bitwise-not
            integer &= ~(0xc000 << 48)
            integer |= 0x8000 << 48
            # Set the version number.
            integer &= ~(0xf000 << 64)
            integer |= version << 76
        self.__dict__['int'] = integer

    def __str__(self):
        # https://stackoverflow.com/questions/32096244/python-magic-function-how-does-it-work
        hex = '%032x' % self.int
        return '%s-%s-%s-%s-%s' % (
            hex[:8], hex[8:12], hex[12:16], hex[16:20], hex[20:])


def uuid4():
    """Generate a random UUID."""
    return UUID(byte_s=os.urandom(16), version=4)

print(uuid4())

# import random as r

#  def generate_uuid():
#         random_string = ''
#         random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         uuid_format = [8, 4, 4, 4, 12]
#         for n in uuid_format:
#             for i in range(0,n):
#                 random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
#             if n != 12:
#                 random_string += '-'
#         return random_string
