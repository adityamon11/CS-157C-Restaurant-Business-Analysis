from audioop import add
import os
import pymongo
import json
import io
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON

HOST_IP = "18.207.247.141"
HOST_PORT = "27017"

def main():

    uri = "mongodb://"+HOST_IP+":"+HOST_PORT

    client = MongoClient(uri)
    print("Connected to",HOST_IP+":"+HOST_PORT+" successfully!")
    db = client["testdb"]
    businessCollection = db["businessCollection"]
    reviewCollection = db["reviewCollection"]
    userCollection = db["userCollection"]

    # y = client.list_database_names
    # print(y)

    while True:
        print("Welcome to the YELP Business Analysis Tool")
        print("Choose an option from the following: ")
        print("1. Find top 10 restaurants in location X")
        print("2. List of users from city X who provide the most number of compliments")
        print("3. Find restaurants that are open after Y Time and have parking and valet service")
        print("4. Find number of restaurants that are open/closed in a zipcode")
        print("5. Find restaurants in a certain zip code that provides delivery services")
        print("6. Find businesses with review counts greater than X and display hours")
        print("7. Find restaurants in location X where dogs are allowed and wifi is free")
        print("8. Find average star rating for every state. Display the state and the star ratings")
        print("9. Find restaurants in a certain zip code where you don’t have to make reservations and restaurant attire is casual")
        print("10. Create users with given parameters")
        print("11. Create business with given parameters")
        print("12. Update user reviews")
        print("13. Update business information")
        print("14. Delete user who hasn’t shown activity in X Time")
        print("15. Find sum of users who joined yelp since date X")
        print("16. Find top 10 businesses in location X with highest number of check in times")
        print("17. EXIT")
        user_val = input()

        if user_val == '1':
            print("Selected 1")
            print("Use Case: Find top 10 restaurants in location X")
            loc = input("Enter postal code (Ex. 93101): ")
            myVals = []
            print("Processing...")

            results = db.reviewCollection.aggregate([
            { 
                "$match": { "stars": {"$gte":4} } },
                {"$sort": {"stars": -1}},
                { "$limit": 500 },
                {"$project": {"business_id": "$business_id" }}

            ])
            
            for result in results:
                myVals.append(result.get('business_id'))

            endResult = db.businessCollection.find({"postal_code":loc,"business_id":{"$in":myVals}},{"business_id":1,"name":1}).limit(10)
            if len(list(endResult.clone())) > 0:
                for result in endResult:
                    print(result)
            else:
                print("No records found!")

            proceed = input("Press any key to continue ")
            continue
        elif user_val == '2':
            print("Selected 2")
        elif user_val == '3':
            print("Selected 3")
        elif user_val == '4':
            print("Selected 4")
            print("Use Case: Find number of restaurants that are open/closed in a zipcode")
            loc = input("Enter postal code (Ex. 93101): ")
            res = ""
            op = input("Press 0 for Closed , 1 for Open ")
            if(op == 0):
                res = "Closed"
            else:
                res = "Open"
            results = db.businessCollection.aggregate([
                { "$match": { "$and": [ { "postal_code": { "$eq": loc } }, { "is_open": { "$eq": int(op) } } ] } },
                { "$group": { "_id": "null", "count": { "$sum": 1 } } }
                ])
                
            for result in results:
                print(result.get('count') , "Restaurants are",res,"in postal code",loc)
            proceed = input("Press any key to continue ")

            continue

        elif user_val == '5':
            print("Selected 5")
        elif user_val == '6':
            print("Selected 6")
        elif user_val == '7':
            print("Selected 7")
            print("Use Case: Find restaurants in location X where dogs are allowed and wifi is free")
            loc = input("Enter postal code (Ex. 93101): ")
            results = db.businessCollection.find({"postal_code":loc,"attributes.WiFi":"u'free'","attributes.DogsAllowed":"True"},{"business_id":1,"name":1}).limit(10)
            if len(list(results.clone())) > 0:
                for result in results:
                    print(result)
            else:
                print("No records found!")
            
            proceed = input("Press any key to continue ")

            continue

        elif user_val == '8':
            print("Selected 8")
        elif user_val == '9':
            print("Selected 9")
        elif user_val == '10':
            print("Selected 10")
            print("Use Case: Create user with given parameters")
            name = input("Enter name of the user ")
            reviews = int(input("Enter the number of reviews written by this user "))
            yelp_since = input("Enter the date since the user joined Yelp (format YYYY-MM-DD ")
            post_record = {"name": name,"review_count":reviews,"yelping_since":yelp_since}
            db.userCollection.insert_one(post_record)
            print("Record created")
            results = db.userCollection.find({"name":name,"review_count":reviews,"yelping_since":yelp_since})
            if len(list(results.clone())) > 0:
                for result in results:
                    print(result)
        
            else:
                print("No records found!")

            proceed = input("Press any key to continue ")

            continue
        elif user_val == '11':
            print("Selected 11")
        elif user_val == '12':
            print("Selected 12")
        elif user_val == '13':
            print("Selected 13")
            print("Use Case: Update business information ")
            businessId = input("Enter the business id ")
            
            print("Displaying Record")

            results = db.businessCollection.find({"business_id":businessId},{"business_id":1,"name":1,"address":1,"city":1})

            if len(list(results.clone())) > 0:
                for result in results:
                    print(result)
        
            else:
                print("No records found!")

            name = input("Enter new name ")
            address = input("Enter new address ")
            city = input("Enter new city ")

            db.businessCollection.update_one({"business_id":businessId},{"$set":{"name":name,"address":address,"city":city}})
            results = db.businessCollection.find({"business_id":businessId},{"business_id":1,"name":1,"address":1,"city":1})
            print("Record Updated")
            if len(list(results.clone())) > 0:
                for result in results:
                    print(result)
        
            else:
                print("No records found!")

            proceed = input("Press any key to continue ")
            continue


        elif user_val == '14':
            print("Selected 14")
        elif user_val == '15':
            print("Selected 15")
        elif user_val == '16':
            print("Selected 16")
            print("Use Case: Find top 10 businesses in location X with highest number of check in times")
            loc = input("Enter postal code (Ex. 93101): ")
            agg = [
            {"$match": {"postal_code": { "$eq": loc }}},
            {"$project": {"_id":"$business_id","name":"$name","checkin_count":{ "$size": { "$ifNull": [ "$check-in", [] ] }}}}, 
            {"$sort":{"checkin_count":-1}},
            {"$limit":10}
            ]
            results = db.businessCollection.aggregate(agg,allowDiskUse=True)
            for result in results:
                print(result)

            proceed = input("Press any key to continue ")
            continue

        else:
            print("Terminating")
            break

        break

if __name__ == "__main__":
    main()

