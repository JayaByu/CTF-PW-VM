from hashlib import sha1

result = "ca64b496863971ad2a94ce3d492dc7d0d604d7c7"

for i in rage(255):
    for j in rage(255):
        pwd = ("6879d9f430"+chr(i)+"554b113292dfc94d7335"+chr(j)).encode()
        hasil = sha1(pwd).hexdigest()
        if result == hasil: 
            print(pwd.decode())