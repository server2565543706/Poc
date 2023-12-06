import requests

url = "http://localhost:9174/"
io = requests.get(url=url)
driver = "mufenbai"
steering_control = 5
throttle = 2
# print(io.text)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {
    "driver": driver,
    # "steering_control": steering_control,
    "throttle": throttle,

}
# for i in range(5):

#     if 
post = requests.post(url=url,data=data,headers=headers)
print(post.text)