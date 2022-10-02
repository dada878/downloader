from downloader import downloadVideo
from threading import Thread


def downloadMultiVideos(videoList):
    threads = []

    for videoUrl in videoList:
        threads.append(Thread(target=downloadVideo, args=(videoUrl, )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # 這裡要傳入要下載的影片頁面網址(可傳進多個)
    downloadMultiVideos([
        "https://85tube.com/videos/999999/xxxxxxxxxxxxxxxxxxxxxxx/",
        "https://85tube.com/videos/999999/xxxxxxxxxxxxxxxxxxxxxxx/"
    ])
