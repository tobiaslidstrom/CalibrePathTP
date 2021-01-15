program:
tags = sublist(raw_list("tags", ","), 0, 1, ",");
author = sublist(raw_list('authors', ", "), 0, 2, ", ");
series = strcat(field("series"), " (", field("series_index"), ") - ");
title = re(field("title"), ":", " -");

if field("series") == "" then
	series = ""
fi;

title_trim = strcat(substr(title, 0, 50), " […]");
title = cmp(strlen(title), 50, title, title, title_trim);

strcat(tags, "/", author, "/", series, title, "/", author, " - ", title);
