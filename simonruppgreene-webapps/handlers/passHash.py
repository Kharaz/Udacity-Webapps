# This module contains functions for making a secure
# and salty password verification/hash generation system.

import random
import string
import hashlib

# salted pw stuff -v

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)

# non salted -v

def hash_str(string):
	string = str(string)
	return hashlib.md5(string).hexdigest()

def make_hash(val):
	return "%s|%s" % (val, hash_str(val))

def verify_hash(h):
	val = h.split('|')[0]

	if(h == make_hash(val)):
		return val
	else:
		return False