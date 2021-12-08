import psutil, datetime, json

def cpu_cores():
    return psutil.cpu_count()

def cpu_util():
    return psutil.cpu_percent(interval=1)
    
def memory_used():
    return psutil.virtual_memory().percent

def memory_avail():
    return (100-psutil.virtual_memory().percent)

def disk_name():
    return psutil.disk_partitions()[0].device

def disk_total():
    d = psutil.disk_usage('/')
    total = d.total
    return total / (2**30)

def disk_used():
    d = psutil.disk_usage('/')
    return d.percent

def user_name():
    info = psutil.users()
    if(info[0].name):
        return info[0].name
    else:
        return "username"

def user_boot_time():
    formated = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return formated

def allData():
    data={
        'cpu cores': cpu_cores(),
        'cpu util': cpu_util(),
        'memory used': memory_used(),
        'memory available': memory_avail(),
        'disk name': disk_name(),
        'disk space': disk_total(),
        'disk used': disk_used(),
        'user name': user_name(),
        'user boot time': user_boot_time(),
        }
    response = json.dumps(data)
    return response

