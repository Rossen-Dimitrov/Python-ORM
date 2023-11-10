from proxy_list import proxy_list_file
import urllib.request, socket

socket.setdefaulttimeout(180)


def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.add_headers = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        sock = urllib.request.urlopen('https://www.google.co.kr')
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print("ERROR:", detail)
        return 1
    return 0


for item in proxy_list_file:
    if is_bad_proxy(item):
        print("Bad Proxy", item)
    else:
        print(item, "is working")


is_bad_proxy()
