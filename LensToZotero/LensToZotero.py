from pyzotero import zotero
import os
import csv
import json
import codecs


def get_feild(item, feild):
    if item.get(itemTemplate_list[feild]):
        if item[itemTemplate_list[feild]] != "NA":
            return item[itemTemplate_list[feild]]
    return ""


def get_tags(item, feild):
    tags = []
    for i in itemTemplate_list[feild]:
        if item.get(i):
            if item[i] != "" and item[i] != "NA":
                tags = tags + [{"tag": item[i]}]
    return tags


def get_pages(item, feild):
    if item.get(itemTemplate_list[feild][0]):
        start = item[itemTemplate_list[feild][0]]
    else:
        start = ""
    if item.get(itemTemplate_list[feild][1]):
        end = item[itemTemplate_list[feild][1]]
    else:
        end = ""
    if start != "" and end != "" and start != "NA" and end != "NA":
        return start+"-"+end
    if start == "" or start == "NA":
        return end
    else:
        return start


def get_authors(item, feild):
    author = []
    if item.get(itemTemplate_list[feild]):
        if item[itemTemplate_list[feild]] != "" and item[itemTemplate_list[feild]] != "NA":
            for i in item[itemTemplate_list[feild]].split(";"):
                author = author + [{"creatorType": "author", "firstName": ' '.join(
                    i.split(" ")[:-1]), "lastName":i.split(" ")[-1]}]
    return author


def get_doc(doc_name, cwd):
    """return the requested test document"""
    with open(os.path.join(cwd, "%s" % doc_name), "r") as f:
        return f.read()


def csv_to_json(csvFile, jsonFile):
    jsondict = {}
    with codecs.open(csvFile, encoding='utf-8-sig') as csvfile:
        csv_data = csv.DictReader(csvfile, delimiter=';')
        jsondict["data"] = []

        for rows in csv_data:
            jsondict["data"].append(rows)

    with codecs.open(jsonFile, 'w') as jsonfile:
        jsonfile.write(json.dumps(jsondict["data"]))

    return True


itemType = {
    "": "journalArticle",
        "journal article": "journalArticle",
        "preprint": "preprint",
        "book chapter": "bookSection",
        "conference proceedings article": "conferencePaper",
        "editorial": "journalArticle",
        "review": "journalArticle",
        "report": "journalArticle",
        "dataset": "dataset",
        "letter": "journalArticle",
}

itemTemplate = {
    "title": get_feild,
    "creators": get_authors,
    "abstractNote": get_feild,
    "bookTitle": get_feild,
    "publicationTitle": get_feild,
    "conferenceName": get_feild,
    "volume": get_feild,
    "issue": get_feild,
    "place": get_feild,
    "publisher": get_feild,
    "date": get_feild,
    "pages": get_pages,
    "DOI": get_feild,
    "ISSN": get_feild,
    "ISBN": get_feild,
    "url": get_feild,
    "extra": get_feild,
    "tags": get_tags,
}

itemTemplate_list = {
    "title": "Title",
    "creators": "Author.s",
    "abstractNote": "Abstract",
    "bookTitle": "Source.Title",
    "publicationTitle": "Source.Title",
    "conferenceName": "Source.Title",
    "volume": "Volume",
    "issue": "issue.Number",
    "place": "Source.Country",
    "publisher": "Publisher",
    "date": "Publication.Year",
    "pages": ["Start.Page", "End.Page"],
    "DOI": "DOI",
    "ISSN": "ISSNs",
    "ISBN": "ISSNs",
    "url": "External.URL",
    "extra": "Lens.ID",
    "tags": ["Label", "label_class", "label_cited"],
}


def transfer(file_name):
    library_id = 12823381
    library_type = "user"
    api_key = "lPlZV0aiYzZhWVmSZO6psgGA"
    zot = zotero.Zotero(library_id, library_type, api_key)

    # csvfile = 'pubs_20231024_fix.csv'
    jsonfile = 'pubs_20231024_fix.json'

    csv_to_json(file_name, jsonfile)

    # cwd = os.path.dirname(os.path.realpath("C:/agri/LensToZotero/"))
    cwd = os.getcwd()

    doc = json.loads(get_doc(jsonfile, cwd))

    for item in doc:
        template = zot.item_template(itemType[item["Publication.Type"]])
        for key in template:
            if key in itemTemplate:
                template[key] = itemTemplate[key](item, key)
        list_template = zot.check_items([template])
        resp = zot.create_items(list_template)
