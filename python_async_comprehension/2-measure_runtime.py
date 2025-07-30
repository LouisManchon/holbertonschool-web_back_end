#!/usr/bin/env python3
"""
Function measuring runtime
of coroutine and return duration
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Function measuring execution time
    of coroutine and return duration
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.perf_counter()
    return end - start
