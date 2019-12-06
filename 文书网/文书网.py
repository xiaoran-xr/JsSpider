# -*- coding:utf-8 -*-
# 文书网爬虫 http://wenshu.court.gov.cn
# date: 2019年12月5日

import requests
import execjs


def wenshu_list_spider():
    session = requests.session()
    url = 'http://oldwenshu.court.gov.cn/list/list'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'DNT': '1', 'Host': 'oldwenshu.court.gov.cn', 'Pragma': 'no-cache', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/77.0.3865.90Safari/537.36'}
    resp = session.get(url=url, headers=headers)
    set_cookie = resp.headers['Set-Cookie']
    url = 'http://oldwenshu.court.gov.cn/List/ListContent'
    with open('文书网.js', 'r', encoding='utf-8') as f:
        wenshu_js = f.read()
    ej_com = execjs.compile(wenshu_js)
    vl5x = ej_com.call('vl5x', set_cookie)
    guid = ej_com.call('guid',)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'DNT': '1',
        'Host': 'oldwenshu.court.gov.cn',
        'Origin': 'http://oldwenshu.court.gov.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://oldwenshu.court.gov.cn/list/list',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/77.0.3865.90Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    post_data = {
        'Param': '案由:刑事案由,案件类型:刑事案件,全文检索:李腾飞',
        'Index': '1',
        'Page': '10',
        'Order': '法院层级',
        'Direction': 'asc',
        'vl5x': vl5x,
        'number': '&gui',
        'guid': guid,
    }
    resp = session.post(url=url, headers=headers, data=post_data)
    return resp.content.decode('utf-8')


if __name__ == '__main__':
    wenshu_list_spider()