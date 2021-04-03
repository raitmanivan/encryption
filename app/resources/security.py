import bcrypt
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import binascii, os

try:
    import local_settings
    ENCRYPTION_KEY = local_settings.ENCRYPTION_KEY
except:
    print("Please create a local_settings file")

# region Encrypt


def generate_key():
    secret = ENCRYPTION_KEY.encode('ASCII')
    key = HKDF(secret, 32, b'h.security', SHA512, 1, context=bytes(1))
    return key


def encrypt_AES_GCM(msg, secret_key):
    aes_cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, auth_tag = aes_cipher.encrypt_and_digest(msg)
    return (ciphertext, aes_cipher.nonce, auth_tag)


def encrypt(password):
    print("Security - Encrypting data")
    round_key = generate_key()
    password = password.encode('ASCII')
    encrypted_pwd = encrypt_AES_GCM(password, round_key)
    pwd_storage_string = "{0};{1};{2}".format(binascii.hexlify(encrypted_pwd[0]).decode('ASCII'),
                                            binascii.hexlify(encrypted_pwd[1]).decode('ASCII'),
                                            binascii.hexlify(encrypted_pwd[2]).decode('ASCII'))
    return pwd_storage_string
# endregion

# region Decrypt


def decrypt_AES_GCM(encrypted_msg, secret_key):
    (ciphertext, nonce, auth_tag) = encrypted_msg
    aes_cipher = AES.new(secret_key, AES.MODE_GCM, nonce)
    plaintext = aes_cipher.decrypt_and_verify(ciphertext, auth_tag)
    return plaintext


def decrypt(password):
    print("Security - Decrypting data...")
    password = password.split(";")
    for i in range(len(password)):
        password[i] = binascii.unhexlify(password[i].encode('ASCII'))
    round_key = generate_key()
    decrypted_pwd = decrypt_AES_GCM(password, round_key).decode('ASCII')
    return decrypted_pwd
# endregion
