with open("test.txt", mode="w", encoding = "utf-8") as mf:
    mf.write("This is a test file.\n")
with open("test.txt", mode="r", encoding = "utf-8") as mf:
    print(mf.read())