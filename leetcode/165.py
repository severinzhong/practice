def compareVersion(version1,version2):
    while version1 and version2: 
        i = j = 0
        while i<len(version1) and version1[i]!='.' :
            i += 1
        while j<len(version2) and version2[j]!='.' :
            j+= 1
        v1 = version1[:i]
        v2 = version2[:j]
        while v1 and v1[0] == '0' :
            v1 = v1[1:]
        while v2 and v2[0] == '0' :
            v2 = v2[1:]
        if v1 :
            n1 = int(v1)
        else :
            n1 = 0
        if v2 :
            n2 = int(v2)
        else :
            n2 = 0
        if n1>n2:
            return 1
        if n1<n2 :
            return -1
        version1 = version1[i+1:]
        version2 = version2[j+1:]
    if version1 :
        for x in [str(x) for x in range(1,10)] :
            if x in version1 :
                return 1
    if version2 :
        for x in [str(x) for x in range(1,10)] :
            if x in version2 :
                return -1
    return 0
if __name__ == '__main__' :
    print(compareVersion("19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000",
"19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000"))