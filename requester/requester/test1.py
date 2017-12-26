import requests
import utils
import handles

#
httpSession = requests.Session()
init_headers = utils.getHeaders('e:/headers.txt')

#创建一个下载器
downloadHtml = handles.Downloader(httpSession, init_headers)

#创建一个list，存储下载的种子，以及请求种子的方式、可选的数据参数
seed_url = [('http://logistics-front.liangdawang.com/logistics-front/ownInventoryWeightController/showList.htm?bindType=1','GET',None),]


r = downloadHtml('http://logistics-front.liangdawang.com/logistics-front/ownInventoryWeightController/showList.htm?bindType=1','POST', {
    'row':10,
    'page':3,
    'searchValue':'',
    'storageName':'',
    'dealer':'',
    'startDate':'',
    'endDate':'',
    'outState':''
})

print(r.headers)
print(r.request.headers)