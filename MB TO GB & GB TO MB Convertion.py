def mbgb():
    #MB to GB
    k = float(input("MB To GB : "))
    GB = k/1024

    if GB <= 1:
        GB = format(k / 1024, '.2f')
        print(GB,"GB")
    else:
        GB = format(k / 1024, '.2f')
        print(GB, "GB")
mbgb()
#MB To GB
def gbmb():
    j = float(input("GB To MB : "))
    MB = format(j*1024, ".0f")
    print(MB, "MB")

gbmb()
