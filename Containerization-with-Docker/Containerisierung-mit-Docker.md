# Containerisierung mit Docker
Autoren: [@Lukas Ahlert](https://github.com/LukasAhl) und [@Maximilian Reiner](https://github.com/ReinerMx)

## 1. Einleitung 
- **Verständnis von Containerisierung (Theorie)**: Was, warum, wann?
- **Praxis**: Docker zur Containerisierung nutzen.

## 2. Was ist Containerisierung? 

- **Definition**: 
  - Containerisierung ist eine leichte Form der Virtualisierung, bei der eine Anwendung und ihre Abhängigkeiten in einen Container gepackt werden.
  - Diese Container können konsistent in verschiedenen Umgebungen laufen.
  
- **Wesentliche Merkmale**:
  - **Isolierte Umgebung**: Jeder Container läuft in einer isolierten Umgebung mit eigenem Dateisystem, Prozessen und Netzwerk-Stack.
  - **Leichtgewichtig**: Container teilen sich den Kernel des Host-Betriebssystems, was sie effizienter als virtuelle Maschinen (VMs) macht.

- **Analogie**: 
  - Vergleiche die Containerisierung mit "Schiffscontainern" in der Logistik – standardisierte, portable Einheiten, die überall hin transportiert werden können, unabhängig davon, was sich darin befindet.

---

## 3. Warum ist Containerisierung wichtig? 

- **Konsistenz zwischen Umgebungen**: 
  - Container stellen sicher, dass dieselbe Anwendung in Entwicklungs-, Test- und Produktionsumgebungen ohne das Problem "Es funktioniert auf meinem Rechner" läuft.

- **Vorteile**:
  - **Portabilität**: Container können auf mehreren Plattformen (z. B. lokal, Cloud) betrieben werden.
  - **Skalierbarkeit**: Containerisierte Anwendungen können einfach über Cluster skaliert werden.
  - **Effizienz**: Effizienter als VMs, da Container sich den Betriebssystem-Kernel teilen.
  - **Geschwindigkeit**: Schnellere Start- und Herunterfahrzeiten im Vergleich zu VMs.

- **Echte Anwendungen**:
  - Von Unternehmen in Bereichen wie Microservices-Architekturen, cloud-nativen Anwendungen und CI/CD-Pipelines übernommen.

---

## 4. Wann sollte man Containerisierung einsetzen? 

- **Anwendungsfälle**:
  - **Microservices**: Aufteilen von Anwendungen in kleinere Dienste, die unabhängig bereitgestellt und skaliert werden können.
  - **CI/CD-Pipelines**: Container ermöglichen es CI/CD-Pipelines, nahtlos in verschiedenen Phasen zu funktionieren.
  - **Entwicklungsumgebungen**: Containerisierte Entwicklungsumgebungen verringern die Reibung zwischen Entwicklung und Produktion.

- **Wann man Containerisierung NICHT verwenden sollte**:
  - Anwendungen, die eine sehr enge Hardware-Kopplung benötigen oder nicht-containerisierte Abhängigkeiten erfordern.

---

## 5. Einführung in Docker 

- **Was ist Docker?**:
  - Docker ist eine Open-Source-Plattform, die die Bereitstellung, Skalierung und Verwaltung von Anwendungen in Containern automatisiert.
  
- **Docker-Komponenten**:
  - **Docker Engine**: Kernkomponente zum Ausführen von Containern.
  - **Docker Hub**: Ein Register für Docker-Images.
  - **Docker Compose**: Tool zum Definieren und Ausführen von Multi-Container-Anwendungen.

- **Wie Docker die Entwicklung verändert hat**:
  - Vereinfachte die Erstellung und Verwaltung von Containern.
  - Bietet einen Standard für Containerisierung.

- **Wichtige Begriffe**:
  - Dockerfile: <br>
    - Textdatei mit Anweisungen zur Erstellung des Docker-Images <br>
    - “Rezept” für den Container
  - Image: <br>
     - “Blaupause” eines Containers, der aus Dockerfile gebaut wird <br>
     - Enthält alle notwendigen Dateien und Abhängigkeiten (Betriebssystem, Programmbibliotheken, Anwendungscode, etc.) <br>
     - Grundlage für weitere Containerstarts
  - Volumes: Persistente Speicherung von Daten unabhängig von Containern
 
---

## 6. Wie containerisiert man eine Anwendung mit Docker? 

### Schritte zur Containerisierung einer einfachen Anwendung:

1. **Schritt 1**: Docker installieren  
   - Stelle sicher, dass Docker auf deinem Rechner installiert ist.

2. **Schritt 2**: Erstellen einer `Dockerfile`  
   - Eine `Dockerfile` ist eine Textdatei, die Anweisungen für den Bau des Docker-Images enthält.
   - Beispiel für eine Node.js-Anwendung:
     ```dockerfile
     # Schritt 1: Basis-Image
     FROM node:14

     # Schritt 2: Arbeitsverzeichnis festlegen
     WORKDIR /usr/src/app

     # Schritt 3: Anwendungscode kopieren
     COPY . .

     # Schritt 4: Abhängigkeiten installieren
     RUN npm install

     # Schritt 5: Anwendung starten
     CMD ["node", "app.js"]

     # Schritt 6: Port freigeben
     EXPOSE 3000
     ```

3. **Schritt 3**: Docker-Image bauen  
   - Befehl: `docker build -t my-app .`

4. **Schritt 4**: Container starten  
   - Befehl: `docker run -p 3000:3000 my-app`

5. **Schritt 5**: Volumes einbinden, um Daten persistent zu speichern (optiional)  
   - Beispiel-Befehl für eine MongoDB: `docker run -v /mein/host/pfad:/data/db --name mongo-container mongo`

6. **Schritt 6**: In Docker Hub hochladen (optional)
   - Befehl: `docker push benutzername/app-name`

---
sollte noch vorgeschoben werden und zu Containerisierung verallgemeinert
## 7. Wann sollte man Docker NICHT verwenden? 
- **Komplexe monolithische Anwendungen**:
  - Wenn die Anwendung auf einem stark spezifischen Setup basiert, das von Containerisierung nicht profitiert.

- **Ressourcenintensive Anwendungen**:
  - Hochleistungsanwendungen, die eine strikte Kontrolle über CPU und Arbeitsspeicher erfordern, könnten durch den Overhead der Containerisierung nicht profitieren.

- **Altsysteme**:
  - Ältere Systeme, die schwer zu migrieren sind, eignen sich möglicherweise nicht für Container.

---

## 8. Zusammenfassung & Fazit 

- **Wichtige Erkenntnisse**:
  - Containerisierung macht Anwendungen portabel, skalierbar und effizient.
  - Docker vereinfacht die Erstellung und Verwaltung von Containern.
  - Nutze Docker, wenn du skalierbare und portable Anwendungen baust, aber beachte auch die Grenzen.

- **Abschließende Bemerkung**: 
  - Containerisierung ist ein entscheidender Teil der modernen Softwareentwicklung und -bereitstellung, und Docker hat sich als das Standard-Tool dafür etabliert.


---
Wir müssen uns auch noch fragen ausdenken, die wir diskutieren können, falls es aus der Gruppe keine Fragen gibt
## 9. Quellen

- [Docker-Dokumentation](https://docs.docker.com/)
- [Kubernetes und Container-Orchestrierung](https://kubernetes.io/)
