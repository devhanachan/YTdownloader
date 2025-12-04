import yt_dlp

### These code are ass I will never use it again
def getTitle(url: str) -> str:
    try:
        info = yt_dlp.YoutubeDL({'quiet': True}).extract_info(url, download=False)
        return info.get('title', 'Title not found')
    except Exception as error:
        return f"Error: {error}"

def getThumbnails(url: str) -> str:
    try:
        info = yt_dlp.YoutubeDL({'quiet': True}).extract_info(url, download=False)
        return info.get('thumbnail', '')
    except:
        return ""   # avoid returning error strings

def getViews(url: str) -> str:
    try:
        info=yt_dlp.YoutubeDL({'quiet': True}).extract_info(url, download=False)
        return info.get('view_count', 'noview?')
    except:
        return ""
### ass code ends here


def get_video_info(url: str):
    try:
        info=yt_dlp.YoutubeDL({'quiet': True}).extract_info(url, download=False)
        return{
            "title": info.get('title','notitle'),
            "thumbnail": info.get('thumbnail',''),
            "views":info.get('view_count',0),
            "channel":info.get('channel','Unknown'),
            "upload_date":info.get('upload_date','Unknown'),
            "duration":info.get('duration',0),
            "likes":info.get('like_count'),

        }
    except Exception as error:
        return {'error': str(error)}