from fastapi import FastAPI
import models, database
from routers import blog, user, authentication
app = FastAPI()
models.Base.metadata.create_all(database.engine)
get_db = database.get_db 
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)




