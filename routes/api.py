from fastapi.routing import APIRouter

router = APIRouter(prefix="/api")


@router.get("/data")
async def get_data() -> dict[str, str]:
    data = {"hello": "world"}
    return data
