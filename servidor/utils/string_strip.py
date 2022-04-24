import contextlib
async def string_strip(string):
    with contextlib.suppress():
        string = string.strip()
        if string:
            return string
    
