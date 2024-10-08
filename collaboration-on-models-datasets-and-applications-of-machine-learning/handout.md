# Collaboration on models, datasets and applications of machine learning
[@LeaHem77](https://github.com/LeaHem77)

## Table of contents
[1. Introduction](#1.-Introduction)

[2. Collaboration on models and datasets - Federated learning](#2-collaboration-on-models-and-datasets---federated-learning)

[2.1 Why federated learning](#21-why-federated-learning)

[2.2 How federated learning wors](#22-how-federated-learning-works)

[3. Exchange and reuse of trained models - example transfer learning](#3-exchange-and-reuse-of-trained-models-or-parts-of-models---example-transfer-learning)

[3.1 Why transfer learning is useful](#31-why-transfer-learning-is-useful)

[3.2 How transfer learning works](#32-how-transfer-learning-works)

[4. Hugging Face](#4-hugging-face)

[4.1 What is Hugging Face](#41-what-is-hugging-face)

[4.2 Transformers library](#42-transformers-library)

[4.3 Hugging Face Hub](#43-hugging-face-hub)

[5. Other platforms](#5-other-platforms-for-exchange-of-models-data-sets-and-applications)

[6. Sources](#6-sources)


## 1. Introduction
Machine learning (ML) describes the process of using artificial intelligence to create models/algorithms for specific types of tasks. After training with training data, a model can be used for a new problem with new input data (e.g. classification or prediction). For example, through supervised classification, the model is built with training data. Expert knowledge is necessary for correct classification; the procedure is very laborious and time-consuming. To collaborate on models and datasets, federated learning can be used to split training data between multiple users. It allows for model training across decentralized data sources without sharing the data itself. An approach to benefit from existing ML models is transfer learning. Transfer learning means that the code for models is passed on to other work groups and, with the help of minor changes, a similar problem can be solved with the same model. This approach saves resources. An example of a platform where machine learning models and datasets can be uploaded, developed further and exchanged, is Hugging Face.


## 2. Collaboration on models and datasets - Federated learning
### 2.1 Why federated learning
Collaborative machine learning is often used when companies do not have enough own data to ensure a desired accuracy for a ML model. It can also be used when sensitive user data needs to remain private. A company can jointly develop a model with others, the confidentiality of their data is not compromised in this process.
A collaborative approach for ML is federated learning, where  sensitive user data is kept private.
Federated learning is motivated by data privacy, data minimization and data access rights.

Disadvantages:
- transferring the model to and from the server for each user involves large amounts of data to be moved: high communication costs
- data heterogeneity: users/entities gather their own data, not standardized
    - no guarantee that user data is gathered independently or identically distributed

### 2.2 How federated learning works
With federeated learning, a ML algorithm is trained on multiple local datasets contained in local nodes without explicitly exchanging data samples. In principle, local models are trained on local data samples and parameters (e.g. the weights and biases of a deep neural network) are exchanged between models. A generel model is created in this process, which is shared by all nodes.

Neural networks, loosely based on the human brain, are machine-learning models that learn to solve problems using interconnected layers of nodes, or neurons.

## 3. Exchange and reuse of (trained) models or parts of models - Example transfer learning
### 3.1 Why transfer learning is useful
Designing a machine learning model is often a resource- and time-consuming approach. A large data set is required to train the model. In some cases, however, the required data is either not freely accessible or available. In addition, not every development team has the opportunity to create their own training data. In such cases, access to pre-trained models can help shorten the training process. This is where transfer learning is interesting. The model can be trained for the new situation with a small amount of data. This is particularly useful when a lot of expert knowledge is required (e.g. in natural language processing). Training time is minimized as it eliminates the need to spend days or weeks building a neural network.

Advantages of transfer learning:
- reduced training time: models are partially trained and can be quickly adapted
- improved neural network performance: pre-trained models often perform better, even with smaller datasets
- no large amounts of data required: transfer learning can work effectively with smaller datasets for new tasks

Transfer learning improves the efficiency of building a neural network and reduces the resources required. Knowledge and characteristics of a model can be transferred between networks.

### 3.2 How transfer learning works
The main idea behind transfer learning is to improve learning in a new task by leveraging knowledge from a related task. While there are different strategies for transfer learning, a common approach involves modifying a pre-trained model to suit the new task:

1. Select a pre-trained model: Choose a model that was trained on a similar problem, with knowledge relevant to the new task.
2. Adapt the model:
    - freeze or fine-tune layers: Early layers that capture general features can be reused, while later task-specific layers can either be modified or retrained.
    - add new layers: If the new task differs significantly, new layers can be introduced to handle the task-specific requirements.
3. Train on new data: The adapted model is then trained on the new dataset, which is typically much smaller than what would be needed for training from scratch.

Transfer learning works best when the features learned in the original task can be applied to the new task. However, if the tasks are too different, the effectiveness of transfer learning may decrease.
Generally speaking: In deep learning, transfer learning only works if the model characteristics gained in the first task are general. Otherwise, the concepts cannot be transferred to another problem, rendering the model useless.


## 4. Hugging Face
### 4.1 What is Hugging Face
Hugging Face is a company whose platform enables users to build and provide tools and resources for the AI ​community. It started with a focus on Natural Language Processing (NLP), but it has expanded significantly into other domains and now supports a broader range of machine learning applications.
It is the company behind Transformers, the leading open source library for developing cutting-edge machine learning models. The code behind the models can be viewed and used, in contrast to closed source software. The repository is constantly growing.

Features:
- develops tools for building machine learning applications
- Transformers library: Transformers is a deep learning architecture that uses the self-attention mechanism (to capture dependencies and relations within input sequences) and gives different weights to the importance of each piece of input data. It is mainly used in the fields of natural language processing and computer vision.
- platform: allows users to share machine learning models and datasets
- Models Hub: Trained machine learning models for various task areas that are up to date. Development and usage are possible, complete with documentation and examples.
- Datasets Hub: Variety of data sets that can be used to train and test models.
Hugging-Face is free, but also offers a paid corporate option with customer support.

### 4.2 Transformers-library
Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models based on the transformers architecture.
Transformers support framework interoperability between PyTorch, TensorFlow, and JAX. This provides the flexibility to use a different framework at each stage of a model’s life; train a model in three lines of code in one framework, and load it for inference in another. Models can also be exported to a format like ONNX and TorchScript for deployment in production environments.

### 4.3 Hugging-Face-Hub
The Hugging-Face-Hub is a Platform for hosting Git-based code repositories, models (including version control), datasets and web applications (e.g. small demos of machine learning applications). A variety of trained models can support users in various areas, including:
- Natural Language Processing: text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice and text generation.
- Computer vision: image classification, object detection and segmentation.
- Audio: automatic speech recognition and audio classification.
- Image: Text-to-image and image-to-image generators.


## 5. Other platforms for exchange of models, data sets and applications
- OpenML: open platform for sharing datasets, algorithms, and experiments
- TensorFlow: create ML models that can run in any environment
- PyTorch: deep learning framework built to be flexible and modular for research, with the stability and support needed for production deployment
- scikit-learn (ML in Python): provides simple and efficient tools for predictive data analysis
- XGBoost: implements machine learning algorithms under the Gradient Boosting framework
- Keras: API for ML-powered apps, scale to larger GPU clusters
- MLflow: models and generative AI apps on a unified, end-to-end,
open source MLOps platform


## 6. Sources
#### Collaboration on models and datasets
- https://news.mit.edu/2022/collaborative-machine-learning-privacy-0907 (8.10.2024)
- https://www.adnovum.com/services/digital-innovation/incubator/collaborative-machine-learning (8.10.2024)
- https://en.wikipedia.org/wiki/Federated_learning (8.10.2024)
#### Transfer Learning
- https://medium.com/@akankshabali5/transfer-learning-cd8648ca8bcc (29.9.2024)
- https://aws.amazon.com/de/what-is/transfer-learning/ (29.9.2024)
- https://en.wikipedia.org/wiki/Layer_(deep_learning) (29.9.2024)
#### Hugging face
- https://huggingface.co/ (30.9.2024)
- https://huggingface.co/docs/transformers/index (6.10.2024)
- https://medium.com/@yuvrajkakkar1/-hugging-face-revolutionizing-ai-collaboration-in-the-machine-learning-community-28d9c6e94ddb (3.10.2024)
- https://azure.microsoft.com/de-de/solutions/hugging-face-on-azure (3.10.2024)
- https://www.youtube.com/watch?v=jBFFUwL0TyY (3.10.2024)
- https://de.wikipedia.org/wiki/Hugging_Face (3.10.2024)
#### Other examples
- https://www.openml.org (4.10.2024)
- https://www.tensorflow.org (4.10.2024)
- https://pytorch.org/ (4.10.2024)
- https://scikit-learn.org/stable/(4.10.2024) 
- https://xgboost.readthedocs.io/en/stable/ (4.10.2024)
- https://keras.io/ (4.10.2024)
- https://mlflow.org/ (4.10.2024)