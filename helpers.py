def stringSpelter(str=None):
    if (str):
        return str.replace(';', ' ').replace(',', ' ').replace('.', ' ').replace('،', ' ').replace('-', ' ').split()
    else:
        return ''


home = '/'
homeApi = '/api/v1'
