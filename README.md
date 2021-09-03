# Introduction
This is a single page application (SPA) where users can upload an image and extract the text contained in that image.

<img width="670" alt="1 0_landing_page" src="https://user-images.githubusercontent.com/2443514/132050954-a82b8187-ff8c-4205-bac8-dd39b55c9695.png">

# Prerequisites
The following software packages are required to build and run the application locally and in docker

* Docker Desktop +20.10.8
* `chocolatey` package manager (Windows only)
* npm
* Python +3.9
* Node JS
* make

# Build and Deploy with `make`
The below table provides more details about the `make targets` used to build, deploy, and run the application. 
In order to use them, run the `make <Make Target>` command in the project's root folder.

| Make Target | Description |
|-------------|-------------|
| `build-app` | Build the images |
| `build-app-no-cache` | Build the images without cache |
| `start-app` | Start the application (requires a build first) |
| `stop-app` | Stop the application |


# Learning Outcomes
The following is a reflection on the learning outcomes while building this project.

1. Use Vue.js and leverage Vue.js components.
2. Provide Python API for feature extraction of uploaded images.
3. Perform feature engineering on uploaded images using opencv.
4. Use Tesseract OCR to get text from images.
5. Serve the application with Nginx.
6. Proxy API calls from Nginx to Flask.
7. Deploy with Docker as single images.
8. Deploy using docker-compose.
9. Deploy using a manifest on local kubernetes cluster.
10. Deploy using a manifest on to Azure kubernetes cluster.

# References
* This project is based on a [tutorial for building SPA with Flask and Vue.js](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/), which is a awesome resource to get started with Vue.js and Flask

* This tutorial shows you how to [upload files with Vue.js](https://masteringjs.io/tutorials/vue/file-upload)

* This resource is for [displaying images in Vue.js](https://stackoverflow.com/questions/45071661/how-can-i-display-image-by-image-uploaded-on-the-vue-component)

* This resource is great to learn [how to install Tesseract-OCR on Linux](https://linuxhint.com/install-tesseract-ocr-linux/)

# Additional Information and Commands
This section contains some helpful commands. Some require `npm` to be installed on your system.

## Client Side Commands
Run the following commands inside the `client/` folder

## Add a Vue Plugin

    Use command `vue add <name>`

## Build the Frontend App

    Use command `npm run build`

## Run Fontend App

    use command `npm run serve` inside the **\src\client**

## Run Frontend App in Production Preview Mode

    Use command `server -s dist`
