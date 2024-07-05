from fastapi import Request, Response


def test(request: Request, response: Response):
    response.status_code = 201
    response.set_cookie('new_cookie', 'iam a new cookie value')
    response.headers['Authorization'] = f'Bearer abcdefg'
    
    return {"message": "working"}