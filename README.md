# CS-157C-Restaurant-Business-Analysis

We aim to create an application that provides an analysis of different types of restaurants and businesses across 8 metropolitan areas spread out in the USA and Canada. We will be providing different types of use cases to the users so that relevant information can be easily shown to users.

NoSQL deployment is the perfect choice for such an application since the data is spread out across multiple documents and is of varying types. There is no rigid structure to the data hence, using a relational database would not be a good choice. Moreover, the current data is of restaurant businesses in USA and Canada, and as the system scales after adding data from other countries, it would be better managed using a non-relational database. Further, this data could be spread across multiple replica sets and shards as well. For all of this, using MongoDB would be a great choice as it fits all of our use cases.

Use Cases:
        1. Find top 10 restaurants in location X
        2. List of users who provide the most number of compliments
        3. Find restaurants that are open after Y Time and have parking and valet service
        4. Find number of restaurants that are open/closed in a zipcode
        5. Find restaurants in a certain zip code that provides delivery services
        6. Find businesses with review counts greater than X and display hours
        7. Find restaurants in location X where dogs are allowed and wifi is free
        8. Find average star rating for every state. Display the state and the star ratings
        9. Find restaurants in a certain zip code where you don’t have to make reservations
        10. Create users with given parameters
        11. Create business with given parameters
        12. Update user reviews
        13. Update business information
        14. Delete a user based on the user id
        15. Find sum of users who joined yelp since date X
        16. Find top 10 businesses in location X with highest number of check in times
