from dotenv import load_dotenv
import os
from multiprocessing import pool
import time


def test_function(instance: int):
    time.sleep(instance / 100)
    load_dotenv()
    key = os.environ.get("SUPER_SECRET_KEY_A")
    print(f"{instance}: Initial {key=}")

    newval: str = f"new_value_{instance}"
    os.environ["SUPER_SECRET_KEY_A"] = newval
    print(f"{instance}: {newval=}")
    time.sleep(2)

    key = os.environ.get("SUPER_SECRET_KEY_A")
    print(f"{instance}: Final {key=}")


if __name__ == "__main__":
    pool = pool.Pool(processes=4)
    pool.map(test_function, [1, 2, 3, 4])
