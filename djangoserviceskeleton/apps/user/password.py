# BCrypt was developed to replace md5_crypt for BSD systems.
# It uses a modified version of the Blowfish stream cipher.
# Featuring a large salt and variable number of rounds,
# it's currently the default password hash for many systems
# (notably BSD), and has no known weaknesses.
# See: http://pythonhosted.org/passlib/lib/passlib.hash.bcrypt.html

from passlib.hash import bcrypt


def encrypt(raw_password):
    return bcrypt.encrypt(raw_password)


def check(raw_password, hash):
    return bcrypt.verify(raw_password, hash)


def identify(hash):
    return bcrypt.identify(hash)