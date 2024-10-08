# STAC Clients for R and Python
[Introduction](#introduction)

[STAC Clients for R](#stac-clients-for-r)

[STAC Clients for Python](#stac-clients-for-python)

[Comparison](#comparison-between-rstac-and-pystac)

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

## Comparison between rstac and pystac