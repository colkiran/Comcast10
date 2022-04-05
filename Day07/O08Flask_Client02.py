
import requests

BASE = "c"

response = requests.get(BASE + '/getproduct/biscuts')

print(response.json())

res  = response.json()
for k, info in res.items():
    print(k.upper())
    print("--------")
    for ky, vl in info.items():
        print(ky)
        print("-----")
        for ki, v in vl.items():
            print(ki, "=>", v)
        print("-" * 40)
