import hashlib

print("========== Aaron's Hash Checker ==========")
print("")

print("========== Currently Supports MD5 SHA1 SHA512 ==========")

hash_type = input("What kind of hash is it? > ")

print("")

file = input("What file do you want to hash? > ")

print("")

provided_hash = input("What is the hash that you want to check against? > ")

print("")

if hash_type == "MD5":
    with open(file, 'rb') as file_to_check:
        data = file_to_check.read()

    hash_returned = hashlib.md5(data).hexdigest()


if hash_type == "SHA1":
    with open(file, 'rb') as file_to_check:
        data = file_to_check.read()

    hash_returned = hashlib.sha1(data).hexdigest()


if hash_type == "SHA512":
    with open(file, 'rb') as file_to_check:
        data = file_to_check.read()

    hash_returned = hashlib.sha512(data).hexdigest()










if provided_hash == hash_returned:
    print("Hash Verified")
else:
    print("Verification failed. File has been changed!")
    print("")
    print("New file hash", hash_returned)
    print("")
