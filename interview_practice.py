def isUnique(string):
    s = set(string)
    if (len(s)==len(string)):
        print("True")
    else:
         print("False")


def perm(string1, string2):
    if len(string1) != len(string2):
        return False

    string1_sorted = ''.join(sorted(string1))
    string2_sorted = ''.join(sorted(string2))

    for i in range(len(string1_sorted)):
        if (string1_sorted[i] != string2_sorted[i]):
            return False
    #else
    return True

def stringRotation(s1, s2):
    new_s1 = s1 + s1
    if s2 in new_s1:
        return True
    else:
        return False

def getBit(num, i):
    return ((num & (1 << i)) !=0)


def print_power_set(l):
    num = len(l)
    subseq = set()
    for i in range(2**num):
        power = ""
        for j in range(num):
            element = l[j]
            b = ((i >> j) & 1)
            
            if b:
                power+=element
                subseq.add(power)
        
            #else continue


    print(sorted(subseq))



def insertion(N, M, i, j):
    for pos in range(i, j+1):
        #get bit from M:
        value = ((M >> pos) & 1)
        b = 0
        #clear & update the bit at pos:
        mask = ~(1 << pos)
        b |= (N & mask) | (value << pos)

    return b





       
    

def main():
    print_power_set("ba")


main()

