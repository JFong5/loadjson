import pymongo
from pymongo import MongoClient
import json


def inputJsonName():
    '''
    Prompts the user for a Json File name
    Return: Json File Input (Str)
    '''
    jsonName = input("Input the json file name you would like to insert. \n")
    return jsonName


def inputPortNum():
    '''
    Prompts the user for a Port Num
    Return: Port Num Input (Int)
    '''
    portNum = int(input("Please input a port number. \n"))
    return portNum


def main():
    # Prompt user for portNum and insert it to client name
    portNum = inputPortNum()
    client = MongoClient('mongodb://localhost:' + str(portNum))
    dbs = client.list_database_names()

    # Checks if the database exists and drops
    if '291db' in dbs:
        # if exists removes database
        print("Database already exists.")
        db = client["291db"]
        db.data.drop()
        print("Updating data base....")

    # Checks
    db = client["291db"]
    collection = db["dplb"]

    fileName = inputJsonName()
    with open(fileName) as file:
        data = json.loads(file)

    collection.delete_many({})
    collection.insert_many(data)

    print("Collection Created!")


main()