import contextlib
async def string_to_int(string):
    with contextlib.suppress():
        return int(string)