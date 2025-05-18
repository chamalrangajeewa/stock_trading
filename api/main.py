import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .routers.transactions import router as transactions_router
from .routers.account import router as account_router
from .containers import ApplicationContainer

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

def create_app() -> FastAPI:
    container = ApplicationContainer()
    container.config.from_dict(
        {
            "version": "1.0.0",
            "db" : {"url": "sqlite:///./webapp.db"} 
        }
    )
   
    # container.wire(modules=[".routers.transactions"])

    app = FastAPI(
    openapi_tags=tags_metadata,
    title="ChimichangApp",
    description="description",
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    debug=True)

    app.container = container
    app.include_router(transactions_router)
    app.include_router(account_router)

    origins = [
    "http://localhost:3000",
    "http://172.25.80.1:3000"
    # Add more origins here
    ]

    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

    return app

app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)