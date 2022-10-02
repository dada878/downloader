from bs4 import BeautifulSoup
import requests
from multiVideos import downloadMultiVideos


def DownloadFromSearch(keywords, limit):
    videoList = []

    for keyword in keywords:
        for num in range(limit):
            print(f"正在搜尋關鍵字 {keyword} 第 {str(num+1)} 頁")
            page = num + 1
            url = f"https://85tube.com/search/{keyword}/?mode=async&function=get_block&block_id=list_videos_videos_list_search_result&q={keyword}&category_ids=&sort_by=&from_videos={page}"
            response = requests.get(url)
            if response.status_code != 200:
                break
            soup = BeautifulSoup(response.text, "html.parser")
            videoItems = soup.find_all("div", class_="item")
            for video in videoItems:
                videoList.append(video.find("a").get("href"))

    downloadMultiVideos(videoList)


if __name__ == '__main__':
    # 第一個參數傳入要搜尋的關鍵字(多個)
    # 第二個參數傳入最多抓幾頁
    DownloadFromSearch([
        "Keyword1",
        "Keyword2",
        "Keyword3",
    ], 10)
