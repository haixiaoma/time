import time

# 获取用户输入的分钟数
minutes = int(input("Enter the number of minutes to focus: "))
# 将分钟转换为秒
seconds = minutes * 60

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")