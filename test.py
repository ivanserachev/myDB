import datetime

f=open('/home/ivan/Documents/DB/val1::1::1000:::val2::4::998495:::val3::21::999738:::','rb')

st=datetime.datetime.now()
lines=f.readlines()
count=0
separator= [226, 128, 140]
for l in lines:
    ln = l.split(bytearray(separator))
    if str(1).encode('utf-8') in ln[0]:
        count+=1
print(count)
print(datetime.datetime.now()-st)