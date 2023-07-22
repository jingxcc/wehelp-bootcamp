import csv
import json
import urllib.request as req
import re


def get_image_url(text):
    pattern_img = r"https?://[^\s]*\.(?:jpg|JPG)\b"
    urls = re.split(r"(?=http)", text)
    for url in urls:
        if re.match(pattern_img, url):
            image_url = url
            break
    else:
        image_url = ""
    return image_url


# connect
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with req.urlopen(src) as response:
    data = json.load(response)
result = data["result"]["results"]

# --- process data ---
# stitle: 景點名稱
# address: 區域 *
# longitude: 經度
# latitude: 緯度
# file: 第一張圖檔網址*
DISTRICTS = {
    "中正區",
    "萬華區",
    "中山區",
    "大同區",
    "大安區",
    "松山區",
    "信義區",
    "士林區",
    "文山區",
    "北投區",
    "內湖區",
    "南港區",
}


# process data: address to district
for item in result:
    address = item["address"]
    if address != None:
        idx = address.find("區")
        district = ""
        if idx != -1:
            district = address[idx - 2 : idx + 1]
        if district in DISTRICTS:
            item["district"] = district
        else:
            item["district"] = ""

# process data: result_districts, filter district
result_districts = [item for item in result if item["district"]]

# process data: file to image
for item in result_districts:
    file = item["file"]
    if file != None:
        image_url = get_image_url(file)
        item["image"] = image_url

# process data: mrt_data, data group by mtr
mrt_data = {}
mrt = set()

for item in result_districts:
    if item["MRT"] != None:
        mrt.add(item["MRT"])

for m in mrt:
    mrt_data[m] = []

for item in result_districts:
    if item["MRT"] != None:
        mrt_data[item["MRT"]].append(item["stitle"])

# write attraction.csv
with open("attraction.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for item in result_districts:
        row = [
            item["stitle"],
            item["district"],
            item["longitude"],
            item["latitude"],
            item["image"],
        ]
        writer.writerow(row)

# write mrt.csv
with open("mrt.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for m in mrt:
        row = [m] + mrt_data[m]
        writer.writerow(row)
