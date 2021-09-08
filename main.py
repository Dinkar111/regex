import re
import os
import json


# pattern = r"id=\"bk107\">\s*<author>(.+)</author>(.|\s|\n)*?<description>((.|\s)+?)</description>"
#
# replace_author_pattern = r"(id=\"bk107\">[\s\n]*<author>).*(</author>)"
#
# with open('data.xml', 'r+') as xml_file:
#     xml = xml_file.read()
#     author_name = re.search(pattern, xml).group(1)
#     description = re.search(pattern, xml).group(3)
#
#     print(f"Author Name: {author_name}")
#     print(f"Description: {description}")
#
#     new_content = re.sub(replace_author_pattern, r'\1Madhav\2', xml)
#     xml_file.seek(0)
#     xml_file.truncate()
#     xml_file.write(new_content)
#     print("done")
#


def search_and_add_link_to_new_files():

    search_pattern = r"chrome://[\w-]*"
    lst = []

    for root, directory, files in os.walk("./new directory"):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file_handler:
                file_txt = file_handler.read()
                matched_objects = re.finditer(search_pattern, file_txt)
                for matched in matched_objects:
                    if matched.group() not in lst:
                        lst.append(matched.group())

    new_file = open("matched_link.json", "w")
    json_data = {
        "link": lst
    }
    json_object = json.dumps(json_data)
    new_file.write(json_object)

search_and_add_link_to_new_files()
