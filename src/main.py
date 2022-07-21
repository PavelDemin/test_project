from fastapi import Depends, FastAPI, Query, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from core.config import config
from db.storage import database
from services.csv_service import get_csv_service
from services.image_service import ImageService, get_image_service

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

public = Jinja2Templates(directory="public")


@app.on_event('startup')
async def startup():
    await database.connect()

    csv_service = get_csv_service()
    await csv_service.delete_table()
    await csv_service.load_data_from_csv(config.csv_file_name)


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get("/", response_class=HTMLResponse)
async def request_image(request: Request,
                        category:  list[str] = Query(None),
                        image_service: ImageService = Depends(get_image_service)) -> Response:
    image_url = await image_service.get_image_by_category(category)

    return public.TemplateResponse("index.html", {"request": request, "image": image_url})
