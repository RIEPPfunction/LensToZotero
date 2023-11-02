from pyzotero import zotero

from .utils import *


def transfer(settingsPath):

    settigs = get_settings(settingsPath)

    zot = zotero.Zotero(settigs["library_id"],
                        settigs["library_type"], settigs["api_key"])

    jsonfile = 'lens_json.json'

    csv_to_json(settigs["filePath"], jsonfile)

    doc = json.loads(get_doc(jsonfile, cwd=os.getcwd()))

    delete_doc(jsonfile, cwd=os.getcwd())

    for item in doc:
        template = zot.item_template(itemType[item["Publication.Type"]])
        for key in template:
            if key in itemTemplate:
                template[key] = itemTemplate[key](item, key)
        list_template = zot.check_items([template])
        resp = zot.create_items(list_template)

    print("Transer: "+settigs["filePath"]+" to zotero")
