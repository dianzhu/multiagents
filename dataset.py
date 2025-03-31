import csv

filename1 = open('datasets/dataset1.csv', 'r')
filename2 = open('datasets/dataset2.csv','r')
filename3 = open('datasets/dataset3.csv','r')
filename4 = open('datasets/dataset4.csv','r')
filename5 = open('datasets/dataset5.csv','r')
filename6 = open('datasets/dataset6.csv','r')
filename7 = open('datasets/dataset7.csv','r')

file1 = csv.DictReader(filename1)
file2 = csv.DictReader(filename2)
file3 = csv.DictReader(filename3)
file4 = csv.DictReader(filename4)
file5 = csv.DictReader(filename5)
file6 = csv.DictReader(filename6)
file7 = csv.DictReader(filename7)

