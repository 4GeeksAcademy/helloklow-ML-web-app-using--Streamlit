# ML web app with Flask example: decision tree classifier diabetes prediction

Link to Render app: https://helloklow-ml-web-app-using-flask.onrender.com/

This repository contains the minimum requirements to get a web application up and working using the model trained in one of our prior projects. The model deployed will be the decision tree classifier based diabetes prediction. I have set-up much of the nit-picky configuration for you, but it is up to you to build the heart of the app and get it deployed to Render.

The project consists of four main parts:

1. **Model inference function**: This portion takes data from users and sends it to the model for prediction. It then sends back the prediction.
2. **Flask**: Flask is a simple web application framework, it will act as the go-between to bridge the html world of the user's web-browser and our internal python functions.
3. **Render**: render is the cloud hosting service we will use to actually run our application. This allows us to have a public URL where the application can be accessed.