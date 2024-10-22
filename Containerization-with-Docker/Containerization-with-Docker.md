# Containerization with Docker
Authors: [@Lukas Ahlert](https://github.com/LukasAhl) and [@Maximilian Reiner](https://github.com/ReinerMx)


## 1. What is Containerization? 

- **Definition**: 
  - Containerization is a lightweight form of virtualization that involves packaging an application and its dependencies into a container.
  - These containers can run consistently across different computing environments.
  
- **Key Characteristics**:
  - **Isolated Environment**: Each container runs in its isolated environment with its own filesystem, processes, and network stack.
  - **Lightweight**: Containers share the host machine’s OS kernel, making them more efficient compared to virtual machines (VMs).

- **Analogy**: 
  - Compare containerization to "shipping containers" in the logistics industry—standardized, portable units that can be transported anywhere, irrespective of what’s inside.

---

## 2. Why is Containerization Important? 

- **Consistency Across Environments**: 
  - Containers ensure that the same application works in development, testing, and production environments without the "works on my machine" issue.

- **Benefits**:
  - **Portability**: Run containers across multiple platforms (e.g., local machine, cloud).
  - **Scalability**: Easily scale containerized applications across clusters.
  - **Efficiency**: More efficient than VMs because containers share the OS kernel.
  - **Speed**: Faster startup and shutdown times compared to VMs.

- **Real-World Usage**:
  - Adopted by companies for microservices architecture, cloud-native applications, CI/CD pipelines, and more.

---

## 3. When to Use Containerization? 

- **Use Cases**:
  - **Microservices**: Split applications into smaller services that can be independently deployed and scaled.
  - **CI/CD Pipelines**: Containers allow continuous integration/continuous deployment (CI/CD) pipelines to work seamlessly across different stages.
  - **Development Environments**: Containerized development environments reduce the friction between development and production.

- **When NOT to Use Containers**:
  - Applications that need very tight hardware coupling or require non-containerized dependencies.
  - **Complex monolithic applications**: When specific hardware or environment configurations are necessary.
  - **Resource-intensive applications**: Applications that require strict control over CPU and RAM may be negatively affected by containerization.
  - **Legacy systems**: Older systems that are difficult to migrate into containers
---

## 4. Introduction to Docker 

- **What is Docker?**:
  - Docker is an open-source platform that automates the deployment, scaling, and management of applications inside containers.
  
- **Components of Docker**:
  - **Docker Engine**: Core component for running containers.
  - **Docker Hub**: A registry for Docker images.
  - **Docker Compose**: Tool for defining and running multi-container applications.

- **How Docker Changed the Game**:
  - Simplified container creation and management.
  - Provided a standard for containerization.

 - **Key terms**:
   - Dockerfile: <br>
    - A text file with instructions for creating the Docker image <br>
    - The "recipe" for the container
   - Image: <br>
     - A "blueprint" of a container, built from a Dockerfile <br>
     - Contains all necessary files and dependencies (operating system, libraries, code, etc.) <br>
     - Basis for further container starts
  - Volumes: Persistent storage of data independent of containers
---

## 5. How to Containerize an Application Using Docker 

### Steps to Containerize a Simple Application:

1. **Step 1**: Install Docker  
   - Ensure Docker is installed on your machine.

2. **Step 2**: Create a `Dockerfile`  
   - A `Dockerfile` is a text file that contains instructions for building the Docker image.
   - Example for a Node.js application:
     ```dockerfile
     # Step 1: Base Image
     FROM node:14

     # Step 2: Set Working Directory
     WORKDIR /usr/src/app

     # Step 3: Copy Application Code
     COPY . .

     # Step 4: Install Dependencies
     RUN npm install

     # Step 5: Start Application
     CMD ["node", "app.js"]

     # Step 6: Expose Port
     EXPOSE 3000
     ```

3. **Step 3**: Build Docker Image  
   - Command: `docker build -t my-app .`

4. **Step 4**: Run the Container  
   - Command: `docker run -p 3000:3000 my-app`

5. **Step 5**: Integrate Volumes to store data persistently  
   - Example Command for MongoDB: `docker run -v /mein/host/pfad:/data/db --name mongo-container mongo`

6. **Step 6**: Push to Docker Hub (Optional)
   - Command: `docker push username/my-app`


---

## 6. Summary & Conclusion 

- **Key Takeaways**:
  - Containerization allows applications to be portable, scalable, and efficient.
  - Docker simplifies the creation and management of containers.
  - Use Docker when building scalable, portable applications, but understand its limitations.

- **Closing Remark**: 
  - Containerization is a critical part of modern software development and operations, and Docker has become a de facto tool for this.

- **Q&A**: Open the floor for questions.

---

## 7. Additional Resources 

- [Docker Documentation](https://docs.docker.com/)
- [Docker-Logos](https://www.docker.com/company/newsroom/media-resources/)
- [Kubernetes und Container-Orchestrierung](https://kubernetes.io/)
- [RedHat](https://www.redhat.com/de/topics/cloud-native-apps/what-is-containerization)
- [OPC Router](https://www.opc-router.de/was-ist-docker/)
