#!/usr/bin/env python3

import json
import requests
from random import randint


def main():
    url = f"https://api.isevenapi.xyz/api/iseven/{randint(1, 10)}"
    print(f"enviando requisicao {url} ...")
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        print(data["ad"])
    else:
        print("response status:", response.status_code)


if __name__ == "__main__":
    main()
