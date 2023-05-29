from data_retrieval import get_data
url = ""
while(not len(url)):
    url = input("Input the url reddit : ")
print("Looking for the url ... \n")
get_data(url)