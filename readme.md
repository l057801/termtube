# Termtube

A small tool to search youtube through the terminal and play videos using mpv, built with python on top of the youtube-search-python project

## To get up and running:
1. clone repo
2. install requirements
3. make sure you have mpv installed
4. make sure you have the following alias set: 
> alias termtube='python3 ~/insert_path_to_file/main.py'

5. run termtub in terminal and enjoy

---
## Future work:
- currently the youtube videos are downloaded in a temp folder and cleared only when quitting, add functionality; which could be an issue for long sessions taking up memory. Find solution to clear video after mpv is closed.
