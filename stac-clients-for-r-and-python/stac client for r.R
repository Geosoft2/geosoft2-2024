# Installieren der benötigten Pakete:
install.packages("rstac")
install.packages("sf")
install.packages("terra")
install.packages("tibble")
library(terra)
library(sf)
library(tibble)
library(rstac)

# Angeben einer URL zu einer Stac API
stac_url <- "https://planetarycomputer.microsoft.com/api/stac/v1"

# Aufbau der Verbindung zur API
s_obj <- stac(stac_url)
str(s_obj)

# Informationen über die stac API:
get_request(s_obj)
# alternativ:
s_obj %>% get_request()

# Anforderungen und Spezifikationen:
conformance_classes <- s_obj %>% conformance() %>% get_request()
conformance_classes

# Abfrage des Collections-Endpoint, nicht des top-level Endpoints
collections_query <- s_obj %>% collections()
# Liste aller verfügbaren Collections, also der verfügbaren datasets
collections_query %>% get_request()

# Suchanfrage an den Catalog stellen:
stac_search(
    q = s_obj,
    collections = "usgs-lcmap-conus-v13",
    datetime = "2021-01-01/2021-12-31",
    limit = 10
) %>% get_request()

# Beispiel zur Suche nach bestimmter Region (Ashe Couty, North Carolina)
ashe <- read_sf(system.file("shape/nc.shp", package = "sf"))[1, ]
plot(st_geometry(ashe))

ashe_bbox <- ashe %>% st_transform(4326) %>% st_bbox()
ashe_bbox

stac_query <- stac_search(
                    q = s_obj,
                    collections = "usgs-lcmap-conus-v13",
                    bbox = ashe_bbox,
                    datetime = "2021-01-01/2021-12-31",
                    limit = 10
) %>% get_request()
stac_query

signed_stac_query <- items_sign(
  stac_query,
  sign_planetary_computer() # Authentifizierung beim Planetary Computer
)
signed_stac_query

# Download des Datasets (lcpri: primary land coverage)
output_directory <- "C:/Users/lraeu/OneDrive/Desktop/Geosoftware II/geosoft2-2024/data"
assets_download(signed_stac_query, "lcpri", output_dir = output_directory, overwrite = TRUE)
output_file <- file.path("C:/Users/lraeu/OneDrive/Desktop/Geosoftware II/geosoft2-2024/data/lcmap/CU/V13/025011/2021/LCMAP_CU_025011_2021_20220721_V13_CCDC/LCMAP_CU_025011_2021_20220629_V13_LCPRI.tif") %>% rast()
plot(output_file)
rast("C:/Users/lraeu/OneDrive/Desktop/Geosoftware II/geosoft2-2024/data/B1.tiff")

ashe %>% st_transform(st_crs(output_file)) %>% st_geometry() %>% plot(add = TRUE, lwd = 3)



