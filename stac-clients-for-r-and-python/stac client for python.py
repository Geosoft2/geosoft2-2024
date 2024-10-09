## Grundlagen 

import json # Zur Anzeige der Abfrageergebnisse
import pystac 
import requests # Für Interaktion mit APIs

from pystac import Catalog, get_stac_version # Erweiterung von pystac zum Einbinden von bestehenden Catalogs
from pystac_client import Client # Erweiterung von pystac u.a. zum suchen in STACs



## Einbinden eines STACs

root_catalog = Catalog.from_file('https://raw.githubusercontent.com/stac-utils/pystac/main/docs/example-catalog/catalog.json')
root_catalog.describe() # Aufbau des Catalogs



## Informationen über den Catalog

# Informationen über den Stac Clienten
print(f"ID: {root_catalog.id}")
print(f"Title: {root_catalog.title or 'N/A'}")
print(f"Description: {root_catalog.description or 'N/A'}")



## Informationen über die vorhandenen Collections

collections = list(root_catalog.get_collections()) # get_collections() und weitere Func. im Handout erläutert
print(f"Number of collections: {len(collections)}") # Anzahl der vorhandenen Collections
print("Collections IDs:")
for collection in collections:
    print(f"- {collection.id}")



## Informationen über die vorhandenen Items 

items = list(root_catalog.get_all_items())
print(f"Number of items: {len(items)}")
for item in items:
    print(f"- {item.id}")



## Abfragen von einzelnen STAC Objekten

item = root_catalog.get_item("LC80140332018166LGN00", recursive=True) # Einzelenes Item, weitere Benutzung im Folgenden

# collection = root_catalog.get_collection("ID", recursive=BOOL)
# weitere möglich



## Abfragen von Metadaten

print(item.geometry)
print(item.bbox)
print(item.datetime)
print(item.collection_id)
item.get_collection() # Abfrage, zu welcher Collection das item gehört



## Erweiterte Metadaten abfragen (Common Metadata)

print(item.common_metadata.instruments)
print(item.common_metadata.platform)
print(item.common_metadata.gsd) 



## Abfrage von Assets

for asset_key in item.assets: #.assets als Func zur Abfrage aller Assets eines Items
    asset = item.assets[asset_key]
    print('{}: {} ({})'.format(asset_key, asset.href, asset.media_type)) # asset-key,(..) werden in den String {},(..) eingesetzt



## Informationen über ein Asset

asset = item.assets['B3']
print(asset.to_dict()) # Ähnlich zur Abfrage mit .format



## Speichern von Daten aus einem STAC

for asset_key in item.assets:
    asset = item.assets[asset_key]
    asset_url = asset.href
    file_name = asset_key + '.' + asset.media_type.split('/')[-1]
    
    # Fragt die Daten von der API ab
    response = requests.get(asset_url) # Nutzung der requests-Library
    
    # Speichere die Datei
    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    print(f'{file_name} heruntergeladen.')








### Weitere Optionen mit der Client-Extension von pystac



## STAC einbinden

catalog_url = 'https://planetarycomputer.microsoft.com/api/stac/v1'
client = Client.open(catalog_url) # Client interagiert mit API-Endpunkt (URL)



## Suche nach Items (Beispiel Sentinel-2)

search = client.search(
    collections=['sentinel-2-l2a'], 
    bbox=[-47.02148, -17.35063, -42.53906, -12.98314],
    datetime='2023-01-01/2023-01-31',
    limit = 10
)



## Ein Item aus den Ergebnissen abrufen

items = list(search.items())
print(len(items))
print(items)
item = items[5]
print(f"Item ID: {item.id}")
print(f"Item datetime: {item.datetime}")



## Informationen der Items aus den Ergebnissen abrufen

for asset_key, asset in item.assets.items():
    print(f"Asset Key: {asset_key}")
    print(f"Asset URL: {asset.href}")
    print(f"Asset Media Type: {asset.media_type}")
