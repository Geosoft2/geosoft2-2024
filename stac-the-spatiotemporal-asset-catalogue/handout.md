@Juliarotert

<img width="100" alt="Logo" src="https://github.com/user-attachments/assets/5664ee5f-bb0c-4947-894d-fd96f22d1edd">

# **STAC: the SpatioTemporal Asset Catalog**

## Introduction 
> **"The STAC Specification is a common language to describe geospatial information, so it can more easily be worked with, indexed, and discovered."** [^1]
- Short description in own words: ...

- STAC: concept/ standard
- STAC Specification: technical document/ descriptions

- SpatioTemporal Asset
    - "any file that represents information about the Earth captured in a certain place and at a particular time" [^2]
- Catalog
    - "a complete, usually alphabetical list of items, often with notes giving details" [^3]

- Origin: scenes of satellite imagery
- Presence: variety of (spatiotemporal) uses, e.g. Point Clouds or Data Cubes

## Overview
- Concept and implementation of common metadata for spatiotemporal assets
- Useful for Data providers, Developers and Data users
- Components/ Core Specifications:
    - STAC Item - core atomic unit
    - STAC Catalog - JSON file of links 
    - STAC Collection - extension with additional information
    - STAC API - endpoint for search

### What is STAC?
- Collection of Specifications and Software
- Describes spatial and/or temporal data
- Common structure for describing and cataloging spatiotemporal assets
- "aim to standardize the way geospatial asset metadata is structured and queried"

### Why is STAC relevant?
- "The goal is for all providers of spatiotemporal assets (Imagery, SAR, Point Clouds, Data Cubes, Full Motion Video, etc) to expose their data as SpatioTemporal Asset Catalogs (STAC), so that new code doesn't need to be written whenever a new data set or API is released"
- "To establish a standard, unified language to talk about geospatial data, allowing it to be more easily searchable and queryable"
- Data is often provided similar but not as much the same as they can be found by users in one search
- STAC solves this Problem by providing common metadata for spatiotemporal Data
- The easy implementable but customizable and flexible standard makes STAC attractive for providers, developers and users

### How does the STAC Specification work?

<img width="1222" alt="archive_infra" src="https://github.com/user-attachments/assets/8aede27e-2b22-44ca-82f9-fd60fbed61e1">

- Network of JSON-Files referencing other JSON-files (linked with each other)

- detailed description of core-specifications

- Components are semi-independent: can be used alone but work better together
**STAC Item**
![STAC-Item](https://github.com/user-attachments/assets/34514af4-8488-4bb0-9167-c7eee5553ca4)

**STAC Catalog**
![Catalog-layout](https://github.com/user-attachments/assets/a2a7ced6-e637-4d3d-8374-e6dc3e8e3d97)

**STAC Collection**
![STAC-Collection](https://github.com/user-attachments/assets/764d7d8a-3f83-4372-9946-f330b0f9eb88)

**STAC API**

- Links:


## STAC Extensions
- For adding specific metadata
- Many extensions are hosted in GitHub
- General json-schema includes properties and definitions for (objects of the) extensions such as types or items

<details>
<summary>Code extract of the json-schema eo-extension defining the object "eo:cloud_cover":</summary>
    
                "properties": {
                  "summaries": {
                    "type": "object",
                    "$comment": "We can't properly validate summary objects types (min/max or schemas) yet.",
                    "allOf": [
                      {
                        "$ref": "#/definitions/validate_bands"
                      },
                      {
                        "properties": {
                          "eo:cloud_cover": {
                            "type": ["array", "object"],
                            "items": {
                              "$ref": "#/definitions/eo:cloud_cover"
                            }
    
</details>

### EO: Electro-Optical Extension
- 
- **Examples:**
    - eo:cloud_cover -> Estimate, percentage
    - eo:center_wavelength -> of the band, micrometers
    - eo:solar_illumination -> of the band, as measured at half the maximum transmission, W/m2/micrometers
<details>
<summary>Code extract of a STAC-Item with eo-extension:</summary>
    
      "properties": {
        "datetime": "2020-12-11T22:38:32.125Z",
        "created": "2020-12-12T01:48:13.725Z",
        "updated": "2020-12-12T01:48:13.725Z",
        "platform": "cool_sat2",
        "instruments": [
          "cool_sensor_v1"
        ],
        "gsd": 0.66,
        "eo:cloud_cover": 1.2,
        "eo:snow_cover": 0
      },
      "assets": {
        "analytic": {
          "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "title": "4-Band Analytic",
          "roles": [
            "data"
          ],
          "eo:cloud_cover": 1.2,
          "bands": [
            {
              "name": "band1",
              "eo:common_name": "blue",
              "eo:center_wavelength": 0.47,
              "eo:full_width_half_max": 0.07,
              "eo:solar_illumination": 1959.66
            },
</details>



### MLM: Machine Learning Model Extension
-
- **Examples:**
    - mlm:name
    - mlm:memory_size
    - mlm:input

<details>
<summary>Code extract of a STAC-Item with mlm-extension:</summary>
    
        properties": {
        "description": "Basic STAC Item with only the MLM extension and no other extension cross-references.",
        "datetime": null,
        "start_datetime": "1900-01-01T00:00:00Z",
        "end_datetime": "9999-12-31T23:59:59Z",
        "mlm:name": "example-model",
        "mlm:tasks": [
          "classification"
        ],
        "mlm:architecture": "ResNet",
        "mlm:input": [
          {
            "name": "Model with RGB input that does not refer to any band.",
            "bands": [],
            "input": {
              "shape": [
                -1,
                3,
                64,
                64
              ],
              "dim_order": [
                "batch",
                "channel",
                "height",
                "width"
              ],
              "data_type": "float32"
            }
   
    
</details>

### Combination of eo and mlm

## Conclusion
- Advantages:
- Disadvantages:
- Conclusion-sentence:

## Sources
- stacspec
    - https://stacspec.org/en/
    - https://stacspec.org/en/about/
    - https://stacspec.org/en/about/stac-spec/
    - https://stacspec.org/en/tutorials/intro-to-stac/
- Github
    - https://stac-extensions.github.io/
    - https://github.com/radiantearth/stac-spec/
    - https://github.com/radiantearth/stac-spec/tree/master/extensions
    - https://github.com/stac-extensions/eo
    - https://github.com/stac-extensions/eo/blob/main/examples/item.json
    - https://github.com/radiantearth/stac-spec/blob/master/overview.md
    - https://github.com/radiantearth/stac-spec/tree/v0.8.1/extensions/eo
    - https://github.com/stac-extensions/mlm
    - https://github.com/stac-extensions/mlm/blob/main/examples/item_eo_bands.json
- Others
    - https://gogeomatics.ca/spatiotemporal-asset-catalogs-enabling-online-search-and-discovery-of-geospatial-assets/
    - 

[^1]: https://stacspec.org/en/
[^2]: https://github.com/radiantearth/stac-spec/
[^3]: https://www.collinsdictionary.com/de/worterbuch/englisch/catalogue




