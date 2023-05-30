import os
import json
#curent directory

def get_task_name():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    html_files = []
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is an HTML file
        if file_name.endswith(".html"):
            # Add the file name to the list of HTML files
            #remove the html extension 
            file_name = file_name[:-5]
            html_files.append(file_name)
    # Create a dictionary with the HTML files
    html_dict = {"html_files": html_files}
    # Save the dictionary to a JSON file
    with open("task_names.json", "w") as f:
        json.dump(html_dict, f,indent=2)

def get_task_name_by_folder():
    # Create an empty list to store the folder names
    folder_names = []
    folder_path = os.path.dirname(os.path.realpath(__name__))
    # Loop through all files and directories in the folder
    for item in os.listdir(folder_path):
        # Check if the item is a directory
        if os.path.isdir(os.path.join(folder_path, item)):
            # Add the folder name to the list
            folder_names.append(item)
    # Create a dictionary with the folder names
    folder_dict = {"folders": folder_names}
    # Save the dictionary to a JSON file
    with open("task_names.json", "w") as f:
        json.dump(folder_dict, f, indent=2)

def get_JSON_intersect(file1,file2):

    # Load the first JSON file into a dictionary
    with open(file1, "r") as f:
        data1 = json.load(f)

    # Load the second JSON file into a dictionary
    with open(file2, "r") as f:
        data2 = json.load(f)

    # Find the intersection of the values in the dictionaries
    intersection = set(data1["html_files"]) & set(data2["html_files"])

    # Print the intersection of the values
    print(f"The intersection of the values is: {intersection}")

    #save intersection to json file
    html_dict = {"html_files": list(intersection)}

    # Save the dictionary to a JSON file
    with open("task_intersect.json", "w") as f:
        json.dump(html_dict, f,indent=2)

def get_JSON_diff(file1,file2):
    
    # Load the first JSON file into a dictionary
    with open(file1, "r") as f:
        data1 = json.load(f)
    # Load the second JSON file into a dictionary
    with open(file2, "r") as f:
        data2 = json.load(f)
    # Find the intersection of the values in the dictionaries
    diff = set(data1["task_name"]) - set(data2["task_name"])
    #save intersection to json file
    html_dict = {"task_name": list(diff)}
    # Save the dictionary to a JSON file
    with open("task_diff.json", "w") as f:
        json.dump(html_dict, f,indent=2)
