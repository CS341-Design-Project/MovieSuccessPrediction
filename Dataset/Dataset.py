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

print("Average")
print(yearAvg)

print("Relative")
print(yearWeight)

directors = pd.read_csv('Directors.csv')

director = list(set(directors['id']))

directorWeight = {}

for id in director :
  c_id = directors[directors['id'] == id]['c_id'].to_list()
  w = map(lambda x : cinema[cinema['c_id'] == x]['rating'].item() * yearWeight[cinema[cinema['c_id'] == x]['year'].item()],c_id)
  directorWeight[id] = round(mean(w),2)

print(directorWeight)

producers = pd.read_csv('Producers.csv')

producer = list(set(producers['id']))

producerWeight = {}

for id in producer :
  c_id = producers[producers['id'] == id]['c_id'].to_list()
  w = map(lambda x : cinema[cinema['c_id'] == x]['rating'].item() * yearWeight[cinema[cinema['c_id'] == x]['year'].item()],c_id)
  producerWeight[id] = round(mean(w),2)

print(producerWeight)

narratives = pd.read_csv('Narrative.csv')

narrative = list(set(narratives['id']))

narrativeWeight = {}

for id in narrative :
  c_id = narratives[narratives['id'] == id]['c_id'].to_list()
  w = map(lambda x : cinema[cinema['c_id'] == x]['rating'].item() * yearWeight[cinema[cinema['c_id'] == x]['year'].item()],c_id)
  narrativeWeight[id] = round(mean(w),2)

print(narrativeWeight)

heroes = pd.read_csv('Heroes.csv')

hero = list(set(heroes['id']))

heroWeight = {}

for id in hero :
  c_id = heroes[heroes['id'] == id]['c_id'].to_list()
  w = map(lambda x : cinema[cinema['c_id'] == x]['rating'].item() * yearWeight[cinema[cinema['c_id'] == x]['year'].item()],c_id)
  heroWeight[id] = round(mean(w),2)

print(heroWeight)

actors = pd.read_csv('Actors.csv')

actor = list(set(actors['id']))

actorWeight = {}

for id in actor :
  c_id = actors[actors['id'] == id]['c_id'].to_list()
  w = map(lambda x : cinema[cinema['c_id'] == x]['rating'].item() * yearWeight[cinema[cinema['c_id'] == x]['year'].item()],c_id)
  actorWeight[id] = round(mean(w),2)

print(actorWeight)

songs = pd.read_csv('Song.csv')

song = list(set(songs['id']))

songWeight = {}

for id in song :
  c_id = songs[songs['id'] == id]['c_id'].to_list()
  w = map(lambda x : cinema[cinema['c_id'] == x]['rating'].item() * yearWeight[cinema[cinema['c_id'] == x]['year'].item()],c_id)
  songWeight[id] = round(mean(w),2)

print(songWeight)

list = [[k, v] for k, v in songWeight.items()] 
print(list)
df = pd.DataFrame(list,columns=['code','rating']) # Creating DataFrame for Data  Set

df.fillna(0,inplace=True)
df.to_csv("Song_r.csv")

"""# Data Set Design

"""

ds = pd.DataFrame(columns=['director','producer','narrative','hero','actor','song','rating']) # Creating DataFrame for Data  Set

cinemaId = list(set(cinema['c_id']))

f={}

for i in cinemaId:

  directorId = directors[directors['c_id'] == i]['id'].to_list()
  if len(directorId):
    f['director'] = round(mean(map(lambda x: directorWeight[x],directorId)),2)  

  producerId = producers[producers['c_id'] == i]['id'].to_list()
  if len(producerId) :
    f['producer'] = round(mean(map(lambda x: producerWeight[x],producerId)),2)  
  
  narrativeId = narratives[narratives['c_id'] == i]['id'].to_list()
  if len(narrativeId):
    f['narrative'] = round(mean(map(lambda x: narrativeWeight[x],narrativeId)),2)
  
  heroId = heroes[heroes['c_id'] == i]['id'].to_list()
  if len(heroId):
    f['hero'] = round(mean(map(lambda x: heroWeight[x],heroId)),2)

  actorId = actors[actors['c_id'] == i]['id'].to_list()
  if len(actorId):
    f['actor'] = round(mean(map(lambda x: actorWeight[x],actorId)),2)

  songId = songs[songs['c_id'] == i]['id'].to_list()
  if len(songId):
    f['song'] = round(mean(map(lambda x: songWeight[x],songId)),2)

  f['rating'] = cinema[cinema['c_id'] == i]['rating'].item()
  
  ds = ds.append(f,ignore_index=True)

ds.fillna(0,inplace=True)
ds.to_csv("Dataset.csv")

ds.tail(50)
