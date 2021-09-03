# Introduction
This is a single page application (SPA) where users can upload an image and extract the text contained in that image.

<img width="670" alt="1 0_landing_page" src="https://user-images.githubusercontent.com/2443514/132050954-a82b8187-ff8c-4205-bac8-dd39b55c9695.png">


**Learning Outcomes:**
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

## References
* This project is based on a [tutorial for building SPA with Flask and Vue.js](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/), which is a awesome resource to get started with Vue.js and Flask

* This tutorial shows you how to [upload files with Vue.js](https://masteringjs.io/tutorials/vue/file-upload)

* This resource is for [displaying images in Vue.js](https://stackoverflow.com/questions/45071661/how-can-i-display-image-by-image-uploaded-on-the-vue-component)

* This resource is great to learn [how to install Tesseract-OCR on Linux](https://linuxhint.com/install-tesseract-ocr-linux/)

# Build Workflow

1. Create new component with `<name>.vue`
2. Update client/src/router/index.js to map `/<name>` to the <name> component

# Using Commands
All commands are grouped by the root directory in which they are executed.

## /client/
### Add a Vue Plugin
Use command `vue add <name>`

### Build the app
Use command `npm run build`

### Run App
use command `npm run serve` inside the **\src\client**

### Run Production App in Preview Mode
Use command `server -s dist`
