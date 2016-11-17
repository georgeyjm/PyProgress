import pyprogress
import time

count = 12

progressBar = pyprogress.bar(count)
for i in range(count):
    time.sleep(0.5) #Work Here
    progressBar.update()
