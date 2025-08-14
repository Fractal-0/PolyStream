from structs import GenerateStream
from rich import print
import requests

addons = [
    "stremio://torrentio.strem.fun/qualityfilter=brremux,hdrall,dolbyvision,dolbyvisionwithhdr,threed,4k,480p,scr,cam/manifest.json"
]

addons = [addon.replace("stremio://", "https://").replace("/manifest.json", "") for addon in addons]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

def requestStreams(type, id):
    streams = []
    
    for addon in addons:
        print(f"{addon}/stream/{type}/{id}.json")
        
        response = requests.get(f"{addon}/stream/{type}/{id}.json", headers=headers)
        response.raise_for_status()
        
        for stream in response.json().get('streams', []):
            try:
                streams.append(GenerateStream(**stream))
            except Exception as e:
                print(f"Failed to parse stream: {stream}")
                print(e)
                exit()
        
    return streams
        
print(requestStreams("movie", "tt1300854"))