import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)

body=res.text

r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print("-"*30)
print("환율계산기")
print("-"*30)
print("")

for c in captures:
    print(c[0] + " : " + c[1])

print()
usd = float(captures[0][1].replace(",", ""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해주세요 : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전 되었습니다.")