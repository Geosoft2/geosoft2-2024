## Data cubes for earth observation data
Authors: [@anienabe](https://github.com/anienabe), [fthieman](https://github.com/fthieman)
### What are Datacubes? 
A data cube is a multidimensional array of values, typically used to represent data in a structured format for analysis and querying. While the number of dimensions can vary, three dimensions are most common. This is because much of the data we encounter is two-dimensional, such as spreadsheets or images. When you stack hundreds or thousands of these two-dimensional datasets—like satellite images taken over different months—you create a three-dimensional structure, with time serving as the third dimension. This stacked format resembles a cube, hence the name "data cube." 

In a geographic context, the typical dimensions for width and length correspond to the x- and y-coordinates of latitude and longitude. Depending on the use case, the third dimension could be depth (e.g., when working with geologic or oceanographic data), altitude (e.g., when analyzing atmospheric data), or time, which is the leading third dimension in the context of earth observation.  
![data cubes](https://github.com/fthiemann/geosoft2-2024/blob/main/data_cubes.png)
Architecture of a data cube; Source: Kopp et al.

<br />

### Benefits 
#### Handling large amounts of data 
When observing the Earth, the amount of data collected and stored is enormous. The organized, array-based structure of a data cube facilitates access to the needed data.  

 
#### Efficiency  
Due to the organized structured by the grouped data, it is quick and easy for the user to find and retrieve data. 

Users can make different kinds of queries: 

- Request data from a specific location (e.g., a time series of observations from that area) 
- Request data from a specific time (e.g., an image from that date).
![selection data cubes](https://github.com/fthiemann/geosoft2-2024/blob/main/selection_data_cubes.png)


#### Complex analyses 
The multidimensional structure enables complex analyses, such as time series analysis and multidimensional querying. 


#### Scalability 
Data cubes are designed to handle large volumes of data, which is important in Earth observation where the datasets can reach petabytes in size. Their scalability ensures that they can accommodate growing datasets without sacrificing performance. 

 

#### Interoperability 
Data cubes can integrate data from various sources and sensors, harmonizing different formats and spatial resources. This is helpful for researchers who can then easily examine trends, patterns and relationships in the data over different dimensions, such as geographical location and time.   

 

#### Analysis Ready Data (ARD) 
Data once stored and processed correctly in a data cube, can directly be used for computation, e.g. for machine learning.  

 
<br />

### Challenges 
#### Large amount of data  
The biggest challenge when working with data cubes is the sheer volume of data, which can reach petabytes in size. For storing those amounts of data locally a certain infrastructure is necessary of which the costs can be prohibitively high. Currently, it is most effective to use public commercial clouds like Amazon AWS, Google Cloud, or Microsoft Azure to optimize data storage. Additionally, data compression techniques for images can help manage storage needs. 


#### Decisions 
Beyond storage solutions, decisions must be made regarding file formats (e.g., JPEG, GeoTIFF) and their respective advantages and disadvantages. It's also essential to plan how to process data within the data cube and consider its overall design for optimal performance. 

 
#### Preconditions 
Decisions regarding processing and design impact performance during computationally intensive tasks. Specific hardware and algorithms are often required to facilitate these computations effectively. 

 
#### Data Integration 
While a data cube with correctly stored data is practical, there are several challenges in data integration to become ‘analysis ready data’ (ARD): 

- The data must be geometrically correct and in the appropriate coordinate system. 
- Atmospheric corrections must be applied to eliminate distortions. 
- Cloud masking is necessary to remove clouds, ensuring a clear view of the surface. 
- Data from different sources must be standardized to ensure compatibility. 
- The time dimension must be accurately represented. 


#### Expertise needed 
Many users who want to work with data cubes may not possess the necessary technical skills or experience to effectively execute complex queries and data analyses. This can lead to inefficient use of the data and limit the organization's ability to analyze and make decisions based on the insights derived from the data. 

 

#### Legal and ethical challenges 
Legal and ethical challenges in data cubes and Earth observation primarily revolve around privacy concerns and data protection regulations. Organizations must handle the collected data responsibly, consider individuals' privacy, and avoid misuse. To ensure that data cubes follow the FAIR principles, ISO 19123-1/19123-3 were instated and updated. 

 
<br />

### Use Cases 
#### Water Resources Management 
Data cubes have been effectively used for managing water resources by tracking changes in water extent, monitoring wetlands, and assessing flood risks. 

 
#### Environmental Monitoring 
Via Environmental Monitoring it is possible to perform time series analyses for monitoring forest cover, coastline changes and urban expansion. This is interesting for e.g. governments who want to track illegal activities.  

 
#### Disaster Management 
By providing timely and easily accessible data, data cubes support disaster response efforts. For example, they have been used to track flood risks and assess the aftermath of extreme weather events. 

This is consequently also important for the government and their political decisions in a natural disaster. 


<br />

### Practical Examples 
#### Australian GeoScience Data Cube 
Developed by Geoscience Australia and hosted on the National Computational Infrastructure at the Australian National University, the Australian GeoScience Data Cube represents a significant advancement in Earth observation data management. This pixel-aligned collection comprises over 300,000 Landsat scenes from across Australia, all geometrically and spectrally calibrated to accurately reflect the Earth's surface. As the first continental Landsat data cube featuring overlapping temporal scenes, it paves the way for innovative analytical approaches.  

Australia uses data from the Data Cube for various purposes, such as scientific research, improving community safety, exploring mineral resources, navigation, and supporting the country's prosperity.  

The Australian Geoscience Data Cube laid the foundation for Digital Earth Australia (DEA). DEA is a newer initiative that provides a comprehensive platform, enabling users to access and analyze Earth observation data through user-friendly tools and services. This platform extends the utility of the data cube, offering insights for decision-making across sectors like environmental monitoring, agriculture, and disaster management.  

DEA provides free satellite imagery amounting to nearly 1.5 petabytes. The data is 'Analysis Ready Data' (ARD), making analyses as easy as possible for potential users. 

 
#### Digital Earth Africa 
Digital Earth Africa (DEA) is the largest project under NASA's Committee on Earth Observation Satellites (CEOS) initiative, utilizing the Open Data Cube technology to create a comprehensive data cube for the African continent. It includes datasets from Landsat and Sentinel-1, offering a rich collection of satellite imagery and web services. Through DEA, users can explore spectral indices over time and perform interactive change detection using spectral and radar data. A notable example is the detection of changes in the Volta River area in central Ghana. The data is easily accessible via the Africa GeoPortal. 


<br />

### Sources 
Achieving the Full Vision of Earth Observation Data Cubes; Kopp et al. 

https://www.mdpi.com/2306-5729/4/3/94 (Stand: 06.10.2024) 

 

OBSERVER: Data cubes: Enabling and facilitating Earth Observation applications 

https://www.copernicus.eu/en/news/news/observer-data-cubes-enabling-and-facilitating-earth-observation-applications (Stand: 05.10.2024) 

 

Earth observation data cubes for water resources management 

https://www.space4water.org/s4w/web/news/earth-observation-data-cubes-water-resources-management (Stand: 06.10.2024) 

 

Digital Earth Africa 

https://www.digitalearthafrica.org (Stand: 06.10.2024) 

 

ISO Norm 19123-1 

https://committee.iso.org/sites/tc211/home/projects/projects---complete-list/iso-19123-1.html (Stand: 08.10.2024) 

 

Australian GeoScience Data Cube 

https://www.ga.gov.au/scientific-topics/dea/about/open-data-cube (Stand: 04.10.2024) 

 

 

 


