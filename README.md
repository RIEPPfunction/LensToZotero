# LensToZotero

Transfer Lens publications in csv format to Zotero

# Quickstart

1. `pip install LensToZotero`
2. You'll need the ID of the personal or group library you want to access:
   - Your **personal library ID** is available [here](https://www.zotero.org/settings/keys), in the section `Your userID for use in API calls`
   - For **group libraries**, the ID can be found by opening the group's page: `https://www.zotero.org/groups/groupname`, and hovering over the `group settings` link. The ID is the integer after `/groups/`
3. You'll also need<sup>†</sup> to get an **API key** [here](https://www.zotero.org/settings/keys/new)
   - press "Allow write access" button, when you create your key
4. Are you accessing your own Zotero library? `library_type` is `'user'`
5. Are you accessing a shared group library? `library_type` is `'group'`.

Then create a file settings.txt:

```txt
filePath doc_name.csv
library_id your_id
library_type user
api_key your_api_key
```

And place setting.txt and doc_name.csv near the root of the called function.

# Using

Example:

```python
from LensToZotero.LensToZotero import transfer

transfer("doc_name.csv")
```
