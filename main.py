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
    #Prompt user for portNum and insert it into client name
    portNum = inputPortNum()
    client = MongoClient('mongodb://localhost:' + str(portNum))

    #Checks if the database name exists
    dbs = client.list_database_names()
    if '291db' in dbs:
        # if exists removes the database
        print("Database already exists.")
        db = client["291db"]
        db.data.drop()
        print("Updating data base....")

    #Connects database 291db to client and create collection
    db = client["291db"]
    collection = db["dplb"]

    #Prompt user for json fileName and process items one row at a time
    #inserts items into collection_list
    collection_list = []
    fileName = inputJsonName()
    with open(fileName) as file:
        for item in file:
            dic = json.loads(item)
            collection_list.append(dic)
    
    #insert collection list into database
    collection.delete_many({})
    collection.insert_many(collection_list)
    print("Collection Created!")

main()

