import pymongo
from pymongo import MongoClient

def inputPortNum():
    '''
    Prompts the user for a Port Num
    Return: Port Num Input (Int)
    '''
    portNum = int(input("Please input a port number. \n"))
    return portNum
    

def mainMenu(db):
    '''
    Prompts user for an option from 1 to 5
    Execute certain functions for each choice 
    '''

    #Prompt user for option number
    choice = int(input("Please select the following task you would like to perform: \n1.Search for article \n2.Search for authors \n3.List the venues \n4.Add an article \n5.Exit \n"))
    if choice == 1:
        #Executes searchForArticle(db) function
        searchForArticle(db)
    elif choice == 2:
        #Executes searchForAuthors(db) function
        searchForAuthors(db)
    elif choice == 3:
        #Executes listVenues(db) function
        listVenues(db)
    elif choice == 4:
        #Executes addArticle(db) function
        addArticle(db)
    elif choice == 5:
        #Executes exit function and closes program
        exit()

def searchForArticle(db):
    """
    Prompts user for keyword
    Displays all Articles matching the keyword
    """
    #Connects to dplb collection in the database
    collection = db["dplb"]

    #Creates a list to store matchingArticles to keywords
    matchingArticles = []

    #Prompts user for matching keyword or keywords
    userKeywords = input("Please insert a keyword or keywords of the article you would like to search\n")

    query = {"title": userKeywords}
    mydoc = collection.find(query)

    for x in mydoc:
        print(x)

def searchForAuthors(db):
    pass

def listVenues(db):
    pass

def addArticle(db):
    pass

def exit():
    print("Now exiting, thank you for using our services!")

def main():
    #Prompt user for portNum and insert it into client name
    portNum = inputPortNum()
    client = MongoClient('mongodb://localhost:' + str(portNum))
    db = client["291db"]

    #Calls Main menu function
    mainMenu(db)

if __name__ == "__main__":
    main()
    
