from fastapi import FastAPI
from blogs.routes import router as blogsapp
from youtube.routes import router as youtubeapp

app = FastAPI()

app.include_router(blogsapp, prefix='/api/blogs')
app.include_router(youtubeapp, prefix='/api/youtube')