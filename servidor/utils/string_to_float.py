import contextlib
async def string_to_float(string):
    with contextlib.suppress():
        return float(string)