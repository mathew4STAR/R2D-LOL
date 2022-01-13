import pafy as pf

def download_video(link):
    video = pf.new(link)
    stream = video.getbest()
    stream.download()
    return video.title()