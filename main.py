from fastapi import FastAPI, Depends
from routers import TestRouter
from middlewares import add_process_time_header, test_mw
from fastapi.middleware.cors import CORSMiddleware

# intiailize app
app = FastAPI(root_path="/api")

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# FastAPI.add_middleware() is intherited from Starlette which accepts it's own middleware classes.
# You need to use app.middleware("http")(add_process_time_header) or just use decorator form
app.middleware('http')(add_process_time_header)

# routers with middleware
app.include_router(TestRouter, dependencies=[Depends(test_mw)])