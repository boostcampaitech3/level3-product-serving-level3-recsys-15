if __name__ == "__main__":
    import uvicorn

    uvicorn.run("book-music-app.main:app", host="0.0.0.0", port=30002, reload=True)
