import os
import aiofiles

async def save_file(id, file):
    filename = f"{id}.csv"
    file_path = os.path.join(os.getcwd(), "app", "assets", "files", filename)
    async with aiofiles.open(file_path, 'wb') as f:
        while True:
            chunk = await file.read(1024)
            if not chunk:
                break
            await f.write(chunk)

    return None
