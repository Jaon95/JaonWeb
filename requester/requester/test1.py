import requests
import utils
import handles

downloadHtml = handles.Downloader(requests.Session(), utils.getHeaders('e:/headers.txt'))

print(downloadHtml('http://logistics-front.liangdawang.com/logistics-front/ownInventoryWeightController/showList.htm?bindType=1','POST', {
    'row':10,
    'page':3,
    'searchValue':'',
    'storageName':'',
    'dealer':'',
    'startDate':'',
    'endDate':'',
    'outState':''
}))