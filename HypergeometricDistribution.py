from scipy.special import comb 

#function to find hypergeometric probability
def hypergeometricProb(N, n, M, k):
    prob = (comb(M, k) * comb(N - M, n - k)) / comb(N, n)
    return prob

#Values from contigencytable.py
N1 = 558 #total people in data set 
n1 = 76 + 144 # males
M1 = 393 #ppl with hypertension
k1 = 144 #males with hypertension

menProb = hypergeometricProb(N1, n1, M1, k1)
print("Probability of getting this table from the perspective of men: {:.6f}".format(menProb))
