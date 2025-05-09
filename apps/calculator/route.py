from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
@router.post('/')
async def run(data: ImageData):
    print("Received POST /calculate")

    #image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
    try:    
        image_data = base64.b64decode(data.image.split(",")[1])
    except Exception as e:    
        return {"message": "Failed to decode image", "error": str(e), "status": "error"}
    
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)

    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)

    data = []
    for response in responses:
        print('response in route: ', response)
        data.append(response)
    
    return {
        "message": "Image processed",
        "data": data,
        "status": "success",
    }