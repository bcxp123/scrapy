import requests
import json
from lxml import etree

def main():
	url = "https://www.kuaidaili.com/free/"
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	res = requests.get(url = url,headers = headers)
	tree = etree.HTML(res.text)
	prox_list = tree.xpath('//div[@id="list"]/table[@class="table table-bordered table-striped"]//tr')[1:16]
	ipLists = []
	for line in prox_list:
		ip_dict = {}
		ip_dict['ip'] = line.xpath('./td[1]/text()')[0]
		ip_dict['port'] = line.xpath('./td[2]/text()')[0]
		ipLists.append(ip_dict)
	newIp = []
	for ip in ipLists:
		url = 'http://www.baidu.com'
		ip_url =  str(ip['ip'] )+ ':' + str(ip['port'])
		if requests.get(url,proxies={'http://':ip_url},timeout=3).status_code == 200:
			newIp.append(ip)
		else:
			continue
	
	with open('ip.txt','w',encoding='utf8') as fp:
		fp.write(json.dumps(newIp))


	# print(len(ipLists))
	# print(ipLists)
	# print(len(newIp))

if __name__ == "__main__":
	main()
