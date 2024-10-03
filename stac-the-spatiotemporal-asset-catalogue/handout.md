@Juliarotert

# **STAC: the spatiotemporal asset catalogue**

## 1. Introduction 

## 2. Overview
### What
### why
### how

## 3. STAC Extensions
- for adding specific metadata
### EO: Electro-Optical Extension
> https://github.com/stac-extensions/eo/blob/main/examples/item.json
```
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
```
- Examples: eo:cloud_cover, eo:center_wavelength, eo:solar_illumination
### MLM: Machine Learning Model Extension
> https://github.com/stac-extensions/mlm/blob/main/examples/item_eo_bands.json
```
"properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
```
- Examples: mlm:name, mlm:memory_size, mlm:input

## 4. Conclusion

## Sources


