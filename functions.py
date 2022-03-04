from youtubesearchpython import VideosSearch
import os

class bcolors:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    COUNT = '\u001b[33m'
    DURATION = '\u001b[35m'


def search(query,limit):
    limit = int(limit)
    query = str(query)
    response = VideosSearch(query, limit)
    return response.result()

# function for analyzing results and printing out
def analyze_response(resp):
    finalAnalyzed = {}
    resp = resp['result']
    for ind, res in enumerate(resp):
        finalAnalyzed[str(ind+1)] = {
                'duration' : res['duration'],
                'link' : res['link'],
                'viewCount' : res['viewCount']['short'],
                'title' : res['title'],
                'channel' : res['channel']['name'],
                'published' : res['publishedTime']
                }
    
    for k,v in finalAnalyzed.items():
        print(f"{k}) {v['title']}\t{bcolors.DURATION}{v['duration']}\t{bcolors.COUNT}{v['viewCount']} {bcolors.ENDC}")

    return finalAnalyzed

# function for choosing
def stream_choice_video(choices, number):
    chosen = choices[str(number)]
    url = chosen['link']
    # clean name
    name = chosen['title'].replace("'","")
    location = f"~/Videos/temp/temp_{name}.mp4"
    os.system(f"yt-dlp --quiet -f 'best[ext=mp4]' {url} -o '{location}'")
    return location

def create_temp():
    # check if temp directory exists:
    os.chdir(os.path.expanduser('~/Videos'))
    if 'temp' in os.listdir():
        pass
    else:
        os.mkdir('temp')

# function for os calls
def start_video(name):
    symbols = ['[',']','(',')',' ','{','}']
    # convert name into format mpv accepts
    for s in symbols:
        name = name.replace(s,f"\{s}")
    os.system(f"mpv --no-terminal {name} &")

def delete_temp():
    os.system('rm -rf ~/Videos/temp')

def close_all():
    os.system("pkill -f mpv")
