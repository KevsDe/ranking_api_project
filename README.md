![img](https://github.com/KevsDe/ranking_api_project/blob/master/output/github.png)

# Objective of this project: build our own api.

Information sources:
* [Github](https://github.com/ironhack-datalabs/datamad0820)

For this project I used:
*Docker
*Heroku
*MongoDB
*Mongodb Atlas
Libraries:
* Requests
* Pymongo
* Regex
* Dotenv
* Bs4
* Flask
* Random
* bson.objectid
* datetime
*Itertools
*Os
*Math
* Argparse
* In adittion to functions that I created during the whole process.

## Summary
For this project, my objective was to write my own API in flask retrieving information extracted from Github API and performing web scraping that is previously stored on MongoDB.
## Valid endpoints:
* /student/create/<studentname>  - Purpose: Create a student and save into DB - Params: studentname the student name - Returns: student_id
* /student/all - Purpose: List all students in database - Returns: An array of student objects
* /lab/create - Purpose: Create a lab to be analyzed - Params: The lab name to be analyzed. Example: lab tableau data visualization - Returns: lab_id
*/lab/<lab_id>/search - Purpose: Display information about the lab status - Params: lab_id - Returns: See Lab analysis sectionº
*/lab/memeranking - Purpose: Ranking of the most used memes for datamad0820 divided by labs
*/lab/<lab_id>/meme - Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab
*/lab/all Purpose: List all lab_id in database - Returns: An array of labs_id objects

ºLab analysis response:
*Number of open pull requests
*Number of closed pull request
*The ratio of completed corrections
*Students who have not delivered the pull request
*The list of unique memes used for that lab
*Instructor grade time in hours: (pr_close_time-last_commit_time)
## Files
* ranking_api.py: Extract all the information create a database named "datamad08020" and a collection named "pull" to MongoDB.
* database_shaper.py: Create to collections, add the students and labs information to mongodb and add a new row to the "pull" collection with the "lab id".
* drop_mongoDB: Drop the database "datamad0820" form mongoDB.

## Thanks 
