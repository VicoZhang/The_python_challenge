import base64
import requests
import re


# def get_unreal(start, end=''):
#     url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
#     Authorization = format(base64.b64encode(b'butter:fly').decode())
#     headers = {'Range': 'bytes=%s-%s' % (start, end),  # end可以不传
#                'Authorization': 'Basic %s' % Authorization}
#     response = requests.request("GET", url, headers=headers)
#     data = response.content
#     if data:
#         print(response.content)
#         return response.headers['Content-Range']
#     else:
#         return False
#
#
# def get_Info(start=30203):
#     while True:
#         contentRange = get_unreal(start)
#         if contentRange:
#             reg = re.compile('-(.*)/')
#             start = reg.findall(str(contentRange))
#             start = int(''.join(start))+1
#         else:
#             break
#
#
# def get_Reverse(start=2123456789):
#     while True:
#         contentRange = get_unreal(start)
#         if contentRange:
#             reg = re.compile('bytes (.*)-')
#             start = reg.findall(str(contentRange))
#             start = int(''.join(start))-1
#         else:
#             break


# get_Reverse(start=2123456789)

# msg = 'esrever ni emankcin wen ruoy si drowssap eht'
# print(msg[::-1])

# url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
# Authorization = format(base64.b64encode(b'butter:fly').decode())
# headers = {
#     'Range': 'bytes=1152983631-',
#     'Authorization': 'Basic %s' % Authorization}
# response = requests.request("GET", url, headers=headers)
# h = open("data.zip", "wb")
# h.write(response.content)
# h.close()


