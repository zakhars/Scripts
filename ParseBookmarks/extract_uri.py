import sys
import datetime
from operator import itemgetter, attrgetter

def GetSortedUrlsJson(input_file):
    urls = []
    url_pattern = r'"uri": "'  # "uri": "http://smart-lab.ru/blog/offtop/165228.php"
    for line in input_file:
        urlp = line.find(url_pattern)
        if urlp != -1:
            urls.append(line[urlp + 8:-2])
    return sorted(urls)


def get_string_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def GetSortedUrlsHtml(input_file, sort_by):

    urls = []
    # <DT><A HREF="http://ya.ru/" ADD_DATE="1365481775" ICON="data:image/png;base64,xyz...">Яндекс</A>

    url_pattern1 = '<DT><A HREF="'
    url_pattern2 = '" ADD_DATE='

    date_pattern1 = 'ADD_DATE="'
    date_pattern2 = '" ICON='
    date_pattern2_alt = '">'

    content = input_file.readlines()
    for line in content:
        if line.find(url_pattern1) != -1:
            try:
                url = get_string_between(line, url_pattern1, url_pattern2)
                has_icon = (line.find(date_pattern2) != -1)
                date_s = get_string_between(line, date_pattern1, date_pattern2 if has_icon else date_pattern2_alt)
                date_readable = datetime.datetime.fromtimestamp(int(date_s))
                urls.append((url, date_readable))
            except Exception as ex:
                try:
                    print('Exception occurred for line (%s): %s' % (line, ex))
                except:
                    pass


    return sorted(urls, key = itemgetter(sort_by))


input_file = open(sys.argv[1], encoding="utf8")
sort_by = int(sys.argv[2])
#sorted_urls = GetSortedUrlsJson(input_file)
sorted_urls = GetSortedUrlsHtml(input_file, sort_by)
input_file.close()
if (sort_by == 0):
    for url, _ in sorted_urls:
        print(url)
else:
    for url, date in sorted_urls:
        print(date.strftime('%Y%m%d'), " ", url)
