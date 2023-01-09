import base64
import wave

wave_data = ''
with open('page_source.txt', 'r') as f:
    for line in f.readlines():
        wave_data += str(line.replace('\n', ''))

with open('indian.wav', 'wb') as f:
    f.write(base64.b64decode(wave_data))

with wave.open('indian.wav', 'rb') as f:
    with wave.open('indian1.wav', 'wb') as ff:
        ff.setparams(f.getparams())
        for i in range(f.getnframes()):
            ff.writeframes(f.readframes(1)[::-1])



