import cheezer
import streamlit as stream
import os

def ajig():
    stream.success(f"Now playing {i['title']} by {i['artist']}...")
    stream.audio(f"music/{i['rawName']}")

stream.title('spotifier')
cheez = []
p = stream.text_input('Song name or url')
z = False
if p != '':
    for a,b,c in os.walk('music'):
        if a == 'music':
            global found
            found = False
            for ii in c:
                info = {
                    'title' : ii.split('-')[1].replace('.mp3',''),#.replace(' '),
                    'artist' : ii.split('-')[0],#.replace(' '),
                    'rawName' : ii
                }
                #stream.write(info['title'].split('.')[::-1][0])
                del info['title'].split(' ')[len(info['title'].split(' '))-1]
                del info['artist'].split(' ')[len(info['artist'].split(' '))-1]
                cheez.append(info)
        for i in cheez:
            if p.lower() in i['title'].lower() or p.lower() in i['artist'].lower():
                if stream.button(f"{i['title']} | {i['artist']}",key=i['title']):
                    stream.success(f"{i['title']} by {i['artist']}...")
                    stream.audio(f'music/{i["rawName"]}')
        if p.startswith('https://open.spotify.com'):
            stream.write('fetching Song...')
            juh = cheezer.getSong(p)
            #stream.write(juh)
            p=False
            for i in cheez:
                if i['rawName']==juh['info']['artist']+'-'+juh['info']['title']+'.mp3':
                    if stream.button(f"{i['title']} by {i['artist']}",key=i['title']):
                        stream.success(f"{i['title']} by {i['artist']}...")
                        stream.audio(f'music/{i["rawName"]}')
                    p=True
            if not p:
                if stream.button(f"{juh['info']['title']} by {juh['info']['artist']}",key=juh['info']['title']):
                        cheezer.download(juh)
                        stream.success(f"now playing {juh['info']['title']} by {juh['info']['artist']}...")
                        stream.audio(f'music/{juh["info"]["rawName"]}')

#stream.audio(open('Deftones - Lhabia.mp3','rb'))