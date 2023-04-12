x=int(input("Jerry's speed in m/s:"))
y=int(input("Tom's speed in m/s:"))
S=int(input("Starting distance between Tom and Jerry in metres:"))
if x<y:
    print("Tom will catch Jerry in", S//(y-x), "second(s)")
else:
    print("Tom will not catch Jerry")