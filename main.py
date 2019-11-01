import json
import re
import random
import string
import get_app_name
# get the feature


class Get():

    def get_all_dict(self, path):
        with open(inpath, encoding='utf-8-sig') as fObj:
            the_dict = json.loads(fObj.read(), strict=False)
        all_dict = dict()
        for each_list in the_dict['log']['entries']:
            end_dict, time, date = self.get_each_item(each_list)
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
            dict_name = str(date) + '.' + str(time) + ',' + ran_str
            all_dict[dict_name] = end_dict

        return all_dict

    def get_each_item(self, alist):
        # print(requestList)
        time = alist['time']
        start_time = alist['startedDateTime']
        date = self.analysis_date(start_time)
        connection = alist['connection']
        src_port, dst_port = self.analysis_port(connection)

        requestList = alist['request']
        headersSize = requestList['headersSize']
        postData = requestList['postData']

        if 'params' in postData.keys():
            params = postData['params']
            params_dict = self.analysis_list(params)
            postData['params'] = params_dict

        queryString = requestList['queryString']
        query_dict = self.analysis_list(queryString)

        headers = requestList['headers']
        headers_dict = self.analysis_list(headers)

        bodySize = requestList['bodySize']
        url = requestList['url']
        url_dict, domain, host = self.analysis_url(url)

        # print(url_dict)
        cookies = requestList['cookies']
        method = requestList['method']
        timings = alist['timings']

        # creat new json
        end_dict = dict()
        end_dict['src_port'] = src_port
        end_dict['dst_port'] = dst_port
        end_dict['host'] = host
        end_dict['domain'] = domain
        end_dict['headersSize'] = headersSize
        end_dict['headers'] = headers_dict
        end_dict['postData'] = postData
        end_dict['queryString'] = query_dict
        end_dict['bodySize'] = bodySize
        end_dict['url'] = url_dict
        end_dict['cookies'] = cookies
        end_dict['method'] = method
        end_dict['timings'] = timings

        return end_dict, time, date

    @staticmethod
    def analysis_value_list(data):
        value_dict = dict()
        new_data = json.loads(data, encoding='utf-8-sig')
        items = new_data[0].items()
        for key, value in items:
            value_dict[key] = value
        return value_dict

    def analysis_list(self, list):
        now_dict = dict()
        for item in list:
            if '[{' not in item['value']:
                now_dict[item['name']] = item['value']
            else:
                new_dict = self.analysis_value_list(item['value'])
                now_dict[item['name']] = new_dict
        return now_dict

    @staticmethod
    def analysis_url(url):
        url_dict = dict()
        re_domain = re.compile(r'.*\.(.+?\..*)')
        re_host = re.compile(r'http[s]?://(.+?)/')

        host = re_host.match(url).group(1)
        domain = re_domain.match(host).group(1)
        if '?' in url:
            re_url = re.compile(r'http[s]?://(.+?)\?(.*)')
            new_url, parameter = re_url.match(url).groups()
            url_dict['url'] = new_url
            items = parameter.split('&')
            for item in items:
                name, value = item.split('=')
                url_dict[name] = value

        return url_dict, domain, host

    @staticmethod
    def analysis_port(connection):
        re_port = re.compile(r'ClientPort:(.+?);EgressPort:(.+)')
        src_port, dst_port = re_port.match(connection).groups()
        return src_port, dst_port

    @staticmethod
    def analysis_date(date):
        re_time = re.compile(r'.+:(\d{2}.+?)\+.*')
        date = re_time.match(date).group(1)
        return date

    @staticmethod
    def write_json(json_):
        json_str = json.dumps(json_)
        name = get_app_name.get_package_name()

        path = 'F:\\Review\\capture\\' + str(name[0]) + '.json'
        with open(path, 'w') as json_file:
            json_file.write(json_str)


if __name__ == "__main__":
    inpath = "F:\\Review\\capture\\newone.har"
    get = Get()
    all_dict = get.get_all_dict(inpath)
    get.write_json(all_dict)
