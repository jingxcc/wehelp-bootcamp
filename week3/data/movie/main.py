import urllib.request as req
import bs4


def getUrlRoot(url):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    request = req.Request(url, headers={"User-Agent": USER_AGENT})

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    return root


def getMovieData(data_movie, url, url_prefix=""):
    # 標題
    # 推文數
    # 發布時間 *
    root = getUrlRoot(url_movie)
    titles = root.find_all("div", class_="title")
    reputations = root.find_all("div", class_="nrec")

    for i in range(len(titles)):
        title = ""
        reputation = ""
        time = ""

        if titles[i].a != None:
            title = titles[i].a.string

            root_article = getUrlRoot(url_home + titles[i].a["href"])
            time = root_article.find(
                "span", class_="article-meta-tag", string="時間"
            ).next_sibling.string

        if reputations[i].span != None:
            reputation = reputations[i].span.string

        data_movie.append({"title": title, "reputation": reputation, "time": time})

    next_link = root.find("a", string="‹ 上頁")
    return data_movie, next_link["href"]


# get data
url_home = "https://www.ptt.cc"
url_movie = "https://www.ptt.cc/bbs/movie/index.html"

data_movie = []
count = 0
while count < 3:
    print(f"===page {count}===")
    data_movie, next_link = getMovieData(data_movie, url_movie, url_home)
    url_movie = url_home + next_link
    print(data_movie)
    count += 1

# write into file
with open("movie.txt", mode="w", encoding="utf-8") as file:
    file.write("")

with open("movie.txt", mode="a", encoding="utf-8") as file:
    for data in data_movie:
        file.write(f"{','.join(str(item) for item in data.values())}\n")
