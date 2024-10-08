# STAC Clients for R and Python
[Introduction](#introduction)

[STAC Clients for R](#stac-clients-for-r)

[STAC Clients for Python](#stac-clients-for-python)

## Introduction
In R and Python, it is possible to explore STACs. In this handout, we aim to provide a brief introduction on how to query STACs, access their metadata, and retrieve the associated datasets.
## STAC Clients for R

## STAC Clients for Python
Similarly to R, Python provides an extension called pystac to facilitate the use of STACs. The following sections will provide an overview of the functions and a quick start guide.

### How to get started with pystac


The first step is to import the pystac library to your project, along with any other libraries you may require to work with Collections, Items and Assets in a straightforward way.

```python
import json
import requests
import pystac

from pystac import Catalog, get_stac_version
from pystac_client import Client
from pystac.extensions.eo import EOExtension
from pystac.extensions.label import LabelExtension
```
Furthermore some extensions of pystac are added. Their functionality will be explained when they are first used.

### How to work with existing STACs

In Order to work with an existing STAC you need to obtain the STACs URL. Depending on the extensions that are used, different functions apply.
Standard:
```python
catalog = Catalog.from_file('LINK')
catalog.describe()
```
With the Client-Extension of pystac
```python
catalog_url = 'LINK'
client = Client.open(catalog_url)
```

### How to obtain some information on STACs
STACs provide a range of information about their collections, items and assets, with some fields being mandatory and others optional. As a result, certain parameters can be obtained with certainty: 
```python
print(f"ID: {catalog.id}")
print(f"Title: {catalog.title or 'N/A'}")
print(f"Description: {catalog.description or 'N/A'}")
```
This semantic is applicable to all objects within a STAC and can be utilised for the retrieval of metadata across all potential parameters: 
```python
print(item.geometry)
print(item.bbox)
print(asset.media_type)
print(asset.href)
...
```
> **get_collections()** retrieves the collections in the given catalog.
>
> **get_collection(*collection_id*)** returns a single collection from the catalog, identified by the ID.
>
> **get_items(*id, recursive=Bool*)** returns all items within a specified catalog. In this context, the "id" parameter can be omitted, as the "recursive" parameter determines whether subcatalogs are traversed.
>
> **get_all_items** retrieves all items from given catalog and all subcatalogs

All these functions are used with "[Object].[Function]".

Additionally, the number of collections within a STAC can be quantified and displayed in a list or any other desired format. This approach combines existing Python syntax with the previously presented pystac functions.
```python
collections = list(catalog.get_collections())
print(f"Number of collections: {len(collections)}")
print("Collections IDs:")
for collection in collections:
    print(f"- {collection.id}")

items = list(catalog.get_all_items())

print(f"Number of items: {len(items)}")
for item in items:
    print(f"- {item.id}")
```


### How to search in a exisiting STAC

### How to download data from a STAC

### How to create your own STAC with pystac

```python

```