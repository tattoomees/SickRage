import psutil

def bytes2human(n):
    symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def diskusage(m):
    values = psutil.disk_usage(m)
    return '"' + m + ' ' + str(values.percent) + '% Free: ' + bytes2human(values.free) + ' Used: ' + bytes2human(values.used) + '/' + bytes2human(values.total) + '"'

