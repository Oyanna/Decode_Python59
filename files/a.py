try:
    somefile = open("hello.txt", "a")
    try:
        somefile.write("hello")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
