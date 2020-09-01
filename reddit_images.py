import urllib.request
import time
import re
import os

# default reddit url
url_string = "http://www.reddit.com/r/EarthPorn/top/?sort=top&t=day"
# default folder to save images
folder = 'img/'

def run_scraper():
    delete_old_images() # cleans out previously downloaded images
    [url_list, number_images] = get_links()
    img_name = 0
    num_urls = len(url_list)
    # Script will grab 2 urls for each image (how Reddit is set up, I think)
    for index in range(0, num_urls, 2):
        url = url_list[index]
        file_name = "img/" + \
            time.strftime("%m") + "_" + time.strftime("%d") + \
            "_" + "%d.jpg" % img_name
        img_name += 1

        get_images(url, file_name)


def get_links():
    req = urllib.request.Request(url_string, headers={'User-Agent': 'Mozilla/5.0'})
    html_source = urllib.request.urlopen(req).read().decode("iso-8859-1")
    # Reddit selfhost images now not using imgur
    url_list = re.findall("https://i.redd.it/\w+.jpg", str(html_source))
    number_images = len(url_list)
    return url_list, number_images


def get_images(img_url, fileName):
    return urllib.request.urlretrieve(img_url, fileName)

def delete_old_images():
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print (e)

if __name__ == "__main__":
    run_scraper()