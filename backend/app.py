from fastapi.responses import FileResponse

from model_pipeline.generator.generate_meme import generate_meme
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()

project_root = os.path.abspath(os.path.dirname(__file__))

# Move one level up
parent_dir = os.path.abspath(os.path.join(project_root, os.pardir))

IMAGE_DIR =  os.path.join(parent_dir, "generated_images")




class MemeRequest(BaseModel):
    user_input: str


@app.get("/")
@app.get("/home")
def read_root():
    image_name = "default2.jpg"

    file_path = os.path.join(IMAGE_DIR, image_name)
    print(file_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Image non trouvée")



@app.get("/generated_images/{image_name}")
def get_image(image_name: str):
    file_path = os.path.join(IMAGE_DIR, image_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Image non trouvée")

@app.post("/generate_meme")
def generate_meme_endpoint(meme_request: MemeRequest):
    try:
        print(meme_request)
        user_input = meme_request.user_input
        meme = generate_meme(user_input=user_input)
        return meme
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to generate meme")







    



            