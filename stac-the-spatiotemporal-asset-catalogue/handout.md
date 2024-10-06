@Juliarotert

# **STAC: the spatiotemporal asset catalogue**

## Introduction 
- short description
- SpatioTemporal Asset
    - "any file that represents information about the Earth captured in a certain place and at a particular time" [^1]
- catalogue
    - "a complete, usually alphabetical list of items, often with notes giving details" [^2]
- Origin: scenes of satellite imagery
- Presence: variety of uses

## Overview

- The STAC Specification
- Components/ Core Specifications
    - Item
    - Catalog
    - Collection
- Components can be used alone but best together
- API Specification

### What
- Collection of Specifications and Software
- Describes spatial and/or temporal data
- Common structure for describing and cataloging spatiotemporal assets
- "aim to standardize the way geospatial asset metadata is structured and queried"

### why
- "The goal is for all providers of spatiotemporal assets (Imagery, SAR, Point Clouds, Data Cubes, Full Motion Video, etc) to expose their data as SpatioTemporal Asset Catalogs (STAC), so that new code doesn't need to be written whenever a new data set or API is released"
- "To establish a standard, unified language to talk about geospatial data, allowing it to be more easily searchable and queryable"

### how
- Network of JSON-Files referencing other JSON-files (kind of linked)
- Links:
- API:
- detailed description of core-specifications
    - Item:
    - Catalog:
    - Collection:

## STAC Extensions
- for adding specific metadata
- many extensions are hosted in GitHub
- json-schema includes descriptions, properties and definitions (for parts) of the extension such as types, items
<details>
<summary>Code extract of the json-schema eo-extension</summary>
    
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

[^1]: https://github.com/radiantearth/stac-spec/
[^2]: https://www.collinsdictionary.com/de/worterbuch/englisch/catalogue




