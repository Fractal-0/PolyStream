from typing import overload, Union
from typing_extensions import Literal
from pydantic import BaseModel, TypeAdapter
from typing import Optional


class BaseStream(BaseModel):
    name: str
    title: str
    filename: Optional[str] = None
    bingeGroup: Optional[str] = None


class TorrentStream(BaseStream):
    type: Literal["torrent"]
    infoHash: str
    fileIdx: Optional[int] = None
    sources: Optional[list[str]] = None


class HttpStream(BaseStream):
    type: Literal["http"]
    url: str


class YouTubeStream(BaseStream):
    type: Literal["youtube"]
    ytId: str


class ExternalStream(BaseStream):
    type: Literal["external"]
    url: str


StreamUnion = Union[TorrentStream, HttpStream, YouTubeStream, ExternalStream]

@overload
def Stream(*, name: str, title: str, type: Literal["torrent"], infoHash: str, fileIdx: Optional[int] = ..., filename: Optional[str] = ..., bingeGroup: Optional[str] = ...) -> TorrentStream: ...
@overload
def Stream(*, name: str, title: str, type: Literal["http"], url: str, filename: Optional[str] = ..., bingeGroup: Optional[str] = ...) -> HttpStream: ...
@overload
def Stream(*, name: str, title: str, type: Literal["external"], url: str, filename: Optional[str] = ..., bingeGroup: Optional[str] = ...) -> ExternalStream: ...
@overload
def Stream(*, name: str, title: str, type: Literal["youtube"], ytId: str, filename: Optional[str] = ..., bingeGroup: Optional[str] = ...) -> YouTubeStream: ...

def GenerateStream(**data) -> StreamUnion:
    if data.get('type'):
        if data['type'] in ['torrent', 'http', 'youtube', 'external']:
            pass
        ValueError("Invalid stream type provided")
    
    elif data.get('infoHash'):
        data['type'] = 'torrent'
        
    elif data.get('url'):
        data['type'] = 'http'
        
    elif data.get('ytId'):
        data['type'] = 'youtube'
        
    elif data.get('externalUrl'):
        data['type'] = 'external'
        data['url'] = data.pop('externalUrl')
        
    else:
        raise ValueError("Could not infer stream type. Please provide 'type' field.")
    
    data['filename'] = data.get('behaviorHints', {}).get('filename')
    data['bingeGroup'] = data.get('behaviorHints', {}).get('bingeGroup')
    
    return TypeAdapter(StreamUnion).validate_python(data)