#!/usr/bin/env python3
"""
Coroutin which take argument and
return delay awaiting to launch this function
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Coroutin which take argument and
    return delay awaiting to launch this function
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    duration: float = end - start
    average: float = duration / n
    return average
