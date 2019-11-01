# coding:utf-8
import json
import re
import random, string

# str = '[{"mod":"cn_s","ce":"cca2f4d2b252ded7cf2eb7af8eb52a8e","c_batch":"1","23_hl_id":"140992497748","msg_id":"140992497748","r_aidlist":"140992497748","feedid":"140992497748","agenttype":"317","c_rtype":"0","mcnt":"sort_id:1;wt_id:2","s2":"home_top_menu","position":"3","c_rclktp":"0","ext":"","s4":"1","isdcdu":"0","r_rank":"0","bstp":"23","t":"21","rpage":"qy_home","block":"headline","s3":"E:020000","tnord":"1","p1":"2_22_222","u":"b2ad52a2f86e941344c01201aa2db7677004","pu":"","v":"10.9.0","rn":"1572439397937","de":"mw7l1wkt2tub8gg9","sid":"mw7l1wkt2tub8gg9.0","hu":"-1","mkey":"b398b8ccbaeacca840073a7ee9b7e7e6","stime":"1572439397936","ua_model":"PRO 6 Plus","net_work":"1","qyidv2":"988EF626B4725F342595EC138F932D9E","dfp":"","iqid":"","biqid":"b2ad52a2f86e941344c01201aa2db7677004","n_mac":"B2-14-9E-E6-93-C3","n_lang":"","n_gps":"","tagemode":"0","pbv":""}]'
# hah = json.loads(str, encoding='utf-8-sig')
# items = hah[0].items()
# print(items)

# url_dict = dict()
# url = 'http://msg.qy.net/v5/alt/act?rn=pv1wrf1b5somxywp_1572439397961&wsc_lgt=&wsc_ltt=&wsc_tt=02&wsc_ost=14&wsc_osl=zh&wsc_st=10.9.0&wsc_sm=B2-14-9E-E6-93-C3&wsc_istr=b2ad52a2f86e941344c01201aa2db7677004&wsc_sid=1428&wsc_cc=&wsc_isc=460002955191125&wsc_ldt=PRO%206%20Plus&wsc_imei=861250717112576&wsc_sp=52288&wsc_iip=10.0.2.15'
# if '?' in url:
#     re_url = re.compile(r'http[s]?://(.+?)\?(.*)')
#     new_url, parameter = re_url.match(url).groups()
#     url_dict['url'] = new_url
#     items = parameter.split('&')
#     for item in items:
#         name, value = item.split('=')
#         url_dict[name] = value
# print(url_dict)

# txt = "ClientPort:59019;EgressPort:58974"
# re_port = re.compile(r'ClientPort:(.+?);EgressPort:(.+)')
# src_port, dst_port = re_port.match(txt).groups()
# print(src_port, dst_port)

# txt = '2019-10-30T20:43:15.0815017+08:00'
# # re_port = re.compile(r'.+:(\d{2}.+?)\+.*')
# # src_port = re_port.match(txt).group(1)
# # print(src_port)
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
print(ran_str)