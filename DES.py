def _circularLeftShift(lst: list, n: int)->list:
    length = len(lst)
    
    n = n % length
    
    return lst[n:] + lst[:n]

def _PC1(key:list)->list:
    PC1_C0 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36]
    PC1_D0 = [63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    
    C0 = []
    D0 = []
    for i in range(0,28):
        C0.append(key[PC1_C0[i]-1])
        D0.append(key[PC1_D0[i]-1])
    return C0, D0

def _PC2(C0: list, D0: list)->list:
    C0D0 = C0 + D0
    
    PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,
           52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
    
    key_i = []
    
    for i in range(0,48):
        key_i.append(C0D0[PC2[i]-1])
    
    return key_i

def keySchedule(key:list)->list:
    v = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    C0, D0 = _PC1(key)
    Ci = C0
    Di = D0
    subKeys = []
    for i in range(0,16):
        
        Ci = _circularLeftShift(Ci,v[i])
        Di = _circularLeftShift(Di, v[i])
        
        Ki = _PC2(Ci, Di)
        # print(''.join(map(str, Ki)))
        subKeys.append(Ki)
        
    
    return subKeys

def _IP(plainText:list)->list:
    
    IP_L0 = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8]
    IP_R0 = [57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
    
    L0 = []
    R0 = []
    for i in range(0,32):
        L0.append(plainText[IP_L0[i]-1])
        R0.append(plainText[IP_R0[i]-1])
    
    return L0, R0

def _expand_function(R: list)->list:
    
    E = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
    
    T = []
    
    for i in E:
        T.append(R[i-1])
        
    return T

def _XOR(a:list, b:list)->list:
    
    result = []
    length = len(a)
    
    for i in range(0,length):
        result.append(a[i]^b[i])
    return result

def _split(lst:list, n:int) -> list:
    length = len(lst)
    
    sublist_size = length // n
    
    reminder = length % n
    
    sublists = []
    
    start = 0
    
    for i in range(n):
        end = start + sublist_size + (1 if i < reminder else 0)
        sublists.append(lst[start:end])
        start = end 
    return sublists

def _binary_str_to_list(binary_str:str)->list:
    return [int(bit) for bit in binary_str]

def _S1(B:list)->list:
    S1 = [
    ['1110', '0100', '1101', '0001', '0010', '1111', '1011', '1000', '0011', '1010', '0110', '1100', '0101', '1001', '0000', '0111'],
    ['0000', '1111', '0111', '0100', '1110', '0010', '1101', '0001', '1010', '0110', '1100', '1011', '1001', '0101', '0011', '1000'],
    ['0100', '0001', '1110', '1000', '1101', '0110', '0010', '1011', '1111', '1100', '1001', '0111', '0011', '1010', '0101', '0000'],
    ['1111', '1100', '1000', '0010', '0100', '1001', '0001', '0111', '0101', '1011', '0011', '1110', '1010', '0000', '0110', '1101'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S1[row][column])

def _S2(B:list)->list:
    S2 = [
    ['1111', '0001', '1000', '1110', '0110', '1011', '0011', '0100', '1001', '0111', '0010', '1101', '1100', '0000', '0101', '1010'],
    ['0011', '1101', '0100', '0111', '1111', '0010', '1000', '1110', '1100', '0000', '0001', '1010', '0110', '1001', '1011', '0101'],
    ['0000', '1110', '0111', '1011', '1010', '0100', '1101', '0001', '0101', '1000', '1100', '0110', '1001', '0011', '0010', '1111'],
    ['1101', '1000', '1010', '0001', '0011', '1111', '0100', '0010', '1011', '0110', '0111', '1100', '0000', '0101', '1110', '1001'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S2[row][column])

def _S3(B:list)->list:
    S3 = [
    ['1010', '0000', '1001', '1110', '0110', '0011', '1111', '0101', '0001', '1101', '1100', '0111', '1011', '0100', '0010', '1000'],
    ['1101', '0111', '0000', '1001', '0011', '0100', '0110', '1010', '0010', '1000', '0101', '1110', '1100', '1011', '1111', '0001'],
    ['1101', '0110', '0100', '1001', '1000', '1111', '0011', '0000', '1011', '0001', '0010', '1100', '0101', '1010', '1110', '0111'],
    ['0001', '1010', '1101', '0000', '0110', '1001', '1000', '0111', '0100', '1111', '1110', '0011', '1011', '0101', '0010', '1100'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S3[row][column])

def _S4(B:list)->list:
    S4 = [
    ['0111', '1101', '1110', '0011', '0000', '0110', '1001', '1010', '0001', '0010', '1000', '0101', '1011', '1100', '0100', '1111'],
    ['1101', '1000', '1011', '0101', '0110', '1111', '0000', '0011', '0100', '0111', '0010', '1100', '0001', '1010', '1110', '1001'],
    ['1010', '0110', '1001', '0000', '1100', '1011', '0111', '1101', '1111', '0001', '0011', '1110', '0101', '0010', '1000', '0100'],
    ['0011', '1111', '0000', '0110', '1010', '0001', '1101', '1000', '1001', '0100', '0101', '1011', '1100', '0111', '0010', '1110'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S4[row][column])

def _S5(B:list)->list:
    S5 = [
    ['0010', '1100', '0100', '0001', '0111', '1010', '1011', '0110', '1000', '0101', '0011', '1111', '1101', '0000', '1110', '1001'],
    ['1110', '1011', '0010', '1100', '0100', '0111', '1101', '0001', '0101', '0000', '1111', '1010', '0011', '1001', '1000', '0110'],
    ['0100', '0010', '0001', '1011', '1010', '1101', '0111', '1000', '1111', '1001', '1100', '0101', '0110', '0011', '0000', '1110'],
    ['1011', '1000', '1100', '0111', '0001', '1110', '0010', '1101', '0110', '1111', '0000', '1001', '1010', '0100', '0101', '0011'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S5[row][column])

def _S6(B:list)->list:
    S6 = [
    ['1100', '0001', '1010', '1111', '1001', '0010', '0110', '1000', '0000', '1101', '0011', '0100', '1110', '0111', '0101', '1011'],
    ['1010', '1111', '0100', '0010', '0111', '1100', '1001', '0101', '0110', '0001', '1101', '1110', '0000', '1011', '0011', '1000'],
    ['1001', '1110', '1111', '0101', '0010', '1000', '1100', '0011', '0111', '0000', '0100', '1010', '0001', '1101', '1011', '0110'],
    ['0100', '0011', '0010', '1100', '1001', '0101', '1111', '1010', '1011', '1110', '0001', '0111', '0110', '0000', '1000', '1101'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S6[row][column])

def _S7(B:list)->list:
    S7 = [
    ['0100', '1011', '0010', '1110', '1111', '0000', '1000', '1101', '0011', '1100', '1001', '0111', '0101', '1010', '0110', '0001'],
    ['1101', '0000', '1011', '0111', '0100', '1001', '0001', '1010', '1110', '0011', '0101', '1100', '0010', '1111', '1000', '0110'],
    ['0001', '0100', '1011', '1101', '1100', '0011', '0111', '1110', '1010', '1111', '0110', '1000', '0000', '0101', '1001', '0010'],
    ['0110', '1011', '1101', '1000', '0001', '0100', '1010', '0111', '1001', '0101', '0000', '1111', '1110', '0010', '0011', '1100'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S7[row][column])

def _S8(B:list)->list:
    S8 = [
    ['1101', '0010', '1000', '0100', '0110', '1111', '1011', '0001', '1010', '1001', '0011', '1110', '0101', '0000', '1100', '0111'],
    ['0001', '1111', '1101', '1000', '1010', '0011', '0111', '0100', '1100', '0101', '0110', '1011', '0000', '1110', '1001', '0010'],
    ['0111', '1011', '0100', '0001', '1001', '1100', '1110', '0010', '0000', '0110', '1010', '1101', '1111', '0011', '0101', '1000'],
    ['0010', '0001', '1110', '0111', '0100', '1010', '1000', '1101', '1111', '1100', '1001', '0000', '0011', '0101', '0110', '1011'],
]

    
    row = int(str(B[0]) + str(B[5]), 2)
    column = int(''.join(map(str, B[1:5])), 2)
    return _binary_str_to_list(S8[row][column])

def _P(T:list)->list:
    
    P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
    
    result = []
    
    for i in range (0, 32):
        result.append(T[P[i]-1])
    
    return result

def _F_function(R:list, key:list)->list:
    
    T1 = _expand_function(R)
    
    T2 = _split(_XOR(T1, key),8)

    T3 = _S1(T2[0])+_S2(T2[1])+_S3(T2[2])+_S4(T2[3])+_S5(T2[4])+_S6(T2[5])+_S7(T2[6])+_S8(T2[7])
    
    T4 = _P(T3)
    
    return T4


def _IP1(RL:list)->list:
    
    IP1 = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
    
    result = []
    
    for i in range(0,64):
        result.append(RL[IP1[i]-1])

    return result

def DES(key, plainText)->list:
    
    subKeys = keySchedule(key)

    P_L,P_R = _IP(plainText)
    
    for i in range(0,16):
        Li = P_R
        F = _F_function(P_R,subKeys[i])

        Pi = _XOR(P_L, F)

        P_L = Li
        P_R = Pi
        
    RL = P_R + P_L
    
    return ''.join(map(str,_IP1(RL)))
    


key =       [0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,0,1]
plainText = [0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1]

Cipher = DES(key, plainText)
print(Cipher)
print(hex(int(Cipher, 2))[2:].upper())



