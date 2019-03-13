from urllib import request


if __name__ == '__main__':

    url = "http://jobs.zhaopin.com/195435110251173.htm?ssidkey=y&ss=409&ff=03&sg=2644e782b8b143419956320b22910c91&so=1"
    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))

    html = html.decode("utf-8")

    print(html)
