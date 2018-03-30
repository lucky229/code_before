#! usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request, parse
import json

if __name__ == "__main__":
    #从有道翻译查询的 Request URL
    Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    #创建Form_Data字典，存储在有道翻译查询获得的 Form Data
    Form_Data = {}
    Form_Data['i'] = 'jack'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'ATUO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1522218468879'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'
    Form_Data['typoResult'] = 'false'

    #使用urlencode方法转换表标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')

    #传递Request 对象和转换完格式的数据
    response = request.urlopen(Request_URL, data)

    #读取信息并解码
    html = response.read().decode('utf-8')

    #使用json
    translate_results = json.loads(html)

    #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']

    #打印翻译结果
    print('翻译的结果是： %s' % translate_results)