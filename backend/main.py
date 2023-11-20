import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from typing import Union
import os
from bot import Bot
from openai import OpenAI


origins = [
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


TEMP_FOLDER = "temp"


@app.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    try:
        # create temp folder if it does not exist
        if not os.path.exists(TEMP_FOLDER):
            os.makedirs(TEMP_FOLDER)
        else:
            # remove all files in temp folder
            for filename in os.listdir(TEMP_FOLDER):
                file_path = os.path.join(TEMP_FOLDER, filename)
                os.remove(file_path)

        # process all the files
        saved_files = []
        for file in files:
            file_path = os.path.join(TEMP_FOLDER, file.filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            saved_files.append(file.filename)

        return {"uploaded": saved_files}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/generate")
async def generate(num_flash_cards: int = 5, optional_instructions: str = ""):
    try:
        bot = Bot(TEMP_FOLDER)
        bot.load()
        return bot.generate(
            num_flash_cards, optional_instructions=optional_instructions
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/tts")
async def tts(text: str):
    try:
        client = OpenAI()
        speech_file_path = "audio/speech.mp3"
        response = client.audio.speech.create(
            model="tts-1",
            voice="echo",
            input=text,
        )
        response.stream_to_file(speech_file_path)
        return FileResponse(speech_file_path, media_type="audio/mp3")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
