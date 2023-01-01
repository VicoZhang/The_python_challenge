from zipfile import ZipFile

with ZipFile('./channel.zip') as f:
    file_num = '90052'
    while True:
        try:
            with f.open('{}.txt'.format(file_num)) as f1:
                res = f1.read().decode()
                file_num = res.split(' ')[-1]
                print(f.getinfo('{}.txt'.format(file_num)).comment.decode(), end='')
        except FileNotFoundError:
            break
        except KeyError:
            break
