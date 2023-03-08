import asyncio
from time import perf_counter
from typing import Callable, List
import consumer
import producer
import resulthandler

NUM_WORKERS = 6
WORK_QUEUE_MAX_SIZE = 20
NUM_RESULT_HANDLERS = 5
RESULT_QUEUE_MAX_SIZE = 20


async def _controller(batch: List[dict], task_completed_callback: Callable, job_completed_callback: Callable) -> None:
    pass


def run_job(batch: List[dict], task_completed_callback: Callable, job_completed_callback: Callable) -> None:
    asyncio.run(_controller(batch, task_completed_callback, job_completed_callback))
