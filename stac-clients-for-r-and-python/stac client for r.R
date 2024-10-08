install.packages("sf")
install.packages("terra")
install.packages("tibble")
library(terra)
library(sf)
library(tibble)
# Installieren des rstac Pakets
install.packages("rstac")
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

# Abfrage des Collections-Endpoint, nicht des top-level Endpoints
collections_query <- s_obj %>% collections()
collections_query
# Liste aller verfügbaren Collections, also der verfügbaren datasets
get_request(collections_query)

# Suchanfrage an den Catalog stellen:
stac_search(
    q = s_obj,
    collections = "usgs-lcmap-conus-v13",
    datetime = "2021-01-01/2021-12-31",
    limit = 999
) %>% get_request
# Mögliche Suchparameter: collections, bbox, datetime, ids, query (Suche nach spezifischen Eigenschaften), limit, sortby, intersects (Übergabe einer Geometrie, die geschnitten werden soll)

# Beispiel zur Suche nach bestimmter Region (Ashe Couty, North Carolina)
ashe <- read_sf(system.file("shape/nc.shp", package = "sf"))[1, ]
plot(st_geometry(ashe))
ashe_bbox <- ashe %>% st_transform(4326) %>% st_bbox()
ashe_bbox
stac_query <- stac_search(
                    q = s_obj,
                    collections = "sentinel-2-l2a",
                    bbox = ashe_bbox,
                    datetime = "2021-01-01/2021-12-31",
) %>% get_request
stac_query

signed_stac_query <- items_sign(
  stac_query,
  sign_planetary_computer() # Authentifizierung beim Planetary Computer
)
signed_stac_query

# Download des Datasets (lcpri: primary land coverage)
assets_download(signed_stac_query, c("lcpri", "lcsec"), output_dir = output_directory, overwrite = TRUE)
output_file <- file.path(
  output_directory,
  "lcmap",
  "CU",
  "V13",
  "025011",
  "2021",
  "LCMAP_CU_025011_2021_20220721_V13_CCDC",
  "LCMAP_CU_025011_2021_20220629_V13_LCPRI.tif"
) %>% rast()
plot(output_file)

plot(rast("C:/Users/lraeu/Desktop/Geosoftware II/geosoft2-2024/data/sentinel2-l2/17/S/MA/2021/01/01/S2A_MSIL2A_20210101T161701_N0212_R140_T17SMA_20210102T070054.SAFE/GRANULE/L2A_T17SMA_A028880_20210101T162158/IMG_DATA/R10m/T17SMA_20210101T161701_B04_10m.tif"))

ashe %>% st_transform(st_crs(output_file)) %>% st_geometry() %>% plot(add = TRUE, lwd = 3)

list.files(
  file.path(tempdir(), "lcmap"),
  recursive = TRUE,
  full.names = TRUE
) |> 
  terra::rast() |>
  terra::plot()
ashe %>% st_transform(st_crs(output_file)) %>% st_geometry() %>% plot(add = TRUE, lwd = 3)

conformance_classes <- s_obj %>% conformance() %>% get_request()
conformance_classes

queryables <- stac_source %>%
              queryables(collections = "sentinel-2-l2a") %>%
              get_request()
queryables
