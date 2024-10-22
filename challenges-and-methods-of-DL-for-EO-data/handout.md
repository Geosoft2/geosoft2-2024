# Challenges, Approaches to Overcome them and Applications of Deep Learning in Earth Observation

author: [@MatteoWeickert](https://github.com/MatteoWeickert)

---

With the growing capabilities of remote sensing, UAVs and other Earth observation tools vast amounts of spatiotemporal data are being generated at an accelerating rate across various fields.
However, the unique characteristics of spatiotemporal data introduce new challenges for deep learning techniques. This document provides an overview of the specific difficulties associated with applying deep learning to spatial data, particularly in comparison to non-spatial data, along with methods for addressing these challenges and examples of deep learning applications in Earth observation. 

---

## Main Challenges when Applying DL to Spatial/EO Data (Compared to Non-Spatial Data)

### 1. Input Size and Complexity of Spatial Data
- **Continuous Space**: Spatial data can span large areas with high resolution, leading to inputs of thousands by thousands of pixels—far larger than the standard input sizes used in traditional DL models.
- **Complex Long-Range Spatial Dependencies**: Spatial observations are always (more or less) related. They often contain long-range dependencies that operate across multiple scales, which introduces computational challenges such as large memory requirements. Deep Learning models that are developed under the assumption of independence mitght therefore not work best for spatial patterns.

### 2. Heterogeneity and Integration of Diverse Data Types
- **Multiple Map Layers**: EO data involves multiple layers (e.g. satellite imagery, climate projections, sensor data) with different spatial resolutions, formats (vector, raster) and noise levels. That complicates the use of single / traditional DL models.
- **Geospatial Data Heterogeneity**: Differences in spatial resolution, file formats, projections and coordinate reference systems (CRS) hinders the integration and joint use of available geospatial data. Given a research problem for a specific geographic region, the geospatial data are typically collected by diverse providers with different emphases and purposes. This often leads to large variety of incompatible data characteristics. Therefore specific methods for statistical modeling and analysis are required. 
- **Spectral Diversity**: EO data often includes multispectral imagery (e.g., Landsat’s 11 bands or Sentinel-2’s 12 bands) that are not directly compatible with traditional RGB-based DL methods.

### 3. Lack of Ground Truth and Label Quality
- **Data Scarcity**: Acquiring labeled ground truth data for EO applications is often slow, costly, and labor-intensive due to the need for field surveys or visually interpretation of high-resolution images. 
- **Weak Labels**: Available labels are often sparse, coarse, or noisy, complicating the training of deep neural networks.

### 4. Interdisciplinarity and Physical Knowledge Integration
- **Incorporating Domain Knowledge**: Spatiotemporal problems in EO require integrating deep learning with physical models or expert knowledge to ensure a realistic result according to physics and improve generalizability to real-world scenarios. 
- **Non-Stationarity and Local Heterogeneity**: Spatial data exhibits non-stationary properties, meaning statistical patterns can vary significantly over space. This complicates the training of models that assume homogeneity.

### 5. Model Generalizability and Overfitting
- **Overfitting Risk**: DL models are prone to overfitting, especially when trained on spatial data with complex, heterogeneous patterns. This is because pure data-driven deep learning can easy learn spurious relationships that look good on the training data and validation but do not generalize well to reality.
- **Out-of-Distribution (OOD) Issues**: Models may perform poorly when exposed to unseen data from regions or conditions not covered in the training set. If a model detects an OOD case, it should also provide an uncertainty value at the end in addition to the prediction or use another method to process the data beforehand.

### 6. Uncertainty and Explainability
- **Black-Box Nature of DL Models**: Deep learning models are often difficult to interpret, which is a problem when transparency is needed to advance scientific understanding. Moreover it makes it difficult to explain why a model works and to determine when it fails. 
- **Uncertainty Quantification**: It is impossible to create a perfect representation of the infinitely complex real world. In addition to that EO data can be noisy, incomplete or distributed unevenly and ultimately are subject to uncertainty. Therefore it is necessary that models not only predict outcomes but also assess the uncertainty of these predictions. 

---

## Methods and Strategies to Tackle the Challenges

### 1. Learning Complex Spatial Dependencies
Convolutional Neural Networks (CNNs) are not sufficient for long-range dependencies. They are powerful at recognising local patterns like edges or textures but are limited when it comes to modelling long-range dependencies, e.g. relationships between distant points that is crucial for spatial data.
- **Attention Mechanisms**: Allow a model to focus on different parts of an image to different degrees by adjusting the influence of certain pixels across the entire image. Therefore it is possible to detect long-range dependencies. This is particularly useful for geospatial data, where patterns are often globally distributed.
- **Patch-Based Approaches**: To reduce computational costs it is possible to capture long-range geospatial dependencies at different scales. Models can learn dependencies within smaller patches of the data, reducing computational costs, and then aggregate the information from these patches and then a model captures the dependencies between the patches.

### 2. Handling Data Scarcity and Weak Labels
- **Weakly Supervised Learning**: Algorithms capable of learning from sparse, coarse, or noisy labels.
    - **Semi-Supervised Learning**: Combines a few high-quality labels with many weak labels, leveraging patterns in the well-labeled data to improve predictions in weakly labeled regions.
    - **Domain-Based Learning**: Additional knowledge / rules or physical models are used to fill gaps in the data, enhancing model performance in under-sampled areas.
    - **Noise Modeling**: Models can learn to recognize and correct for noisy labels by creating a noise model during training. In the case of sparse data availability With a noise model the deep learning model is able to detect erroneous labels and prevent minimise their influence on the model. Moreover it makes it possible to model the uncertainty in the data.
- **Generative Adversarial Networks (GANs)**: Exist of two neural networks that are trained against each other. The generator creates artifical data that are similar to the ground truth data while the discriminator tries to recognize whether the data is real or created by the generator. Through this competition, both networks improve: the generator gets better and better at creating realistic images, while the discriminator gets better and better at distinguishing between real and generated images. To improve data availability GANs can be used to generate realistic synthetic images or data that can be used to compensate for the lack of high quality ground truth data. For example, a GAN can be used to supplement missing or noisy data from satellite imagery.

### 3. Integration of Physical Knowledge
- **integration of symbolic knowledge**
    - **Neuro-Symbolic Models**: Combine neural networks with symbolic knowledge (e.g., rules, logic expressions or knowledge graphs) to guide predictions.
- **numeric physical models**
    - **Physics-Informed Neural Networks (PINNs)**: Combine neural networks with physical laws. This is done by integrating partial differential equations (PDEs) directly into the neural network training process, enhancing model accuracy and generalisability by ensuring that predictions are not only based on the training data but also follow physical laws. Problem is that PINNs are trained for one specific physical case because it considers one specific PDE, so for every new phenomenon the network has to be trained again.
    - **Neural Operator Learning**: Alternative to PINNs. Trains models on a family of partial differential equations to generalize better across different physical phenomena. Problem is that a big amount of simulations that are very time and cost intensive are required.

### 4. Improving Model Generalizability
- **Ensemble Models**: Train individual models on homogenous sub-regions and combine their outputs to improve performance across heterogeneous datasets.
- **Meta-Transfer Learning**: Uses knowledge from related tasks to improve learning on new tasks, allowing models to adapt quickly to new regions with minimal labeled data.
- **Out-of-Distribution Detection**: Models can identify when test cases deviate significantly from training data and treat them as an out-of-distribution (OOD) case. Then another model or a different method has to be used to work with the data.

### 5. Uncertainty Quantification
- **Monte Carlo Dropout (MC-Dropout)**: Randomly disables neurons during training which leads to slightly different results for each prediction and produces a range of predictions. This helps to avoid overfitting by forcing the network to learn more robust features. By analyzing the variance of these predictions, the uncertainty of predictions can be quantified. 
- **Bayesian Neural Networks (BNNs)**: In Bayesian networks, uncertainty is modelled directly in the weights of the model. Instead of fixed weights, the parameters are given probability distributions. This allows BNNs not only to make predictions, but also to give a probability of how certain these predictions and the weights are. This is particularly useful for avoiding overfitting.

---

## Examples of Deep Learning in EO Applications

### 1. Data Pre-Processing / Image Restoration
Images obtained through remote sensing techniques often are of poor quality due to atmospheric conditions. The quality of these images needs to be enhanced to extract useful information from these images.
- **Denoising**: Using CNNs and denoising auto-encoders to clean noisy EO data. Auto-encoders are a type of neural network that is based on unsupervised learning. It consists of two main parts: The encoder that compresses the input data into a lower-dimensional representation ("latent space") and the decoder that tries to reconstruct the original data from the compressed data. The goal is to learn a compact and efficient representation based on the essential features of the data while minimizing the reconstruction error between input and output.  
- **Deblurring**: Restoring original or a sharp image from the blurred image due to atmospheric turbulences in remote sensing. CNNs, auto-encoders and GANs help recover sharp images from the blurred data.
- **Pan Sharpening and super resolution**: Combining low-resolution multispectral and high-resolution panchromatic images to receive an increased resolution of satellite images using auto-encoders and CNNs.
- **Cloud Shadow Removal**: DL models identify and remove clouds and their shadows from EO images, improving data usability.

### 2. Geospatial Object Detection
The challenge of detecting or identifying an object of interest such as a building, an airplane or a tennis court from aerial images acquired through remote sensing is referred to as geospatial object detection.
- **Small Object Detection**: Identifying small objects (e.g., roads, buildings) in aerial images using CNN-based models trained with labeled geospatial images.

### 3. Land Cover and Land Use Classification
- **Pixel-Based and Object-Based**: DL models classify land cover types (e.g., water, forest, urban) and land use (e.g., agricultural vs. recreational) from satellite images. Moreover they can classify scenes, so high-level semantic entities like densely populated areas, rivers, airports, etc. It is also possible to classify smaller objects like fish species or crop types with deep learning.

### 4. Change Detection
- **Temporal Analysis**: Comparing satellite images of the same area from different times to detect changes in urban areas, forests, ice cover, etc.

### 5. Time Series Forecasting
- **Weather and Climate Predictions**: Recurrent Neural Models (RNN), especially LSTM (long short-term memory) networks model and predict spatiotemporal patterns in weather and climate data. One specific use case is making predictions about agricultural yields based on temporal satellite data. RNN models can take into account seasonal patterns and other time-dependent factors to produce accurate crop forecasts, which is very useful for the management of agricultural resources. 
- **Traffic Flow Monitoring**: RNNs are also used to model traffic flows, as these have temporal patterns. Graph Neural Networks (GNNs) can also be used to take into account the network structure of traffic routes. These models represent the roads and junctions (e.g. intersections) as graphs and capture the interactions within the traffic system.
---
### bibliography

Adam J. Stewart, Caleb Robinson, Isaac A. Corley, Anthony Ortiz, Juan M. Lavista Ferres, and Arindam Banerjee. 2022. TorchGeo: Deep Learning With Geospatial Data. In The 30th International Conference on Advances in Geographic Information Systems (SIGSPATIAL ’22), November 1–4, 2022, Seattle, WA, USA. ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/3557915.3560953

Cao, G. (2022). Deep learning of big geospatial data: Challenges and opportunities. In New Thinking in GIScience (S. 159 - 169). Higher Education Press.

Kiwelekar, A. W., Mahamunkar, G. S., Netak, L. D., & Nikam, V. B. (2020). Deep learning techniques for geospatial data analysis. In G. A. Tsihrintzis & L. C. Jain (Eds.), Machine learning paradigms: Learning and analytics in intelligent systems (Bd. 18, S. 63-81). Springer. https://doi.org/10.1007/978-3-030-49724-8_3

Jiang, Z. (2023). Deep learning for spatiotemporal big data: A vision on opportunities and challenges. Department of Computer & Information Science & Engineering, University of Florida, Gainesville, FL, USA.

IBM. (n.d.). Was ist ein Autoencoder? IBM. https://www.ibm.com/de-de/topics/autoencoder

Wikipedia. (n.d.). Generative adversarial networks. In Wikipedia, The Free Encyclopedia. https://de.wikipedia.org/wiki/Generative_Adversarial_Networks

Moseley, B. (n.d.). So what is a physics-informed neural network? Ben Moseley. https://benmoseley.blog/my-research/so-what-is-a-physics-informed-neural-network/