import datetime

def write_log(user, ip, status):
    with open("log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {ip} - {user} - {status}\n")
