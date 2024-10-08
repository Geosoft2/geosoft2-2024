@Juliarotert

<img width="100" alt="Logo" src="https://github.com/user-attachments/assets/5664ee5f-bb0c-4947-894d-fd96f22d1edd">

# **STAC: the SpatioTemporal Asset Catalog**

## Introduction 
> **"The STAC Specification is a common language to describe geospatial information, so it can more easily be worked with, indexed, and discovered."** [^1]

- STAC: concept/ standard/ community of collaborators
- STAC Specification: technical document/ descriptions/ markdown pages on GitHub

- SpatioTemporal Asset
    - "any file that represents information about the Earth captured in a certain place and at a particular time" [^2]
- Catalog
    - "a complete, usually alphabetical list of items, often with notes giving details" [^3]
    - In STAC: a collection of standards for metadata of spatiotemporal assets in the form of links to items or sub-catalogs

- Based on JSON files
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
- Data examples:
    - Imagery (satellites, airplanes, drones)
    - Synthetic Aperture Radar (SAR)
    - Point clouds (LiDAR, structure from motion, ...)
    - Data cubes
    - Full motion video

### What is STAC?
- Standard for Spatiotemporal data
- Common structure for describing and cataloging spatiotemporal assets based on JSON
- Collection of Specifications and Software

**Key words:** standardization, structure, queryable, accessability, interoperability, customizable, flexible, extensible, persistent, reliable, approachable

### Why is STAC relevant?
- STAC makes geospatial data searchable and queryable based on a standard, unified language
- To decrease the writing of code for new releasings by exposing existing data as SpatioTemporal Asset Catalogs
    - Existing metadata structures or extensions can be reused or customized
- Data is often provided similar but not as much the same as they can be found by users in one search
    - STAC solves this Problem by providing common metadata for spatiotemporal Data
- The easy implementable but customizable and flexible standard makes STAC attractive for providers, developers and users
    - Data providers: esasy providing of data because of standardization, simple hosting and many server side tools for better search and security
    - Developers: a given but extendable format and many open source tools and ressources to use for developing
    - Data users: its no more necessary to write own code or search for data in various platforms

### How does STAC work?

- Brings the metadata in a standardized structure to make it queryable and searchable
- Network of JSON-Files referencing other JSON-files (linked to each other)
- Consists of four core component specifications wich are semi-independent: can be used alone but work best in concert with one another

### Core components
**STAC Item**

The Item is the fundamental and core atomic unit of STAC. Being a GeoJSON feature it can be read by GIS or geospatial librarys. It can describe one or more spatiotemporal asset(s) like all bands (assets) of one imagery scene in one item. An item has fields which consist of the existing GeoJSON fields such as id, type, geometry, bbox and properties and additional STAC Item fields which are partially optional. These Fields are e.g. the stac_version, links, assets, stac_extensions or collections. 
A list of item fields is provided on [GitHub item-spec](https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md).


<img width="500" alt="items" src="https://github.com/user-attachments/assets/34514af4-8488-4bb0-9167-c7eee5553ca4">


**STAC Catalog**

A STAC Catalog can link various STAC Items together. A catalog contains a list of STAC Items and of child STAC Catalogs. A catalog can be linked with Items, Collections and other catalogs. 

<img width="400" alt="catalogs" src="https://github.com/user-attachments/assets/a2a7ced6-e637-4d3d-8374-e6dc3e8e3d97">
<img width="300" alt="collections" src="https://github.com/user-attachments/assets/97e97c9b-a474-489b-93dd-7a934857450a">


**STAC Collection**

Within a collection of geospatial data there can be common additional information regarding to these kinds of data. It consists of assets with the same properties on a higher level. A STAC Collection includes additional fields for this additional information. As a standalone it is a lightweight way to describe data holdings.

<img width="600" alt="collections" src="https://github.com/user-attachments/assets/764d7d8a-3f83-4372-9946-f330b0f9eb88">


**(STAC API)**

A STAC API is a service interface for search and differs from the other specifications because it is not only a JSON file but more a dynamic system with various parts. It has access over a group of STAC objects, which are usually held in a database.

<img width="800" alt="archive_infra" src="https://github.com/user-attachments/assets/8aede27e-2b22-44ca-82f9-fd60fbed61e1">


## STAC Extensions
- To add specific metadata in different use cases or more detail about specific data types
- Many extensions are hosted in GitHub
- Basic JSON-schema includes properties and definitions for (objects of the) extensions such as types or items

<details>
<summary>Code extract of the json-schema for the eo-extension defining the object "eo:cloud_cover":</summary>
    
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

### eo: Electro-Optical Extension

The eo Extension refers to EO data which are snapshots of the earth for a single date and time. This extension is specified on the electro-optical field so it contains information e.g. about the platform, the physical conditions and bands.

**Examples:**
- eo:cloud_cover -> Estimate, percentage
- eo:center_wavelength -> of the band, micrometers
- eo:solar_illumination -> of the band, as measured at half the maximum transmission, W/m2/micrometers
- [More examples](https://github.com/radiantearth/stac-spec/tree/v0.8.1/extensions/eo#item-fields)

<details>
<summary>Code extract of a Landsat 8 Item from the collection "landsat-8-11" with eo-extension:</summary>
    
      "properties": {
        "collection": "landsat-8-l1",
        "datetime": "2018-10-01T01:08:32.033Z",
        "eo:cloud_cover": 78,
        "eo:sun_azimuth": 168.8989761,
        "eo:sun_elevation": 26.32596431,
        "landsat:path": 107,
        "landsat:row": 18,
        "eo:gsd": 30,
        "eo:platform": "landsat-8",
        "eo:instrument": "oli_tirs",
        "eo:off_nadir": 0,
        "eo:bands": [
            {
                "name": "B1",
                "common_name": "coastal",
                "gsd": 30,
                "center_wavelength": 0.44,
                "full_width_half_max": 0.02
            },
</details>


### mlm: Machine Learning Model Extension

The mlm-extension provides fields to describe ML models, their training details and inference runtime requirements. This extension is mostly combined with other extensions. 

**Examples:**
- mlm:name -> name of the model
- mlm:tasks -> tasks for which the model can be used for
- mlm:input -> transformation between EO data and model input
- [More examples](https://github.com/stac-extensions/mlm?tab=readme-ov-file#item-properties-and-collection-fields)

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


## Conclusion
- Advantages:
    - Improves providing, developing and using in the field of spatiotemporal data
    - Enables increased accessibility and interoperability
    - Many examples and use cases are already covered by extensions
    - The core is simple and the concept is flexible and 
- Difficulties/Discussion:
    - Much work to make all data STAC compliant -> how to get the community bigger, how far can it grow with voluntary work and the OS base?
    - Spatiotemporal data is only one special type of data -> how to expand to more disciplines? Is it even compatible?
    - Limited by available libraries and tools -> how to generalize or automatize to get faster steps forward more availabilities?


STAC is an enrichment to make spatiotemporal data interoperable, searchable and queryable. It enables better access to data and is constantly growing. The open source background and the simplicity make the use of the standards accessible to all and thus ensures that providers, developers and users can make use of the possibilities and develop them further. 


## Sources
- stacspec
    - https://stacspec.org/en/
    - https://stacspec.org/en/about/
    - https://stacspec.org/en/about/stac-spec/
    - https://stacspec.org/en/tutorials/intro-to-stac/
- GitHub
    - https://stac-extensions.github.io/
    - https://github.com/radiantearth/stac-spec/
    - https://github.com/radiantearth/stac-api-spec/
    - https://github.com/radiantearth/stac-spec/tree/master/extensions
    - https://github.com/stac-extensions/eo
    - https://github.com/stac-extensions/eo/blob/main/examples/item.json
    - https://github.com/radiantearth/stac-spec/blob/master/overview.md
    - https://github.com/radiantearth/stac-spec/tree/v0.8.1/extensions/eo
    - https://github.com/stac-extensions/mlm
    - https://github.com/stac-extensions/mlm/blob/main/examples/item_eo_bands.json
- Others
    - https://gogeomatics.ca/spatiotemporal-asset-catalogs-enabling-online-search-and-discovery-of-geospatial-assets/
    - https://learn.microsoft.com/de-de/azure/orbital/organize-stac-data
    - https://developers.satellogic.com/archive-service/introduction.html
    - https://www.earthdata.nasa.gov/esdis/esco/standards-and-practices/stac

[^1]: https://stacspec.org/en/
[^2]: https://github.com/radiantearth/stac-spec/
[^3]: https://www.collinsdictionary.com/de/worterbuch/englisch/catalogue




