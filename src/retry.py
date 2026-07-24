"""Retry wrapper with exponential backoff + jitter."""
import random
import time


def with_retry(fn, attempts=3, base_delay=0.5):
    last_exc = None
    for i in range(attempts):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            time.sleep(base_delay * (2 ** i) + random.uniform(0, 0.25))
    raise last_exc


# TODO: generalize for gas-notes
