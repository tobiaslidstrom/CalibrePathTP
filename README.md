# CalibrePathTP
Generates a tag based folder structure for exporting books to disc in the Calibre E-Book Manager.

Path structure will look like this:
```
Tag 1/Author/Series (3) - Title/Author - Title
```

## Setup

### Requirements
  * [Calibre E-Book Manager](https://calibre-ebook.com)

### Installation
  * In Calibre open the template editor in `Preferences` > `Saving books to disc` > `Template Editor`
  * Paste the contents of the `template.py` and save
  * Select the books you want to export and press `Save to Disc`
  * Done!

## Usage

### Tags
First tag in the book's tag list will be used
```py
tags = sublist(raw_list("tags", ","), 0, 1, ",");
```

### Authors
List of authors, seperated by comma up to 2 authors
```py
author = sublist(raw_list('authors', ", "), 0, 2, ", ");
```

### Series
Series will be listed if it exist, otherwise title of the book will be shown
```py
series = strcat(field("series"), " (", field("series_index"), ") - ");
```

### Title
Full title will be shown if it's less than 50 characters long, otherwise it's trimmed down
```py
title_trim = strcat(substr(title, 0, 50), " […]");
title = cmp(strlen(title), 50, title, title, title_trim);
```

