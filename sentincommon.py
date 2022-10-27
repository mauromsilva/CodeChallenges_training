#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'
set1 = set(sentence1.split())
set2 = set(sentence2.split())
    
print(sorted(list(set1^set2)), sorted(list(set1&set2)) ) # ^ A.symmetric_difference(B), & A.intersection(B)

#***************  OR THIS WAY BELOW ***************
def solution(vsent1, vsent2):
    v1 = vsent1.split()
    v2 = vsent2.split()
    vunique = []
    viqual =[]

    for c in v1:
        if c not in v2:
            vunique.append(c)
        else:    
            viqual.append(c)
    print('************ unique ************')
    print(vunique)
    print('************ iqual ***************')
    print(viqual)        

    

print(solution(sentence1, sentence2))
