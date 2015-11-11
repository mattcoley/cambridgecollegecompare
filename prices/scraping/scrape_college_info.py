# TODO add celery integration

from lxml import html
import urllib2
import sys, os
import django

# Path additions to allow import of Django models
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(SETTINGS_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'pricecompare.settings'
django.setup()

from prices.models import College

BASE_URL = 'http://www.undergraduate.study.cam.ac.uk/colleges/'

# Atypical cases where colleges don't fit typical naming conventions
COLLEGE_EXCLUSIONS = {
        'Hughes': 'Hughes Hall',
        'Lucy Cavendish': 'Lucy Cavendish',
        'Peterhouse': 'Peterhouse',
        'Trinity Hall': 'Trinity Hall'
}

# Colleges with extra text in their description
ANNOYING_COLLEGES = ['hughes-hall', 'lucy-cavendish', 'murray-edwards-college', 'newnham-college', 'st-edmunds-college', 'wolfson-college']

# Collges that are so different they require different parsing
SPECIAL_COLLEGES = ['peterhouse', 'sidney-sussex-college']

def run_scraper():
    print 'Loading Models'

    # Get the college names from the database
    college_list = College.objects.order_by('college_name')
    college_names = [col.college_name for col in college_list]

    # Fix the college names for urls
    college_names = adjust_college_names(college_names)

    # Data we are collecting from website
    data_columns = ['num_of_undergraduates', 'num_of_graduates', 'num_of_incoming']

    print 'Scraping Data'
    # Scrape the data
    college_data = [find_college_info(name) for name in college_names]

    print 'Saving data'
    # Update models and save them
    for i in range(len(college_data)):
        data = college_data[i]
        college = college_list[i]
        for col in data_columns:
            # TODO verify data is somewhat close to existing values
            setattr(college, col, data[col])

        college.save()

def adjust_college_names(college_names):
    # Fix college naming convention annoyances
    college_names = map(lambda val: '{} college'.format(val) if val not in COLLEGE_EXCLUSIONS else COLLEGE_EXCLUSIONS[val], college_names)

    # Remove unwanted punctuation, spaces, and capitalization (Christ's College -> christs-college)
    college_names = map(lambda val: val.replace("'", ''), college_names)
    college_names = map(lambda val : val.replace(' ', '-'), college_names)
    college_names = map(lambda val: val.lower(), college_names)

    # Slight fix for colleges with '&'s in them
    college_names = map(lambda val: val.replace('&', 'and'), college_names)

    return college_names


def find_college_info(college_name):
    # Get the html of the college page on the Cambridge website
    college_url = BASE_URL + college_name
    request = urllib2.urlopen(college_url)
    html_page = request.read()

    # Convert the html into something we can parse
    tree = html.fromstring(html_page)

    # Mature colleges have extra text that we must skip to get to cool part
    offset = 1 if college_name in ANNOYING_COLLEGES else 0

    # X path to relevant data in html page
    base_path = '//*[@id="block-views-college-views-block-3"]/div/div/div/div/div/div[5]/div[2]/div[{}]/text()'

    # Somehow these colleges have different X paths despite being generated from the same template presumably?
    if college_name in SPECIAL_COLLEGES:
        base_path = '//*[@id="block-views-college-views-block-3"]/div/div/div/div/div/div[4]/div[2]/div[{}]/text()'

    # Return the data in a nice format to be saved back to the database
    return {'num_of_undergraduates': label_to_num(tree.xpath(base_path.format(offset+1))),
            'num_of_incoming': label_to_num(tree.xpath(base_path.format(offset+2))),
            'num_of_graduates': label_to_num(tree.xpath(base_path.format(offset+3)))}

def label_to_num(label):
    # Go from ['c120 undergraduates'] to 120
    return int(label[0].split(' ')[0].replace('c', '')) or 0

def main():
    run_scraper()

if __name__ == '__main__':
    main()


