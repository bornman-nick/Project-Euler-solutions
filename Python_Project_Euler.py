# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:56:52 2018

@author: nickbornman
"""

import math
# important package used for even the most basic mathematics

import numpy as np
# important package usually needed to deal with arrays

import itertools

import datetime as dt
# package I use to time operations

import random
# package to generate random numbers

import re
# use package to read files

from collections import Counter

import sympy
# SymPy is a Python library for symbolic mathematics


"""IMPORTANT FUNCTIONS I COULD USE, BUT ARE DEFINITELY NOT THE MOST EFFICIENT"""

def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        if n % 2 == 0:
            return False
        else:
            for i in range(3,int(math.sqrt(n)) + 3,2):
                if n % i == 0:
                    return False
                    break
            else:
                return True

def trial_division(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
        n = int(n)
    f = 3
    while f**2 <= n:
        if n % f == 0:
            a.append(f)
            n /= f
            n = int(n)
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a



"""Problem 1"""



answer_1 = sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0])

print("Problem 1 answer: ", answer_1)



"""Problem 2"""



list_2 = [1,2]

while list_2[-1] < 4000000:
    list_2.append(list_2[-1] + list_2[-2])
    
answer_2 = sum([i for i in list_2 if i % 2 == 0])

print("Problem 2 answer: ", answer_2)



"""Problem 3"""



list_3 = [i for i in range(2,round(math.sqrt(600851475143)) + 1) if 600851475143 % i == 0 and is_prime(i)]

answer_3 = max(list_3)

print("Problem 3 answer: ", answer_3)



"""Problem 4"""



list_4 = []

for i in range(1,1000):
    for j in range(1,1000):
        num = str(i*j)
        if len(num) % 2 == 1:
            for k in range(0,int((len(num) - 1)/2)):
                if num[k] != num[-(k+1)]:
                    break
            else:
                list_4.append((i,j,int(num)))
        elif len(num) % 2 == 0:
            for k in range(0,int(len(num)/2)):
                if num[k] != num[-(k+1)]:
                    break
            else:
                list_4.append((i,j,int(num)))
                
answer_4 = max([list_4[i][2] for i in range(len(list_4))])

print("Problem 4 answer: ", answer_4)        



"""Problem 5"""



bool_val = True

i = 2520

while bool_val:
    for j in [11,12,13,14,15,16,17,18,19]:
        if i % j != 0:
            i += 20
            break
    else:
        bool_val = False

answer_5 = i

print("Problem 5 answer: ", answer_5)



"""Problem 6"""



sum_of_squares = sum([i**2 for i in range(1,101)])

square_of_sum = sum([i for i in range(1,101)])**2

answer_6 = square_of_sum - sum_of_squares

print("Problem 6 answer: ", answer_6)



"""Problem 7"""



list_7 = []

j = 1

while len(list_7) <= 10000:
    if is_prime(j):
        list_7.append(j)
        j += 1
    else:
        j += 1

answer_7 = list_7[-1]

print("Problem 7 answer: ", answer_7)



"""Problem 8"""



num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

def prod_of_digits(n):
    init = 1
    list_8 = []
    for i in range(0,len(str(num)) - n + 1):
        calc = 1
        for j in str(num)[i:i + n]:
            calc *= int(j)
        if calc >= init:
            list_8.clear()
            list_8.append((str(num)[i:i + n],calc))
            init = calc
    return list_8
            
answer_8 = prod_of_digits(13)[-1][-1]

print("Problem 8 answer: ", answer_8)



"""Problem 9"""



bool_9 = False

list_9 = []

for c in range(3,1001):
    for b in range(2,c):
        for a in range(1,b):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                list_9.append((a,b,c))
                bool_9 = True
                break
        if bool_9:
            break
    if bool_9:
        break
    
answer_9 = a*b*c

print("Problem 9 answer: ", answer_9)           



"""Problem 10"""



list_10 = [i for i in range(1,2000000,2) if is_prime(i)]                
                
answer_10 = sum(list_10) + 2

print("Problem 10 answer: ", answer_10)               
          
      

"""Problem 11"""



long_list = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8,
49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0,
81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65,
52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91,
22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,
24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,
32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,
67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21,
24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,
21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95,
78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92,
16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57,
86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,
19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40,
4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,
88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,
4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36,
20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16,
20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54,
1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
                         
grid = np.reshape(long_list,(20,20))

list_11 = []

for i in range(0,20):
    for j in range(0,20 - 4 + 1):
        list_11.append(grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3])
        list_11.append(grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i])
        
for i in range(0,20 - 4 + 1):
    for j in range(0,20 - 4 + 1):
        list_11.append(grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3])
        list_11.append(grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j])
        
answer_11 = max(list_11)    

print("Problem 11 answer: ", answer_11) 



"""Problem 12"""



answer_12 = 0

n = 1

while answer_12 == 0:
    num_of_div = 0
    s = int((n*(n+1))/2)
    for j in range(1,int(math.sqrt(s)) + 1):
        if s % j == 0 and j != s/j:
            num_of_div += 2
        elif s % j == 0:
            num_of_div += 1
    n += 1
    if num_of_div > 500:
        answer_12 = s
        
print("Problem 12 answer: ", s, "(number of divisors: ", num_of_div,")")



"""Problem 13"""



list_numbers = [37107287533902102798797998220837590246510135740250,
46376937677490009712648124896970078050417018260538,
74324986199524741059474233309513058123726617309629,
91942213363574161572522430563301811072406154908250,
23067588207539346171171980310421047513778063246676,
89261670696623633820136378418383684178734361726757,
28112879812849979408065481931592621691275889832738,
44274228917432520321923589422876796487670272189318,
47451445736001306439091167216856844588711603153276,
70386486105843025439939619828917593665686757934951,
62176457141856560629502157223196586755079324193331,
64906352462741904929101432445813822663347944758178,
92575867718337217661963751590579239728245598838407,
58203565325359399008402633568948830189458628227828,
80181199384826282014278194139940567587151170094390,
35398664372827112653829987240784473053190104293586,
86515506006295864861532075273371959191420517255829,
71693888707715466499115593487603532921714970056938,
54370070576826684624621495650076471787294438377604,
53282654108756828443191190634694037855217779295145,
36123272525000296071075082563815656710885258350721,
45876576172410976447339110607218265236877223636045,
17423706905851860660448207621209813287860733969412,
81142660418086830619328460811191061556940512689692,
51934325451728388641918047049293215058642563049483,
62467221648435076201727918039944693004732956340691,
15732444386908125794514089057706229429197107928209,
55037687525678773091862540744969844508330393682126,
18336384825330154686196124348767681297534375946515,
80386287592878490201521685554828717201219257766954,
78182833757993103614740356856449095527097864797581,
16726320100436897842553539920931837441497806860984,
48403098129077791799088218795327364475675590848030,
87086987551392711854517078544161852424320693150332,
59959406895756536782107074926966537676326235447210,
69793950679652694742597709739166693763042633987085,
41052684708299085211399427365734116182760315001271,
65378607361501080857009149939512557028198746004375,
35829035317434717326932123578154982629742552737307,
94953759765105305946966067683156574377167401875275,
88902802571733229619176668713819931811048770190271,
25267680276078003013678680992525463401061632866526,
36270218540497705585629946580636237993140746255962,
24074486908231174977792365466257246923322810917141,
91430288197103288597806669760892938638285025333403,
34413065578016127815921815005561868836468420090470,
23053081172816430487623791969842487255036638784583,
11487696932154902810424020138335124462181441773470,
63783299490636259666498587618221225225512486764533,
67720186971698544312419572409913959008952310058822,
95548255300263520781532296796249481641953868218774,
76085327132285723110424803456124867697064507995236,
37774242535411291684276865538926205024910326572967,
23701913275725675285653248258265463092207058596522,
29798860272258331913126375147341994889534765745501,
18495701454879288984856827726077713721403798879715,
38298203783031473527721580348144513491373226651381,
34829543829199918180278916522431027392251122869539,
40957953066405232632538044100059654939159879593635,
29746152185502371307642255121183693803580388584903,
41698116222072977186158236678424689157993532961922,
62467957194401269043877107275048102390895523597457,
23189706772547915061505504953922979530901129967519,
86188088225875314529584099251203829009407770775672,
11306739708304724483816533873502340845647058077308,
82959174767140363198008187129011875491310547126581,
97623331044818386269515456334926366572897563400500,
42846280183517070527831839425882145521227251250327,
55121603546981200581762165212827652751691296897789,
32238195734329339946437501907836945765883352399886,
75506164965184775180738168837861091527357929701337,
62177842752192623401942399639168044983993173312731,
32924185707147349566916674687634660915035914677504,
99518671430235219628894890102423325116913619626622,
73267460800591547471830798392868535206946944540724,
76841822524674417161514036427982273348055556214818,
97142617910342598647204516893989422179826088076852,
87783646182799346313767754307809363333018982642090,
10848802521674670883215120185883543223812876952786,
71329612474782464538636993009049310363619763878039,
62184073572399794223406235393808339651327408011116,
66627891981488087797941876876144230030984490851411,
60661826293682836764744779239180335110989069790714,
85786944089552990653640447425576083659976645795096,
66024396409905389607120198219976047599490197230297,
64913982680032973156037120041377903785566085089252,
16730939319872750275468906903707539413042652315011,
94809377245048795150954100921645863754710598436791,
78639167021187492431995700641917969777599028300699,
15368713711936614952811305876380278410754449733078,
40789923115535562561142322423255033685442488917353,
44889911501440648020369068063960672322193204149535,
41503128880339536053299340368006977710650566631954,
81234880673210146739058568557934581403627822703280,
82616570773948327592232845941706525094512325230608,
22918802058777319719839450180888072429661980811197,
77158542502016545090413245809786882778948721859617,
72107838435069186155435662884062257473692284509516,
20849603980134001723930671666823555245252804609722,
53503534226472524250874054075591789781264330331690]

num_13 = 0

k = 0

for i in range(0,5):
    for j in range(len(list_numbers)):
        num_13 += int(str(list_numbers[j])[50 - 10*i - 10:50 - 10*i])
    k = num_13
    num_13 = 0
    if i == 4:
        k = int(str(k)[:10])
        break
    if len(str(k)) > 10:
        k = int(str(k)[:len(str(k)) - 10])
        num_13 += k

answer_13 = k

print("Problem 13 answer: ", answer_13)



"""Problem 14"""



collatz_numbers_list = []

for i in range(1,1000000):
    num_14 = 1
    j = i
    while j != 1:
        if j % 2 == 0:
            j /= 2
        else:
            j = 3*j + 1
        num_14 += 1
    collatz_numbers_list.append(num_14)

answer_14 = collatz_numbers_list.index(max(collatz_numbers_list)) + 1

print("Problem 14 answer: ", answer_14)



"""Problem 15"""



dict_15 = {0:1}

num_of_sides_15 = 20

for i in range(1,(num_of_sides_15 + 1)**2):
    dict_15[i] = 0
    
list_of_points_15 = [i for i in range(0,(num_of_sides_15 + 1)**2)]

# print(np.reshape(list_of_points_15,(num_of_sides_15 + 1,num_of_sides_15 + 1)))

list_of_right_edge_15 = [i for i in list_of_points_15 if (i + 1) % (num_of_sides_15 + 1) == 0 and i != (num_of_sides_15 + 1)**2 - 1]

list_of_lower_edge_15 = [i for i in range((num_of_sides_15 + 1)**2 - (num_of_sides_15+ 1),(num_of_sides_15 + 1)**2 - 1)]

list_of_edges_15 = list_of_right_edge_15 + list_of_lower_edge_15

for key in dict_15:
    if dict_15[key] != 0 and key not in list_of_edges_15 and key != ((num_of_sides_15 + 1)**2 - 1):
        dict_15[key + 1] += dict_15[key]
        dict_15[key + num_of_sides_15 + 1] += dict_15[key]
    elif dict_15[key] != 0 and key in list_of_right_edge_15 and key != ((num_of_sides_15 + 1)**2 - 1):
        dict_15[key + num_of_sides_15 + 1] += dict_15[key]
    elif dict_15[key] != 0 and key in list_of_lower_edge_15 and key != ((num_of_sides_15 + 1)**2 - 1):
        dict_15[key + 1] += dict_15[key]
    if key == ((num_of_sides_15 + 1)**2 - 1):
        break

print("Problem 15 answer: ", dict_15[((num_of_sides_15 + 1)**2 - 1)])



"""Problem 16"""



num_16 = 2**1000

answer_16 = 0

for item in str(num_16):
    answer_16 += int(item)
    
print("Problem 16 answer: ", answer_16)
    


"""Problem 17"""



Numbers_sub_20 = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

Tens_sub_100 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def num_to_word(n):
    if 1 <= n < 20:
        return Numbers_sub_20[n]
    elif 20 <= n < 100:
        return Tens_sub_100[int(n/10)-2] + Numbers_sub_20[n % 10]
    elif 100 <= n < 1000:
        if n in [100,200,300,400,500,600,700,800,900]:
            return Numbers_sub_20[int(n/100)] + "hundred"
        if 0 <= int(str(n)[1:]) < 20:
            return Numbers_sub_20[int(n/100)] + "hundredand" + Numbers_sub_20[int(str(n)[1:])]
        elif 20 <= int(str(n)[1:]) < 100:
            return Numbers_sub_20[int(n/100)] + "hundredand" + Tens_sub_100[(int(n/10) % 10) - 2] + Numbers_sub_20[(n % 100) % 10]
    elif n == 1000:
        return "onethousand"
        
answer_17 = 0

for i in range(1,1001):
    answer_17 += len(num_to_word(i))

print("Problem 17 answer: ", answer_17)



"""Problem 18"""



triangle_18 = [(75),(95,64),(17,47,82),(18,35,87,10),(20,4,82,47,65),(19,1,23,75,3,34),(88,2,77,73,7,63,67),(99,65,4,28,6,16,70,92),(41,41,26,56,83,40,80,70,33),(41,48,72,33,47,32,37,16,94,29),(53,71,44,65,25,43,91,52,97,51,14),(70,11,33,28,77,73,17,78,39,68,17,57),(91,71,52,38,17,14,91,43,58,50,27,29,48),(63,66,4,68,89,53,67,30,73,16,69,87,40,31),(4,62,98,27,23,9,70,98,73,93,38,53,60,4,23)]

list_18 = [0]

for i in range(1,len(triangle_18)):
    new_list_18 = []
    for j in range(0,len(triangle_18[i])):
        upper_limit_18 = int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
        if j == 0 or j == 1:
            l = 0
        else:
            l += int(math.factorial(i-1)/(math.factorial(j-2)*math.factorial(i-j+1)))
        for k in range(0,upper_limit_18):
            new_list_18.append(list_18[k + l] + triangle_18[i][j])
    list_18 = new_list_18

answer_18 = max(list_18) + 75
        
print("Problem 18 answer: ", answer_18)


"""More efficient way


triangle_18 = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

triangle_18.reverse()

for i in range(0,len(triangle_18)-1):
    for j in range(0,len(triangle_18[i+1])):
        triangle_18[i+1][j] += max(triangle_18[i][j],triangle_18[i][j+1])

answer_18 = triangle_18[-1][0]    

print("Problem 18 answer: ", answer_18)

"""



"""Problem 19"""



start_date_19 = dt.datetime(1901,1,1)

end_date_19 = dt.datetime(2000,12,31)

start_date_sunday_19 = start_date_19 + dt.timedelta(days=5)

day_difference = end_date_19 - start_date_sunday_19

day_index = start_date_sunday_19

answer_19 = 0

while (day_index - start_date_sunday_19) <= day_difference:
    if day_index.weekday() == 6 and day_index.day == 1:
        answer_19 += 1
    day_index = day_index + dt.timedelta(days=7)
    
print("Problem 19 answer: ", answer_19)



"""Problem 20"""



num_20 = math.factorial(100)

answer_20 = 0

for i in str(num_20):
    answer_20 += int(i)

print("Problem 20 answer: ", answer_20)
    
    

"""Problem 21"""



answer_21 = 0

def d(n):
    sum_21 = 0
    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            sum_21 += i
    return sum_21

for i in range(1,10001):
    if d(d(i)) == i and i != d(i):
        answer_21 += i
        
print("Problem 21 answer: ", answer_21)    



"""Problem 22"""



dict_letters_22 = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

def alpha_value(s):
    value_22 = 0
    for letter in s:
        value_22 = value_22 + dict_letters_22[letter]
    return value_22

with open("C:\\Users\\Public\\Documents\\Python Scripts\\Project_Euler\\p022_names.txt","r") as file:
    for line in file:
        list_names_22 = sorted(line.replace('"','').split(","))

answer_22 = 0

for i in range(0,len(list_names_22)):
    answer_22 += alpha_value(list_names_22[i])*(i+1)

print("Problem 22 answer: ", answer_22)



"""Problem 23"""



def sum_proper_divisors(n):
    sum_23 = 0
    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            sum_23 += i
    return sum_23

list_abundant_numbers_23 = [i for i in range(1,28124) if sum_proper_divisors(i) > i]

list_sum_abundant_numbers_23 = list(set([i + j for i in list_abundant_numbers_23 for j in list_abundant_numbers_23 if i + j <= 28123]))

answer_23 = int(((28123)*(28124/2)) - sum(list_sum_abundant_numbers_23))

print(answer_23)



"""Problem 24"""



list_24 = list(itertools.permutations(['0','1','2','3','4','5','6','7','8','9']))

list_nums_24 = sorted(list(map(lambda x: "".join(x),list_24)))

answer_24 = list_nums_24[999999]

print("Problem 24 answer: ", answer_24)



"""Problem 25"""



def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        fib1 = 1
        fib2 = 1
        i = 3
        num_25 = fib1 + fib2
        while i < n:
            fib2 = fib1
            fib1 = num_25
            num_25 = fib1 + fib2
            i += 1
    return num_25

answer_25 = 1

while len(str(fib(answer_25))) < 1000:
    answer_25 += 1

print("Problem 25 answer: ", answer_25)



"""Problem 26"""



# I couldn't for the life of me figure out why my mult_order function wasn't working, so I just
# decided to use an equivalent function from the Sympy package called n_order

def mult_order(a,n):
    k = 1
    while ((a**k) % n) != 1:
        k += 1
    return k

def LCM_list(a):
    lcm = a[0]
    if len(a) == 1:
        return lcm
    else:
        for i in a[1:]:
            lcm = int((lcm*i)/(math.gcd(lcm, i)))
        return lcm

def repetend_length(n):
    dict_period = {}
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return 0
    dict_temp = dict(Counter(trial_division(n)))
    for key in dict_temp:
        if (key % 3) == 0:
            dict_period[key] = sympy.ntheory.n_order(10,3)
        elif (key % 487) == 0:
            dict_period[key] = sympy.ntheory.n_order(10,487)
        elif (key % 56598313) == 0:
            dict_period[key] = sympy.ntheory.n_order(10,56598313)
        else:
            dict_period[key] = (key**(dict_temp[key] - 1))*sympy.ntheory.n_order(10,key)
    return LCM_list(list(dict_period.values()))

length_26 = 0

answer_26 = 0

for num in range(1,1001):
    rep_temp = repetend_length(num)
    if rep_temp > length_26:
        length_26 = rep_temp
        answer_26 = num

print("Problem 26 answer: ", answer_26)



"""Problem 27"""



answer_list_27 = (0,0,0)

for a in range(-999,1000,1):
    for b in range(-999,1000,1):
        n = 0
        num_of_primes_27 = 0
        while is_prime(n**2 + a*n + b):
            num_of_primes_27 += 1
            n += 1
        if num_of_primes_27 > answer_list_27[-1]:
            answer_list_27 = (a,b,num_of_primes_27)

print(answer_list_27)
            
print("Problem 27 answer: ", answer_list_27[0]*answer_list_27[1])



"""Problem 28"""



list_1_28 = [i**2 for i in range(3,1002,2)]

list_2_28 = [i - math.sqrt(i) + 1 for i in list_1_28]

list_3_28 = [i - 2*math.sqrt(i) + 2 for i in list_1_28]

list_4_28 = [i - 3*math.sqrt(i) + 3 for i in list_1_28]

answer_28 = 1 + sum(list_1_28) + sum(list_2_28) + sum(list_3_28) + sum(list_4_28)

print("Problem 28 answer: ", answer_28)



"""Problem 29"""



list_29 = []

for i in range(2,101):
    for j in range(2,101):
        list_29.append(i**j)

list_29.sort()

new_list_29 = []

for item in list_29:
    if item not in new_list_29:
        new_list_29.append(item)

answer_29 = len(new_list_29)

print("Problem 29 answer: ", answer_29)



"""Problem 30"""



list_30 = []

for i in range(10,1000000):
    word = str(i)
    num = 0
    for j in range(len(word)):
        num += int(word[j])**5
    if num == i:
        list_30.append(i)

answer_30 = 0

for i in list_30:
    answer_30 += i

print("Problem 30 answer: ", answer_30)



"""Problem 31"""



num_31 = 1

for i_2 in range(0,3):
    for i_3 in range(0,5):
        for i_4 in range(0,11):
            for i_5 in range(0,21):
                for i_6 in range(0,41):
                    for i_7 in range(0,101):
                        if 100*i_2 + 50*i_3 + 20*i_4 + 10*i_5 + 5*i_6 + 2*i_7 <= 200:
                            num_31 += 1

answer_31 = num_31

print("Problem 31 answer: ", answer_31)











"""Problem 32"""



list_32 = []

list_perms = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

length_32 = len(list_perms[0])

def concat(a):
    num = ""
    if len(a) == 0:
        return 0
    else:
        for i in range(len(a)):
            num = num + str(a[i])
        return int(num)

for perm in list_perms:
    for i in range(1,length_32-1):
        for j in range(i+1,length_32):
            multiplicand = concat(perm[:i])
            multiplier = concat(perm[i:j])
            product = concat(perm[j:])
            if multiplicand*multiplier == product:
                list_32.append(product)

answer_32 = sum(list(set(list_32)))

print("Problem 32: ", answer_32)



"""Problem 33"""



list_33 = []

def test_frac(a,b):
    a1, a2 = (a - (a % 10))/10, (a % 10)
    b1, b2 = (b - (b % 10))/10, (b % 10)
    if a2 != 0 and b2 != 0:
        if ((a/b == a1/b1 and a2 == b2) or (a/b == a1/b2 and a2 == b1) or (a/b == a2/b1 and a1 == b2) or (a/b == a2/b2 and a1 == b1)):
            return True
        else:
            return False

for denominator in range(11,100):
    for numerator in range(10,denominator):
        if test_frac(numerator,denominator) == True:
            list_33.append((numerator,denominator))

num, den = 1, 1

for item in list_33:
    num = num*item[0]
    den = den*item[1]

answer_33 = int((num/den)**(-1))

print("Problem 33 answer: ", answer_33) 



"""Problem 34"""



list_34 = []

for i in range(3,1000000):
    word_34 = str(i)
    sum_34 = 0
    for j in word_34:
        sum_34 += math.factorial(int(j))
    if sum_34 == i:
        list_34.append(i)

answer_34 = sum(list_34)

print("Problem 34 answer: ", answer_34)



"""Problem 35"""



def check_even(n):
    word = str(n)
    bool_check = True
    for letter in word:
        if int(letter) % 2 == 0:
            bool_check = False
    return bool_check

list_primes_35 = [i for i in range(1000000) if is_prime(i) and check_even(i)]

list_circ_primes_35 = []

for item in list_primes_35:
    item_word = str(item)
    bool_35 = True
    new_item = item_word
    for i in range(len(item_word)):
        new_item = new_item[-1] + new_item[:-1]
        if not int(new_item) in list_primes_35:
            bool_35 = False
            break
    if bool_35:
        list_circ_primes_35.append(item)

answer_35 = len(list_circ_primes_35)

print("Problem 35 answer: ", answer_35)



"""Problem 36"""



list_36 = []

def is_palindrome(num):
    bool_pal = True
    num_length = len(str(num))
    for i in range(math.floor(num_length/2)):
        if str(num)[i] != str(num)[-(i+1)]:
            bool_pal = False
            break
    return bool_pal

for i in range(1000000):
    i_binary = format(i,'b')
    if str(i_binary)[-1] == '1':
        if is_palindrome(i) and is_palindrome(i_binary):
            list_36.append(i)

answer_36 = sum(list_36)

print("Problem 36 answer: ", answer_36)



"""Problem 37"""



list_of_trunc_primes_37 = []

i = 11

while len(list_of_trunc_primes_37) < 11:
    if is_prime(i) == True:
        is_trunc_prime = True
        for j in range(1,len(str(i))):
            if (is_prime(int(str(i)[:-j])) == True) and (is_prime(int(str(i)[j:])) == True):
                is_trunc_prime = is_trunc_prime and True
            else:
                is_trunc_prime = is_trunc_prime and False
        if is_trunc_prime == True:
            list_of_trunc_primes_37.append(i)
    i += 2

answer_37 = sum(list_of_trunc_primes_37)

print("Problem 37 answer: ", answer_37)



"""Problem 38"""



def concat_pan_prod(num):
    num_list = [i for i in range(1,7)]
    string_temp = ""
    j = 0
    while len(string_temp) < 9:
        string_temp = string_temp + str(num*num_list[j])
        j += 1
    if len(string_temp) == 9 and set(string_temp) == set(["1","2","3","4","5","6","7","8","9"]):
        return int(string_temp)
    else:
        return 0

answer_38 = 0

for i in range(10,10000):
    if concat_pan_prod(i) > answer_38:
        num_38 = i
        answer_38 = concat_pan_prod(i)

print("Problem 38 answer: ", answer_38)



"""Problem 39"""



# CAN BE OPTIMISED

list_39 = []

for p in range(3,1001):
    num_of_solns = 0
    for a in range(1,p - 1):
        for b in range(1,p - 1 - a):
            if a**2 + b**2 == (p - (a + b))**2:
                num_of_solns += 1
    list_39.append(num_of_solns)

answer_39 = list_39.index(max(list_39)) + 3
                
print("Problem 39 answer: ", answer_39)



"""Problem 40"""



string_40 = ""

for i in range(1,200000):
    string_40 = string_40 + str(i)

answer_40 = 1

for j in range(0,7):
    answer_40 *= int(string_40[10**j - 1])

print("Problem 40 answer: ", answer_40)



"""Problem 41"""



n = 7 #Found the right value for n by trial and error

set_nums = set([i for i in range(1,n+1)])

def is_pandigital(num):
    if set_nums == set([int(i) for i in str(num)]) and len(str(num)) == n:
        return True
    else:
        return False

list_temp = [i for i in range((10**(n-1))+1,10**n,2) if is_pandigital(i) and is_prime(i)]

answer_41 = list_temp[-1]

print("Problem 41 answer: ", answer_41)



"""Problem 42"""



list_42 = []

with open("C:\\Users\\Nick\\Documents\\Python Scripts\\Project_Euler\\p042_codedtriangles.txt","r") as file:
    for line in file:
        list_temp_42 = line.split(",")
        for item in list_temp_42:
            list_42.append(item.strip('"'))

new_word = ""

for word in list_42:
    if len(word) >= len(new_word):
        new_word = word

"""Longest word is 14 characters long. So, the largest value a word can assume is 14*26 = 364. The largest triangle number less than 364 is t_26 = 351"""

triangle_nums_42 = [0.5*i*(i+1) for i in range(1,27)]

def word_value(word):
    sum_word = 0
    for letter in word:
        sum_word += ord(letter) - 64
    return sum_word

list_triangle_words_42 = [word for word in list_42 if word_value(word) in triangle_nums_42]

answer_42 = len(list_triangle_words_42)

print("Problem 42 answer: ", answer_42)



"""Problem 43"""



list_43 = [item for item in list(itertools.permutations([0,1,2,3,4,5,6,7,8,9])) if (item[3] % 2 == 0) and ((item[2] + item[3] + item[4]) % 3 == 0) and (item[5] % 5 == 0) and ((100*item[4] + 10*item[5] + item[6]) % 7 == 0) and ((item[5] - item[6] + item[7]) % 11 == 0) and ((100*item[6] + 10*item[7] + item[8]) % 13 == 0) and ((100*item[7] + 10*item[8] + item[9]) % 17 == 0)]

answer_43 = 0

for item in list_43:
    for i in range(0,10):
        answer_43 += (10**i)*item[9 - i]
    
print("Problem 43 answer: ", answer_43)



"""Problem 44"""



list_pentagonal_44 = [(n/2)*(3*n - 1) for n in range(1,10**8)]

set_pentagonal_44 = set(list_pentagonal_44)

for i in range(0,len(list_pentagonal_44)):
    for j in range(0,i):
        if (list_pentagonal_44[i] + list_pentagonal_44[j]) in set_pentagonal_44:
            if (list_pentagonal_44[i] - list_pentagonal_44[j]) in set_pentagonal_44:
                answer_44 = int(list_pentagonal_44[i] - list_pentagonal_44[j])
                break
    else:
        continue
    break

print("Problem 44 answer: ", answer_44)



"""Problem 45"""



triangle_nums_45 = [0.5*n*(n-1) for n in range(1,10**6)]

pentagonal_nums_45 = [0.5*n*(3*n-1) for n in range(1,10**6)]

hexagonal_nums_45 = [n*(2*n-1) for n in range(1,10**6)]

set_of_matches_45 = list(set(triangle_nums_45).intersection(pentagonal_nums_45).intersection(hexagonal_nums_45))

answer_45 = set_of_matches_45[-1]

print("Problem 45 answer: ", answer_45)



"""Problem 46"""



list_primes_46 = set([2] + list(filter(is_prime, list(range(1,10**4,2)))))

list_composite_46 = set(list(range(3,10**4,1))) - list_primes_46

for item in list_composite_46:
    bool_46 = False
    for i in range(1,math.ceil(math.sqrt(item/2))):
        if (item - 2*(i**2)) in list_primes_46:
            bool_46 = True
            break
    if not bool_46:
        answer_46 = item
        break

print("Problem 46 answer: ", answer_46)



"""Problem 47"""



list_47 = range(2,1000000,1)

def trial_division_unique(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
        n = int(n)
    while str(n)[-1] == '5':
        a.append(5)
        n /= 5
        n = int(n)
    f = 3
    while f**2 <= n:
        if n % f == 0:
            a.append(f)
            n /= f
            n = int(n)
        else:
            f += 2
    if n != 1:
        a.append(n)
    return set(a)

trial_division_set(12)

for i in range(len(list_47)):
    if len(trial_division_unique(list_47[i])) == 4:
        if len(trial_division_unique(list_47[i+1])) == 4:
            if len(trial_division_unique(list_47[i+2])) == 4:
                if len(trial_division_unique(list_47[i+3])) == 4:
                    answer_47 = list_47[i]
                    break

print("Problem 47 answer: ", answer_47)
     


"""Problem 48"""



sum_48 = 0

for i in range(1,1001):
    sum_48 += i**i

answer_48 = sum_48 % 10000000000

print("Problem 48 answer: ", answer_48)





"""Problem 49"""



set_ans_49 = set()

for item in range(1001,10000,2):
    list_temp_49 = sorted(list(filter(is_prime,list(map(lambda x: int("".join(x)),set(itertools.permutations(str(item))))))))
    for item in list_temp_49:
        if (item + 3330 in list_temp_49) and (item + 6660 in list_temp_49):
            set_ans_49.add((str(item), str(item+3330), str(item+6660)))

answer_49 = list(set_ans_49)[1][0] + list(set_ans_49)[1][1] + list(set_ans_49)[1][2]

print("Problem 49 answer: ", answer_49)



"""Problem 50"""



"QUITE SLOW: SHOULD IMPROVE SPEED"

list_of_primes_50 = [i for i in range(1,10**6) if is_prime(i)]

set_of_primes_50 = set(list_of_primes_50)

length_primes_50 = len(list_of_primes_50)

answer_50 = 0

length_50 = 0

for i in range(0,length_primes_50 - 1):
    num = sum(list_of_primes_50[i:])
    j = 1
    if num % 2 == 0:
        num = num - list_of_primes_50[-j]
        j += 1
        while num not in set_of_primes_50:
            num -= (list_of_primes_50[-j] + list_of_primes_50[-(j+1)])
            j += 2
    elif num % 2 == 1:
        while num not in set_of_primes_50:
            num -= (list_of_primes_50[-j] + list_of_primes_50[-(j+1)])
            j += 2
    j -= 1
    if (length_primes_50 - j - i) > length_50:
        answer_50 = num
        length_50 = (length_primes_50 - j - i)

print("Problem 50 answer: ", answer_50, length_50)



"""Problem 51"""



list_all_primes_51 = [str(num) for num in range(100000,1000000) if is_prime(num)]

def num_replace(num, old_digit, new_digit):
    return num.replace(old_digit, new_digit)

for number in list_all_primes_51:
    if '0' in number or '1' in number or '2' in number:
        for old_num in range(0,10):
            i = 0
            if str(old_num) in number:
                for new_num in range(0,10):
                    if num_replace(number, str(old_num), str(new_num)) in list_all_primes_51:
                        i += 1
                if i >= 8:
                    if num_replace(number, str(old_num), str(0)) in list_all_primes_51:
                        answer_51 = int(num_replace(number, str(old_num), str(0)))
                        break
                    elif num_replace(number, str(old_num), str(1)) in list_all_primes_51:
                        answer_51 = int(num_replace(number, str(old_num), str(1)))
                        break
                    else:
                        answer_51 = int(num_replace(number, str(old_num), str(2)))
                        break
        else:
            continue
        break

print("Problem 51 answer: ", answer_51) 



"""Problem 52"""



def num_list(n):
    return sorted(list(str(n)))

for num in range(1,1000000):
    if num_list(2*num) == num_list(3*num):
        if num_list(2*num) == num_list(4*num):
            if num_list(2*num) == num_list(5*num):
                if num_list(2*num) == num_list(6*num):
                    answer_52 = num
                    break

print("Problem 52 answer: ", answer_52)



"""Problem 53"""



def fact(n,k):
    ans = 1
    for i in range(1,min(k,n-k)+1):
        ans *= (n+1-i)/i
    return int(ans)

answer_53 = 0

for n in range(1,101):
    for r in range(0,n+1):
        if fact(n,r) > 10**6:
            answer_53 += 1

print("Problem 53 answer: ", answer_53)



"""Problem 54"""



with open("/Users/nick/Documents/Python Scripts/Project_Euler/p054_poker.txt","r") as file:
    list_54 = []
    for info in file:
        item1, item2 = info[:-1].split(' ')[:5], info[:-1].split(' ')[5:]
        list_54.append([item1, item2])

def get_card_num(item):
    first_item = item[0]
    if first_item in ['2','3','4','5','6','7','8','9']:
        return int(first_item)
    elif first_item == 'T':
        return 10
    elif first_item == 'J':
        return 11
    elif first_item == 'Q':
        return 12
    elif first_item == 'K':
        return 13
    elif first_item == 'A':
        return 14

def sort_list(item):
    list_temp = []
    for entry in item:
        list_temp.append([tuple(sorted(entry[0], key = get_card_num, reverse = False)), tuple(sorted(entry[1], key = get_card_num, reverse = False))])
    return list_temp

new_list = sort_list(list_54)

print(new_list[-1])

def hand_score(item):
    if (item[0][0] == 'T' and item[1][0] == 'J' and item[2][0] == 'Q' and item[3][0] == 'K' and item[4][0] == 'A') and (item[0][1] == item[1][1] and item[1][1] == item[2][1] and item[2][1] == item[3][1] and item[3][1] == item[4][1]):
        rank = 10
        rank_value = 14
        card_values = (14, 13, 12, 11, 10)
    elif (get_card_num(item[1][0]) - get_card_num(item[0][0]) == 1) and (get_card_num(item[2][0]) - get_card_num(item[1][0]) == 1) and (get_card_num(item[3][0]) - get_card_num(item[2][0]) == 1) and (get_card_num(item[4][0]) - get_card_num(item[3][0]) == 1) and (item[0][1] == item[1][1] and item[1][1] == item[2][1] and item[2][1] == item[3][1] and item[3][1] == item[4][1]):
        rank = 9
        rank_value = get_card_num(item[4][0])
        card_values = (get_card_num(item[4][0]), get_card_num(item[3][0]), get_card_num(item[2][0]), get_card_num(item[1][0]), get_card_num(item[0][0]))
    elif 
    rank
    rank_value
    card_values

(item[0][1] == item[1][1] and item[1][1] == item[2][1] and item[2][1] == item[3][1] and item[3][1] == item[4][1]):




"""Problem 55"""



answer_55 = 0

def rev_and_add(n):
    rev = 0
    num = n
    while num > 0:
        rev = int((10*rev) + (num % 10))
        num = int(num/10)
    return rev + n

def is_palindrome(n):
    list_n = str(n)
    bool_temp = True
    for i in range(0,math.floor(len(list_n)/2)):
        if list_n[i] != list_n[-(i+1)]:
            bool_temp = False
            break
    return bool_temp

def is_Lychrel(n):
    num = n
    bool_temp = True
    for _ in range(50):
        num = rev_and_add(num)
        if is_palindrome(num):
            bool_temp = False
            break
    return bool_temp

for i in range(1,10000):
    if is_Lychrel(i):
        answer_55 += 1

print("Problem 55 answer: ", answer_55)



"""Problem 56"""



answer_56 = 0

def digit_sum(n):
    return sum(list(map(lambda x: int(x), str(n))))

for a in range(1,100):
    for b in range(1,100):
        if digit_sum(a**b) > answer_56:
            answer_56 = digit_sum(a**b)

print("Problem 56 answer: ", answer_56)



"""Problem 57"""



def num_and_denom_of_cont_frac(alist):
    hlist = [0,1]
    klist = [1,0]
    for i in range(0,len(alist)):
        hnew = alist[i]*hlist[-1] + hlist[-2]
        hlist.append(hnew)
        knew = alist[i]*klist[-1] + klist[-2]
        klist.append(knew)
    return (hlist,klist)

def num_digits(n):
    return len(str(n))

sqrt2contfraclist = [1] + [2 for _ in range(1000)]

answer_57 = sum(list(map(lambda x, y: num_digits(x) > num_digits(y), num_and_denom_of_cont_frac(sqrt2contfraclist)[0], num_and_denom_of_cont_frac(sqrt2contfraclist)[1])))

print("Problem 57 answer: ", answer_57)



"""Problem 59"""



with open("/Users/nick/Documents/Python Scripts/Project_Euler/p059_cipher.txt","r") as file:
    for info in file:
        list_59 = list(map(lambda x: int(x), info.split(',')))

list_charascii_59 = list(range(97, 123))

keys_59 = [key for key in itertools.product(list_charascii_59, repeat = 3)]

def key_gen(n,tup):
    list_temp = []
    for i in range(0,n):
        if i % 3 == 0:
            list_temp.append(tup[0])
        elif i % 3 == 1:
            list_temp.append(tup[1])
        elif i % 3 == 2:
            list_temp.append(tup[2])
    return list_temp

for item in keys_59:
    password = key_gen(len(list_59),item)
    decrypted = ''.join(list(map(lambda x, y: chr(x^y), password, list_59)))
    if 'the' in decrypted and 'be' in decrypted and 'to' in decrypted and 'of' in decrypted and 'and' in decrypted and 'in' in decrypted and 'that' in decrypted:
        # print('Sample text: ', decrypted[:30], '|| ASCII key: ', item)
        key_59 = item
        break

decrypted_message_59 = list(map(lambda x, y: x^y, key_gen(len(list_59),key_59), list_59))

answer_59 = sum(decrypted_message_59)

print("Problem 59 answer: ", answer_59)



"""Problem 65"""



list_old_65 = [1 for i in range(99)]

list_65 = list_old_65

for i in range(0,math.floor(len(list_old_65)/3)):
    list_65[3*i + 1] = 2*(i+1)

list_65 = list_65[::-1]

num_65, denom_65 = list_65[0], 1

for i in range(1,len(list_65)):
    A = num_65
    B = denom_65
    denom_65 = A
    num_65 = list_65[i]*A + B

A = num_65
B = denom_65
denom_65 = A
num_65 = 2*A + B

answer_65 = 0

for letter in str(num_65):
    answer_65 += int(letter)

print("Problem 65 answer", answer_65)















"""Problem 67"""


list_67 = []

with open("C:\\Users\\Public\\Documents\\Python Scripts\\Project_Euler\\p067_triangle.txt","r") as file:
    for line in file:
        numbers_str = line.split(" ")
        numbers_int = [int(x) for x in numbers_str]
        list_67.append(numbers_int)

list_67.reverse()

for i in range(0,len(list_67)-1):
    for j in range(0,len(list_67[i+1])):
        list_67[i+1][j] += max(list_67[i][j],list_67[i][j+1])

answer_67 = list_67[-1][0]    

print("Problem 67 answer: ", answer_67)















"""Problem 92"""



set_1_92 = set()

set_89_92 = set()

def sum_square_digits_str(n):
    return sum([int(digit)**2 for digit in str(n)])

def sum_square_digits_arith(n):
    s = 0
    while n:
        s += (n % 10)**2
        n = ((n - (n % 10))/10)
    return int(s)

for num in range(1,5):
    set_temp = set()
    num_temp = num
    while (num_temp not in set_1_92) and (num_temp not in set_89_92):
        set_temp.add(num_temp)
        num_temp = sum_square_digits_str(num_temp)
    if (num_temp in set_89_92):
        set_89_92 = set_89_92.union(set_temp)
    else:
        set_1_92 = set_1_92.union(set_temp)



















"""Problem 97"""



answer_97 = (28433*(2**7830457) + 1) % 10**10

print("Problem 97 answer: ", answer_97)
















"""Problem 99"""



list_num_99 = []

list_99 = []

with open("C:\\Users\\Nick\\Documents\\Python Scripts\\Project_Euler\\p099_largeexp.txt","r") as file:
    for line in file:
        list_num_99.append(re.split(",|\n",line))

for item in list_num_99:
    list_99.append(int(item[1])*math.log(int(item[0])))
    
answer_99 = np.argmax(list_99) + 1

print("Problem 99 answer: ", answer_99)















"""Problem 137"""



list_137 = []

def root_is_rational(m,n):
    boolean = True
    numerator = sympy.ntheory.factorint(m)
    denominator = sympy.ntheory.factorint(n)
    for key in denominator:
        if key in numerator:
            numerator[key] -= denominator[key]
            denominator[key] = 0
    for key in numerator:
        if (numerator[key] % 2) != 0:
            boolean = False
            break
    for key in denominator:
        if (denominator[key] % 2) != 0:
            boolean = False
            break
    return boolean

i = 0
y = 1

while i < 8:
    n = y**2
    m = 5*n + 2*y + 1
    if root_is_rational(m,n):
        list_137.append(y)
        i += 1
    y += 1
    
answer_137 = 0

print(list_137)

print("Problem 137 answer: ", answer_137)







