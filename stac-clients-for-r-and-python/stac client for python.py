import json
import requests
import pystac

from pystac import Catalog, get_stac_version
from pystac_client import Client
from pystac.extensions.eo import EOExtension
from pystac.extensions.label import LabelExtension

# root_catalog = Catalog.from_file('https://raw.githubusercontent.com/stac-utils/pystac/main/docs/example-catalog/catalog.json')

# root_catalog.describe()

# # Informationen über den Stac Clienten
# print(f"ID: {root_catalog.id}")
# print(f"Title: {root_catalog.title or 'N/A'}")
# print(f"Description: {root_catalog.description or 'N/A'}")

# # Informationen über die vorhandenen Collections:
# collections = list(root_catalog.get_collections())
# print(f"Number of collections: {len(collections)}")
# print("Collections IDs:")
# for collection in collections:
#     print(f"- {collection.id}")
# # Items anzeigen:
# items = list(root_catalog.get_all_items())

# print(f"Number of items: {len(items)}")
# for item in items:
#     print(f"- {item.id}")

# # Einzelnes Item abfragen:
# item = root_catalog.get_item("LC80140332018166LGN00", recursive=True)
# # Abfragen von Metadaten:
# # Core item metadata
# print(item.geometry)
# print(item.bbox)
# print(item.datetime)
# print(item.collection_id)
# item.get_collection()
# # common metadata:
# print(item.common_metadata.instruments)
# print(item.common_metadata.platform)
# print(item.common_metadata.gsd) #Ground Sample Distance (Bodenauflösung)
# # STAC extensions (additional metadata not covered by the core STAC spec)

# # Access STAC items's assets:
# for asset_key in item.assets:
#     asset = item.assets[asset_key]
#     print('{}: {} ({})'.format(asset_key, asset.href, asset.media_type))

# # Informationen über ein Asset:
# asset = item.assets['B3']
# print(asset.to_dict())

# eo_asset_ext = EOExtension.ext(asset)
# bands = eo_asset_ext.bands
# print(bands)
# print(bands[0].to_dict())

# for asset_key in item.assets:
#     asset = item.assets[asset_key]
#     asset_url = asset.href
#     file_name = asset_key + '.' + asset.media_type.split('/')[-1]
    
#     # Lade das Asset herunter
#     response = requests.get(asset_url)
    
#     # Speichere die Datei
#     with open(file_name, 'wb') as f:
#         f.write(response.content)
    
#     print(f'{file_name} heruntergeladen.')

# STAC-API Client öffnen
catalog_url = 'https://planetarycomputer.microsoft.com/api/stac/v1'
client = Client.open(catalog_url)
# Suche nach Sentinel-2-Items mit der STAC API
search = client.search(
    collections=['sentinel-2-l2a'],
    bbox=[-47.02148, -17.35063, -42.53906, -12.98314],
    datetime='2023-01-01/2023-01-31',
    limit = 10
)

# Ein Item aus den Ergebnissen abrufen
items = list(search.items())
print(len(items))
print(items)
item = items[5]  # Nimm das erste gefundene Item

print(f"Item ID: {item.id}")
print(f"Item datetime: {item.datetime}")

# Durch die Assets des Items iterieren
for asset_key, asset in item.assets.items():
    print(f"Asset Key: {asset_key}")
    print(f"Asset URL: {asset.href}")
    print(f"Asset Media Type: {asset.media_type}")

    # Optional: Das Asset herunterladen (Beispiel)
    if asset.media_type == 'image/png':
        response = requests.get(asset.href)
        with open(f"{asset_key}.png", 'wb') as f:
            f.write(response.content)
        print(f"Asset {asset_key} wurde heruntergeladen.")
