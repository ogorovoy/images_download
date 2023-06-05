import requests as requests


print('start program')
i=1
for i in range(72):
    print('dowload '+str(i))
    img_url = 'https://img.yumpu.com/8878904/'+str(i)+'/700x991/supplement-book-of-tennis-rackets-by-siegfried-kuebler.jpg'
    response = requests.get(img_url)
    if response.status_code:
        fp = open('foto'+str(i)+'.png', 'wb')
        fp.write(response.content)
        fp.close()

print('the End')