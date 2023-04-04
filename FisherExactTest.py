from scipy.stats import fisher_exact 

#insert values of contigency table
cont_table = [[76, 144], [89, 249]]

#calculation of P-value from fisher exact test
odds_ratio, p_value = fisher_exact(cont_table, alternative='greater')

print("p-value: {:.6f}".format(p_value))
