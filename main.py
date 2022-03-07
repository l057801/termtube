from youtubesearchpython import VideosSearch
import os
from functions import bcolors, search, analyze_response, create_temp, delete_temp, start_video, stream_choice_video, close_all

if __name__ == "__main__":

    create_temp()
    while True:
        os.system('clear')
        print(f'{bcolors.WARNING}enter (q) at any point to quit!{bcolors.ENDC}')
        searchTerm = input('Search: ')

        if searchTerm.lower() == 'q':
            break
        else:
            try:
                searchNo = int(input('Number of results: '))
                response = search(searchTerm,searchNo)
                analysis = analyze_response(response)
            
                try:
                    choiceNo = input('Choose a number: ')
                    vid = stream_choice_video(analysis,choiceNo)
                    start_video(vid)

                except:
                    if choiceNo.lower() == 'q':
                        break
                    else:
                        print(f'{bcolors.WARNING}Please enter a number{bcolors.ENDC}')

            except:
                if searchTerm.lower() == 'q':
                    break
                else:
                    print(f'{bcolors.WARNING}Please enter a number{bcolors.ENDC}')

    close_all()
    delete_temp()
    os.system('clear')
