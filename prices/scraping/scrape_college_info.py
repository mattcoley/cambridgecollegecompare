from lxml import html
import requests
import urllib2
import sys

COLLEGE_LIST = ["Christ's College", "Churchill College", "Clare College"]
BASE_URL = 'http://www.undergraduate.study.cam.ac.uk/colleges/'


def run_scraper():
    # Remove unwanted punctuation, spaces, and capitalization (Christ's College -> christs-college)
    colleges = map(lambda val: val.replace("'", ''), COLLEGE_LIST)
    colleges = map(lambda val : val.replace(' ', '-'), colleges)
    colleges = map(lambda val: val.lower(), colleges)

    college_data = {college_name: find_college_info(college_name) for college_name in colleges}
    print college_data

def find_college_info(college_name):
    college_url = BASE_URL + college_name
    request = urllib2.urlopen(college_url)
    html_page = request.read()

    # Convert the html into something we can parse
    tree = html.fromstring(html_page)

    # X path to relevant data in html page
    base_path = '//*[@id="block-views-college-views-block-3"]/div/div/div/div/div/div[5]/div[2]/div[{}]/text()'
    return {'num_undergrad': label_to_num(tree.xpath(base_path.format(1))),
            'num_year': label_to_num(tree.xpath(base_path.format(2))),
            'num_grad': label_to_num(tree.xpath(base_path.format(3)))}



def label_to_num(label):
    # Go from ['c120 undergraduates'] to 120
    return int(label[0].split(' ')[0].replace('c', '')) or 0

def main():
    run_scraper()

if __name__ == '__main__':
    main()


