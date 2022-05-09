# CS-157C-Restaurant-Business-Analysis

We aim to create an application that provides an analysis of different types of restaurants and businesses across 8 metropolitan areas spread out in the USA and Canada. We will be providing different types of use cases to the users so that relevant information can be easily shown to users.

NoSQL deployment is the perfect choice for such an application since the data is spread out across multiple documents and is of varying types. There is no rigid structure to the data hence, using a relational database would not be a good choice. Moreover, the current data is of restaurant businesses in USA and Canada, and as the system scales after adding data from other countries, it would be better managed using a non-relational database. Further, this data could be spread across multiple replica sets and shards as well. For all of this, using MongoDB would be a great choice as it fits all of our use cases.
