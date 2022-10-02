import requests
import re
import json

with open("config.json", encoding="UTF8") as f:
    config = json.loads(f.read())


def downloadVideo(url):
    response = requests.get(url)
    videoName = re.sub(
        r'[/\\:*?"<>|]', '', re.search("<title>(.*?)<\/title>", response.text)[1].strip())
    videoUrl = re.search("video_url: '(.*?)',", response.text)[1]
    print(f"開始下載: {videoName}.mp4...")
    videoBytes = requests.get(videoUrl).content
    print(f"{videoName}.mp4 下載完畢")
    with open(f"{config['rootFolder']}/{videoName}.mp4", "wb") as f:
        f.write(videoBytes)


if __name__ == '__main__':
    # 這裡要傳入該影片的頁面網址
    downloadVideo("https://85tube.com/videos/999999/xxxxxxxxxxxxxxxxxxxxxxx/")
