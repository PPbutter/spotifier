import requests as req
import shutil
class songData:
    def __init__(self, data:bytes or str):
        self.song_data = data

    def dump(self) -> bytes:
        return self.song_data

def getSong(link:str):
    resp = req.get('https://api.song.link/v1-alpha.1/links?url='+link.split('https://')[1])
    cheez = resp.json()
    resp.close()
    jsonDATA = {
    'UniqueId' : cheez['entityUniqueId'],
        'ID': cheez['entitiesByUniqueId'][cheez['entityUniqueId']]['id'],
        'title' : cheez['entitiesByUniqueId'][cheez['entityUniqueId']]['title'],
        'artist' : cheez['entitiesByUniqueId'][cheez['entityUniqueId']]['artistName'],
        'thumbnailUrl' : cheez['entitiesByUniqueId'][cheez['entityUniqueId']]['thumbnailUrl'],
        'rawName' : cheez['entitiesByUniqueId'][cheez['entityUniqueId']]['artistName']+'-'+cheez['entitiesByUniqueId'][cheez['entityUniqueId']]['title']+'.mp3'
    }
    respp = req.get('https://eternalbox.dev/api/audio/jukebox/'+jsonDATA['ID'])
    return {'info':jsonDATA,'DATA':songData(respp.content)}


def download(dat):    
    title,artist = dat['info']['title'],dat['info']['artist']
    
    #print(f'successfully collected... {title} by {artist}')
    
    try:
        with open(dat['info']['artist']+'-'+dat['info']['title']+'.mp3','wb') as file:
            file.write(dat['DATA'].dump())
            file.close()
        shutil.move(dat['info']['artist']+'-'+dat['info']['title']+'.mp3','music/'+dat['info']['artist']+'-'+dat['info']['title']+'.mp3')
    except:
        return True
    return False