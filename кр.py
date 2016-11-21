#Наталья Энгель, 153
import urllib.request, re

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('ISO-8859-1')
    except:
        print('Error at', pageUrl)
        return


commonUrl = 'file:///C:/Users/natal/Desktop/thai_pages/'
for i in range(187, 206):
    for n in range(2, 74):
        pageUrl = commonUrl + str(i) + '.' + str(n) + '.html'
        download_page(pageUrl)


def task_numba_one():
    result = re.findall('<a href=*>*</a></td><td>bpat<span class=*>L</span> *<span class=*>L</span></td><td class=pos>*</td><td>*</td></tr><tr><td class=th>')
    print(result)
