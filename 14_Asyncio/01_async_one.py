import asyncio
async def brew_chaai():
    print("Brwing chai...")
    await asyncio.sleep(2)
    print("Chai is ready")
    
    
asyncio.run(brew_chaai())
