import os
import pymongo
import json
import io
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON

HOST_IP = "54.89.252.113"
HOST_PORT = "27017"

def main():

    uri = "mongodb://"+HOST_IP+":"+HOST_PORT

    client = MongoClient(uri)
    print("Connected to",HOST_IP+":"+HOST_PORT+" successfully!")
    db = client["testdb"]
    businessCollection = db["businessCollection"]
    reviewCollection = db["reviewCollection"]

    # y = client.list_database_names
    # print(y)

    while True:
        print("Welcome to the YELP Business Analysis Tool")
        print("Choose an option from the following: ")
        print("1. Find top 10 restaurants in location X")
        print("2. List of users from city x who provide the most number of compliments")
        print("3. Find restaurants that are open after Y Time and have parking and valet service")
        print("4. Find zip codes where most number of restaurants have been closed")
        print("5. Find restaurants in a certain zip code that provides delivery services")
        print("6. Find businesses with review counts greater than X and display hours")
        print("7. Find restaurants where dogs are allowed and wifi is free")
        print("8. Find average star rating for every state. Display the state and the star ratings")
        print("9. Find restaurants in a certain zip code where you don’t have to make reservations and restaurant attire is casual")
        print("10. Create users with given parameters")
        print("11. Create business with given parameters")
        print("12. Update user reviews")
        print("13. Update business information")
        print("14. Delete user who hasn’t shown activity in X Time")
        print("15. Find sum of users who joined yelp since date X")
        print("16. EXIT")
        user_val = input()

        if user_val == '1':
            print("Selected 1")
            print("Use Case: Find top 10 restaurants in location X")
            loc = input("Enter postal code (Ex. 93101): ")
            myVals = []
            print("Started processing")
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

            proceed = input("Press any key to continue")
            continue
        elif user_val == '2':
            print("Selected 2")
        elif user_val == '3':
            print("Selected 2")
        elif user_val == '4':
            print("Selected 2")
        elif user_val == '5':
            print("Selected 2")
        elif user_val == '6':
            print("Selected 2")
        elif user_val == '7':
            print("Selected 2")
        elif user_val == '8':
            print("Selected 2")
        elif user_val == '9':
            print("Selected 2")
        elif user_val == '10':
            print("Selected 2")
        elif user_val == '11':
            print("Selected 2")
        elif user_val == '12':
            print("Selected 2")
        elif user_val == '13':
            print("Selected 2")
        elif user_val == '14':
            print("Selected 2")
        elif user_val == '15':
            print("Selected 2")
        else:
            print("Terminating")
            break

        break

if __name__ == "__main__":
    main()

