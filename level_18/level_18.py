import requests
import bz2
import urllib.parse as prs
import xmlrpc.client

# s = '12345'
# coos = ''

# for i in range(130):
#     url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(s)
#     res = requests.get(url)
#     s = res.text.split(' ')[-1]
#     coo = res.cookies
#     coos += coo.values()[0]
#     if not s.isnumeric():
#         break

# string = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA' \
#          '%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B' \
#          '%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
# new_string = string.replace('+', ' ')
# new_strings = prs.unquote_to_bytes(new_string)
# text = bz2.decompress(new_strings)
# print(text.decode())


# with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as pb:
#     print(pb.phone('Leopold'))

headers = {'Cookie': 'info=the flowers are on their way'}
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
print(requests.get(url, headers=headers).text)
