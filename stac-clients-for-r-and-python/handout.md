# STAC Clients for R and Python
by [Mika Dinnus](https://github.com/MikaDinnus) and [Lukas Räuschel](https://github.com/lraeuschel)
## Content
[Introduction](#introduction)

[STAC Clients for R](#stac-clients-for-r)

[STAC Clients for Python](#stac-clients-for-python)

[Comparison](#comparison-between-rstac-and-pystac)

[Sources](#sources)

## Introduction
With R and Python, you can easily explore STACs, which provide access to Earth observation data. In this handout, we'll give a quick introduction on how to query STACs, get their metadata, and download the related datasets using both R and Python.

## STAC Clients for R
In R, the rstac package allows you to interact with STACs. It provides a range of functions for accessing, searching, and downloading Earth observation data through the STAC protocol.
### Installation and Import of the package
To install the package you can use CRAN:
```r
install.packages("rstac")
```
After installation, ensure that you import the package into your R session:
```r
library(rstac)
```
### Functions
#### Connect to a STAC:
To connect to a STAC, save the URL and use the following function:
```r
stac_url <- "example.url"
stac_obj <- stac(stac_url)
```
#### Conformance classes:
Conformance classes define the specific API standards that a STAC server implements. These standards ensure interoperability, meaning that different STAC services and clients can communicate effectively by following the same set of rules. By checking conformance, you can verify which functionalities the STAC API supports.
```r
stac_obj %>% conformance() %>% get_request()
```
#### Get Metadata about the STAC and the Collections:
Once connected, you can retrieve information about the STAC service:
```r
stac_obj %>% get_request()
```
To get the available collections, use:
```r
stac_obj %>% collections() %>% get_request()
```
#### Search Queries:
To search for specific items within a collection, you can set up a search query:
```r
query <- stac_search(
    q = stac_obj, # STAC object
    collections = "example-name", # Name of a collection, concatenation functions are also possible
    datetime = "2021-01-01/2021-12-31", # Time interval for the search
    limit = 10 # Limit the number of results returned
)
query %>% get_request()
```
In addition to basic search options, you can also filter results by intersections with a geometry or bounding box (bbox), and sort them by specific attributes ( e.g. datetime, id, ground sample distance (gsd), ...).
#### Asset download:
To download assets of an item, rstac provides a convenient function:
```r
assets_download(
    query, # STAC search query
    asset_id = "example-asset-name", # Name of the specific asset to download
    output_dir = "path-to-the-output-dir", # Directory where downloaded files will be saved
    overwrite = TRUE # Overwrite existing files if they already exist
)
```
Now you have donwloaded your data and the files are ready to use.

## STAC Clients for Python
Similarly to R, Python provides an extension called pystac to facilitate the use of STACs. The following sections will provide an overview of the functions and a quick start guide.

### How to get started with pystac
If you have not yet installed pystac on your computer, please do so.  
```console
pip install pystac
```

The first step is to import the pystac library to your project, along with any other libraries you may require to work with Collections, Items and Assets in a straightforward way.

```python
import json
import requests
import pystac

from pystac import Catalog, get_stac_version
from pystac_client import Client

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
> **get_all_items()** retrieves all items from given catalog and all subcatalogs

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
In some cases, it is necessary to narrow down the information you wish to retrieve. In such instances, a search without downloading all data is a logical solution. In pystac, a search can be conducted through the Client Extension.
```python
catalog_url = 'example_url'
client = Client.open(catalog_url)

search = client.search(
    parameter = value,
    limit = value
)
```
The search can be refined using existing parameters and their associated values. In some cases, it may be beneficial to limit the data search using the 'limit' parameter.
> **open(*url*)** works with the client extension and integrates a stac
>
> **search(*parameter = value, (..)*)** works with the client extension, searching for a STAC object 

### How to download data from a STAC
To download data from a STAC, the pystac library's requests extension should be used. This extension interacts with the API, allowing the data to be downloaded to the user's drive.

```python
for asset_key in item.assets:
    asset = item.assets[asset_key]
    asset_url = asset.href
    file_name = asset_key + '.' + asset.media_type.split('/')[-1]
    
    response = requests.get(asset_url)
    
    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    print(f'{file_name} heruntergeladen.')
```

## Comparison between rstac and pystac
rstac and pystac both allow users to access SpatioTemporal Asset Catalogs (STAC) for geospatial data, but they cater to different programming languages. rstac is tailored for R users, integrating well with R's data analysis and visualization tools like sf and terra. In contrast, pystac is designed for Python users, working seamlessly with Python libraries like requests. Your choice between them depends on whether you prefer R or Python for your data analysis tasks.


## Sources
https://stacspec.org/en/tutorials/
https://brazil-data-cube.github.io/rstac/
https://pystac.readthedocs.io/en/stable/
