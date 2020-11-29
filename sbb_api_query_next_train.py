
import json
import requests
import random as rn


def get_train_placement():
    return rn.randint(0,420)/100
def get_train_doors_position_from_category(type):
    return 12
lausanne_id="8592050"
base_url = "http://transport.opendata.ch/v1/stationboard?station=lausanne&transportation[]=train"
a = requests.get(base_url)
myjson = a.text
parsed = json.loads(myjson)
train_name = parsed['stationboard'][0]['name']
train_type = parsed['stationboard'][0]['category']
train_to = parsed['stationboard'][0]['to']
train_platforme = parsed['stationboard'][0]['stop']['platform']

train_position = get_train_placement()
print("Passanger is taking his train in lausanne, going to {}. The {} of model {}. \nTrain will stop on the platform {} and his position in relation to the platform is {}".format(train_to,train_name, train_type,train_platforme, get_train_placement()))
print("Having a {} class train, doors are at the begining and end of the ram".format(train_type))
