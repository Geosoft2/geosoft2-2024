# Handout: Modell Formate im Deep Learning

Autoren: [nicevibesplus](https://github.com/nicevibesplus), [awiechma](https://github.com/awiechma)

## Unterschiede zwischen Machine Learning und Deep Learning

- **Datenmengen**:
  - **Machine Learning**: Funktioniert mit kleinen oder großen strukturierten Datenmengen.
  - **Deep Learning**: Arbeitet mit großen unstrukturierten Datenmengen.

- **Hardware und Laufzeit**:
  - **Machine Learning**: Geringere Laufzeit bei einfacher Hardware.
  - **Deep Learning**: Benötigt leistungsstarke Hardware und hat längere Rechenzeiten.

- **Menschlicher Einfluss**:
  - **Machine Learning**:
    - Braucht eine klare Problemdefinition
    - Merkmalsextraktion muss manuell erfolgen
    - Auswahl geeigneter Algorithmen
  - **Deep Learning**:
    - Benötigt Input des Menschen bei dem Aufbau der Netzarchitektur und Anpassung der Hyperparameter

- **Datenformate**:
  - Die gespeicherten Datenformate sind in beiden Fällen ähnlich.

## Komponenten eines Deep Learning Modells

- **Eingabedaten**: Daten, die ins Modell eingespeist werden.
- **Architektur**: Struktur des neuronalen Netzes.
  - Neuronen: Grundbausteine eines neuronalen Netzes.
  - Schichten: Anordnung der Neuronen im Netzwerk.
  - Aktivierungsfunktionen: Bestimmen, ob ein Neuron aktiviert wird.
- **Verlustfunktionen**: Messen, wie sehr der berechnete Wert vom tatsächlichen Wert abweicht.
- **Optimierungsalgorithmus**: Passt Gewichte und Bias an, um die Leistung des Modells zu verbessern.
- **Gewichte und Bias**: Parametrische Werte, die Eingaben gewichten und die Aktivierungsfunktion verschieben.
- **Hyperparameter**: Parametrische Werte, die zB. Anzahl der Schichten und Neuronen definieren.

## Speicherung von Deep Learning Modellen

- **Unterschiedliche Machine Learning Frameworks verwenden verschiedene Datenformate zur Speicherung.**
- **Ansätze**:
  - Einige speichern nur die Modellarchitektur und die gelernten Parameter.
  - Andere speichern zusätzlich die Trainingsdaten.
- **Relevanz der Trainingsdaten**: Für die Archivierung wichtig, beeinflusst die Nutzung jedoch nicht.

## Verbreitete Frameworks für Deep Learning

1. [**TensorFlow**](https://www.tensorflow.org/) – Google Brain
2. [**PyTorch**](https://pytorch.org/) – Linux Foundation
3. [**Keras**](https://github.com/keras-team/keras)
4. [**CNTK**](https://github.com/microsoft/CNTK) – Microsoft Cognitive Toolkit

## Datei Formate

### HDF5
- **[Legacy Format](https://computersciencewiki.org/index.php/Legacy_system)**
- **Verwendung**: In TensorFlow und Keras.
- **Funktion**: Speicherung von sehr großen Datenmengen.
- **Speichert**:
  - Trainingsdaten
  - Modellarchitektur
  - Gewichte/Bias
  - Informationen über den Zustand des Optimierungsalgorithmus (Checkpointing)
  - Trainingskonfiguration (Verlustfunktion)
  - Metadaten (z.B. Keras Version)

### TFRecord
- **Funktion**: Speichert Trainingsdaten
- **Effizienz**: Optimal für sehr große Datenmengen.
- **Verwendung**: Von TensorFlow.

### ONNX (Open Neural Network Exchange)
- **Funktion**: Austausch von DL-Modellen zwischen verschiedenen Frameworks.
- **Speichert**:
  - Modellarchitektur
  - Gewichte/Bias
  - Ein- und Ausgabeformate des Modells
  - Metadaten

### PKL (Pickle)
- **Funktion**: Speichert Python-Objekte.
- **Verwendung**: In PyTorch.
- **Speichert**:
  - Modellarchitektur
  - Gewichte/Bias
  - Alle Python-Objekte
- **Tool**: Serialisierung und Deserialisierung von Python-Objekten.

### PT (PyTorch Tensors)
- **Verwendung**: In PyTorch.
- **Effizienz**: Besonders effizient für PyTorch durch Speicherung als Tensor.
- **Speichert**:
  - Modellarchitektur
  - Gewichte/Bias
  

## Quellen
IBM Data and AI Team (2023, 6. Juli). *AI vs. machine learning vs. deep learning vs. neural networks. What’s the difference?*. IBM. https://www.ibm.com/think/topics/ai-vs-machine-learning-vs-deep-learning-vs-neural-networks.

Madhavan, S. & Jones, M. T. (2024, 24. April). *Deep learning architectures. The rise of artificial intelligence.* IBM Developer. https://developer.ibm.com/articles/cc-machine-learning-deep-learning-architectures.

Nyuytiymbiy, K. (2020, 30. Dezember). *Parameters and Hyperparameters in Machine Learning and Deep Learning.
What exactly are they and how do they interact?*. Towards Data Science. https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac
