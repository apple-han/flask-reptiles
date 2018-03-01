import re
url = 'http://www.xicidaili.com/'
import requests
import re

res = requests.get(url).text()


reg_ip = re.compile('[0-9]+(?:\.[0-9]+){3}')

reg_foue_ip = re.compile('<td>(\d{1,5})<td>')


result = re.findall(reg_ip,res)

print(result)

