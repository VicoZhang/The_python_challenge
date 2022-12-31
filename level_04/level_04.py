import re

arr = ''
with open('./page_source.txt') as f:
    for s in f.readlines():
        arr += s.replace('\n', '')

# for s in range(len(arr[:-9])):
#     if ord('a') <= ord(arr[s]) <= ord('z'):
#         if ord('A') <= ord(arr[s+1]) <= ord('Z'):
#             if ord('A') <= ord(arr[s+2]) <= ord('Z'):
#                 if ord('A') <= ord(arr[s + 3]) <= ord('Z'):
#                     if ord('a') <= ord(arr[s + 4]) <= ord('z'):
#                         if ord('A') <= ord(arr[s + 5]) <= ord('Z'):
#                             if ord('A') <= ord(arr[s + 6]) <= ord('Z'):
#                                 if ord('A') <= ord(arr[s + 7]) <= ord('Z'):
#                                     if ord('a') <= ord(arr[s + 8]) <= ord('z'):
#                                         print(arr[s+4], end='')


pattern = r'[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]'
result = re.finditer(pattern, arr)
for item in result:
    print(item.group()[4], end='')

