# Introduction
Build an SPA that uploads an image and uses tesseract to display the text output of that image.

**Learning by doing:**
1. First time using Vue.js or JavaScript in general.
2. Designing a product end-2-end.
3. Learn more about the front-end development and get a better understanding of that.

## References
This project is based of a tutorial for building SPA with Flask and Vue.js, specifically: https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/ 

For uploading files I used https://masteringjs.io/tutorials/vue/file-upload 

For displaying images: https://stackoverflow.com/questions/45071661/how-can-i-display-image-by-image-uploaded-on-the-vue-component 

Installing Tesseract-OCR on Linux: https://linuxhint.com/install-tesseract-ocr-linux/ 

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