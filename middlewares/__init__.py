import time
from fastapi import Request, Response


# global middleware
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time}"
    
    print(f"X-Process-Time: {process_time}")
    return response


# router middleware
async def test_mw(request: Request, response: Response):
    print(f"this is test router")
    
    # modify response if needed
    
    

# single route middleware
def hello_mw (request: Request, response: Response):
    print(f"hello from: {request.url.path}")
    
    # modify response if needed
    