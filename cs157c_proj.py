import os
import pymongo
import json
import io
from pymongo import MongoClient
from bson.objectid import ObjectId

HOST_IP = "3.86.34.214"
HOST_PORT = "27017"


def insertRecord(collection):
    post1 = {"id":"1","city": "My City"}
    collection.insert_one(post1)
    print("Record inserted")

def readRecord(collection,key,val):
    results = collection.find({key:val})
    print("Searching for key:",key," and value:",val)
    if len(list(results.clone())) > 0:
        for result in results:
            print(result)
        
    else:
        print("No records found!")

    print("Completed reading")

def deleteRecord(collection):
    results = collection.delete_one({"id":"1"})
    print("Completed delete")

def updateRecord(collection):
    results = collection.update_one({"id":"1"}, {"$set":{"city":"Updated City"}})


def main():

    uri = "mongodb://"+HOST_IP+":"+HOST_PORT

    client = MongoClient(uri)
    print("Connected to",HOST_IP+":"+HOST_PORT+" successfully!")
    db = client["testdb"]
    collection = db["zipsCollection"]

    y = client.list_database_names
    print(y)

    readRecord(collection,"_id","01030")

    insertRecord(collection)
    readRecord(collection,"id","1",)

    updateRecord(collection)
    readRecord(collection,"id","1")

    deleteRecord(collection)
    readRecord(collection,"id","1")

    client.close()
    print("Operation Completed")



if __name__ == "__main__":
    main()






