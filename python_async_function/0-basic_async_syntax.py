#!/usr/bin/env python3
"""
Coroutin that takes in an integer argument
(max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutin which take argument and
    return delay awaiting to launch this function
    """
    duration: float = random.uniform(0, max_delay)
    await asyncio.sleep(duration)
    return duration
