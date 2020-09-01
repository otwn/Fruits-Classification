from typing import Optional, List
from fastapi import FastAPI, Query, Request, HTTPException, File, UploadFile
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from uuid import uuid4

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

classes = ['Fresh Apple', 'Fresh Banana', 'Fresh Orange', 'Rotten Apple', 'Rotten Banana', 'Rotten Orange']

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def index():
    return templates.TemplateResponse("index.html")


@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    return {"filename": file.filename}
    # for upload in request.files.getlist("file"):
    #     print(upload)
    #     print("{} is the file name".format(upload.filename))
    #     filename = upload.filename
    #     destination = "/".join([target, filenames])
    #     print("Accept incoming file:", filename)
    #     print("Save it to:", destination)
    #     upload.save(destination)
    #     # import tensorflow as tf
    #     import numpy as np
    #     from keras.preprocessing import image
    #     from keras.models import load_model
    #     new_model = load_model('model.h5')
    #     new_model.summary()
    #     test_image = image.load_img('images\\'+filename, target_size=(64,64))
    #     test_image = image.img_to_array(test_image)
    #     test_image = np.expand_dims(test_image, axis=0)
    #     result = new_model.predict(test_image)
    #     result1 = result[0]
    #     for i in range(6):
    #         if result1[i] == 1.:
    #             break
    #         prediction = classes[i]
    # return templates.TemplateResponse("template.html", image_name=filename, text=prediction)


@app.get('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


# subapi = FastAPI(openapi_prefix="/api/v1")

# @subapi.get("/")
# def read_root():
#     return {"Welcome to FastAPI. See documents at /api/v1/docs or /api/v1/redoc"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
