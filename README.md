# image-segmentation-example
A simple web app where you can apply image segmentation by just uploading the image. The model is based on the working of [Tensorflow Image Segmentation](https://www.tensorflow.org/tutorials/images/segmentation)

An example of the application is:

![Example](https://github.com/ocakhasan/image-segmentation-example/blob/master/screenshots/segmentation.PNG)

You need to run the notebook file and at the end to save the model you need to run
```python
model.save()
```
It will save the model. You can download the model weights from the files part in the colab. After that

* Clone the repo
* Create a folder named model
* Paste the files or folders you download into that folder.

After those steps, from the command line just write
```
set FLASK_APP=main.py (in Windows)
export FLASK_APP=main.py (in Unix or MacOS)
```

After that just run

```
flask run
```
It will open the application in the "http://127.0.0.1:5000/".
