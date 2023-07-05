import subprocess
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("ISO-8859-1").split('\n')
wifis = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
    good = True
    try:
        results = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("ISO-8859-1").split('\n')
    except subprocess.CalledProcessError:
        good = False
    if good:
        res = [results[10]]
        if results[32][4:15] == "Key Content":
            res.append(results[32])
        else:
            res.append("    Key Content:           : UNKNOWN")
        for line in res:
            print(line)
        print()
