from fastapi import APIRouter, Depends
from controllers import TestController
from middlewares import hello_mw

# initialize router
router = APIRouter(prefix="/test")

# add routers
router.get("/", dependencies=[Depends(hello_mw)])(TestController.test)