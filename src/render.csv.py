from jinja2 import Template, Environment,FileSystemLoader
from pathlib import Path

fname='../data/wc-product-export-24-2-2021.csv'
from myfuncs import ReadCSV
catalog=ReadCSV(fname)

catalog.sort(key=lambda k: k['categorias'])