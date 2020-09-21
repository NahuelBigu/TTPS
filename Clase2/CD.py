from sys import stdin, stdout
# CD UVA - 11849 
cdsJack, cdsJill= map(int, stdin.readline().strip().split())
while (cdsJack!=0 and cdsJill!=0):
    cdsBothOwn= set ()
    for _ in range(cdsJack+cdsJill):
        cdsBothOwn.add(int(stdin.readline().strip()))
    stdout.write(str((cdsJack+cdsJill)-len(cdsBothOwn))+"\n")
    cdsJack, cdsJill= map(int, stdin.readline().strip().split())