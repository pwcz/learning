#!/usr/bin/env python3.9
from graphlib import TopologicalSorter


dependencies = {
    "realpython-reader": {"feedparser", "html2text"},
    "feedparser": {"sgmllib3k"},
}

ts = TopologicalSorter(dependencies)
print(list(ts.static_order()))

