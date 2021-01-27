from statistics import mean
import pandas as pd

cinema = pd.read_csv('Cinema.csv')

yearAvg = {}

for year in range(2000,2021):
  ratings = cinema[cinema['year'] == year]['rating'].to_list()
  avg = mean(ratings)
  yearAvg[year] = avg

maxYear = yearAvg[max(yearAvg,key=yearAvg.get)]
weight = map(lambda year,avg: {year : round(avg/maxYear,2)},yearAvg.keys(),yearAvg.values())

yearWeight = {}

for w in weight :
  yearWeight.update(w) 