from django import template
register = template.Library()

@register.simple_tag
def get_links(LinkFull, r):
    from lxml import html
    import requests
    data = ""
    Link = LinkFull.split("href='")[1].replace("'>Submit link</a></b></h3>", "")
    #return Link
    page2 = r.get(Link)
    tree2 = html.fromstring(page2.content)
    Links = tree2.xpath('//a')
    for y in range(0, len(Links)):
        if "forcedownload" in Links[y].get("href"):
            data += ("<p><a href='" + Links[y].get("href").replace("?forcedownload=1", "") + "'>" + Links[y].text  + "</a></p>")
            #print (Links[y].text.replace("Job Spec -","").replace("Job Spec ","").replace(".pdf","") +  "   " + Links[y].get("href").replace("?forcedownload=1", ""))
    return data
