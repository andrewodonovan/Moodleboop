from django.shortcuts import render
from django.http import HttpResponse
import base64

def index(request):
    from lxml import html
    import requests
    data = ""
    #login pls
    loginpage = "http://bismoodle2.ucc.ie/moodle/login/index.php?"
    r = requests.Session()
    payload = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'username':'116397543', 'password':decode(decode("w4DDksO0w7TDgsK1w5fDkMOiwr7DmMOKw6zDpcKQwqQ", "w6fCncK-wr7DjMOmwrfCkcOpwqI=="), "w4DDksO0w7TDgsK1w5fDkMOiwr7DmMOKw6zDpcKQwqQ=")}
    r.post(loginpage, data = payload)
    #hopefully logged in?
    page = r.get('http://bismoodle2.ucc.ie/moodle/course/view.php?id=2')
    print(page)
    linklist = []
    linklistOutput = []
    tree = html.fromstring(page.content)
    LinkData = tree.xpath('//div[@class="activityinstance"]//a')
    NameData = tree.xpath('//div[@class="activityinstance"]//a//span[@class="instancename"]/text()')
    for x in range (0, len(LinkData)):
        if "resource" not in LinkData[x].get("href") and "Assignment" not in NameData[x]:
            #data+= ("<h3><b><a href='" + LinkData[x].get("href") + "'>" + NameData[x] + "</a></b></h3>")
            data = ("<h3><b>" + NameData[x] + "   " + "<a href='" + LinkData[x].get("href") + "'>Submit link</a></b></h3>")
            linklistOutput.append(data)
            print (NameData[x] + "  " + LinkData[x].get("href"))
     
    return render(request, 'index.html', {'renderhere': data, 'linklistOutput': linklistOutput, 'requests': r})
    return HttpResponse(data)
	
#So that the password is slightly obscure to feel semi safe
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)