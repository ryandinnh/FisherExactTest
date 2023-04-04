# FisherExactTest
Python code to perform Fisher exact test for contingency tables in data analysis and machine learning. Includes a function to compute probabilities and a script that applies test to cardiac dataset to analyze gender differences in hypertension. Useful for statistical analysis of categorical data with small sample sizes.

Cardiac.csv contains measurements related to cardiovascular health. The dataset is used to test the hypothesis that women are more likely to have hypertension (high blood pressure) than men. The dataset includes two variables of interest: hxofHT (hypertension status, with 0 indicating hypertension) and gender (0 for male and 1 for female). 

contigencytable.py script generates a 2x2 contingency table for the cardiac.csv dataset. The dataset includes information on hypertension status (hxofHT) and gender, and the script uses the pandas library to compute a table that counts the number of men and women with and without hypertension. The resulting table is useful for testing hypotheses related to gender differences in hypertension and for analyzing the relationship between hypertension and other variables in the dataset. The script can be modified to compute contingency tables for other datasets with similar categorical variables.

