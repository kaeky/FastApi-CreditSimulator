from fastapi import Depends, HTTPException, Request, status


async def currentUser(request: Request):
    if not hasattr(request.state, "user") or not request.state.user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authenticated user found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return request.state.user