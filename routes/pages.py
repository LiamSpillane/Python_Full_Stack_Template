from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(default_response_class=HTMLResponse, include_in_schema=False)
templates = Jinja2Templates("./templates")


@router.get("/")
async def root(request: Request):
    context = {}
    return templates.TemplateResponse(request, "index.html", context)


# @router.post("/swap-docs")
# async def swap_docs(request: Request):
#     response = dict(await request.form())
#     if response["swap"] == "on":
#         documentation, link = "Swagger UI", "docs"
#     else:
#         documentation, link = "ReDoc", "redoc"
#     context = {"documentation": documentation, "link": link}
#     return templates.TemplateResponse(request, "docs-button.html", context)
