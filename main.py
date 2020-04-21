# better to try making our homework  with functions and additionally "sort, sorted, split"



import json
import operator
from pprint import pprint
import xml.etree.ElementTree as ET


tree = ET.parse('newsafr.xml')
root = tree.getroot()


with open('newsafr.json', encoding='utf-8') as file:
    json_data = json.load(file)


def collecting_words_json(data):
    """
    Initially collecting words from JSON and forming a list
    with them

    """
    words_collection = []
    json_words = []
    for news in data['rss']['channel']['items']:
        words_collection = news['description'].split()
        for word in words_collection:
            if len(word) > 6:
                json_words.append(word.lower())
    json_words.sort()
    return json_words


def collecting_words_xml(root):
    """
    Initially collecting words from XML and forming a list
    with them

    """
    news_xml = []
    xml_items = root.findall('channel/item')
    for item in xml_items:
        news_xml += item.find('description').text.split()
    xml_words = []
    for word in news_xml:
        if len(word) > 6:
            xml_words.append(word.lower())
    xml_words.sort()
    return xml_words


def finding_frequent_words(top_words):
    """
    Determining the most frequently met words

    """
    count = 1
    top_words_dict = {}
    reference_word = top_words[0]
    
    for word in top_words:
        if word == reference_word:
            count += 1
            top_words_dict[word] = count
        else:
            reference_word = word
            count = 1
    top_words_dict_sorted = sorted(top_words_dict.items(), key=operator.itemgetter(1), reverse=True)
    return top_words_dict_sorted


def printing_top_10_words(top_words_dict):
    """
    Printing the 10 most frequently met words
    
    """
    print('\n10 most frequently met words in the news provided for our analysis (word cited, times met):\n')
    start_point = 0
    while start_point != 10:
        pprint(top_words_dict[start_point])
        start_point += 1


print('\nWorking with JSON-data')
top_words_json = collecting_words_json(json_data)
json_words_dict = finding_frequent_words(top_words_json)
printing_top_10_words(json_words_dict)

print('\nWorking with XML-data')
top_words_xml = collecting_words_xml(root)
xml_words_dict = finding_frequent_words(top_words_xml)
printing_top_10_words(xml_words_dict)


