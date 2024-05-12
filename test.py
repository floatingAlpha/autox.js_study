import requests
result="96f2758f-b684-4bd1-b641-3805bdf9a6ad"
url = "https://webvpn.zzuli.edu.cn/http/77726476706e69737468656265737421f3f05885692a72457201c7a99c406d3651/Field/CardPay"

data = {
  'vpn-12-o1-cgyy.zzuli.edu.cn': '',
    'PayNo': '02',
    'Money': '0',
    'CardMoney': '1',
    'Count': '0.00',
    'MemberNo': '',
    'CardNo': '542102060223',
    'BillType': '100',
    'Password': '',
    'IsCheckPassword': '0',
    'OID': '96f2758f-b684-4bd1-b641-3805bdf9a6ad',
    'VenueNo': '001',
    'PayDiscount': '100',
    'IsUseMemberType': '1',
    'EWMNum': '1',
    '_': '1715471574359'
}

def base64_encode(input_string):
    input_bytes = input_string.encode('utf-8')
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
}

session = requests.session()
def get_ticket(headers):
    res0 = session.get(url="https://webvpn.zzuli.edu.cn/", headers=headers, allow_redirects=False)
    a = res0.headers['Set-Cookie'].index(";")
    ticket = res0.headers['Set-Cookie'][:a]
    print(ticket)
    return ticket

get_ticket(headers)
