import os
import datetime
import sort
import shutil
import random

def run():
    date = datetime.date.today()
    try:
        path = str(date) + " test (" + str(random.randrange(1,10000)) + ")"
    except Exception as e:
        try:
            path = str(date) + " test (" + str(random.randrange(1,10000)) + ")"
        except Exception as e:
            print("test.........FAIL")


    os.mkdir(path)
    print(path)
    for i in range(1,50):
        img = open(path + "/" + str(i) + '.jpg', "w+")
        img.close
    # try:
    #     sort.run(path)
    #     print("test.........FAIL")
    # except Exception as e:
    #     print("test.........PASS")
    # shutil.rmtree(path)





if __name__ == '__main__':
    run()
