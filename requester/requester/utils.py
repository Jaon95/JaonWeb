
def getHeaders(file_name):
    f = open(file_name,'r')
    headers = {}
    for i in f:
        i = i.strip()
        data = i.split(':')
        headers[data[0]] = data[1]
    return headers

if __name__=="__main__":
    headers = getHeaders('e:/headers.txt')
    print(headers)
