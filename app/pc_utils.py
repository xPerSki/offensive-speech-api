import psutil as ps
from psutil import POWER_TIME_UNLIMITED
import asyncio

DEFAULT_INTERVAL: float = 5


async def get_cpu_usage(interval: float = DEFAULT_INTERVAL, verbose=False):
    while True:
        cpu_usage: float = get_cpu_usage_once()
        print(f"CPU usage: {cpu_usage:.2f}%") if verbose else None
        await asyncio.sleep(interval)
        return cpu_usage


async def check_cpu_threshold(treshold: float, verbose=False):
    while True:
        cpu_usage = await get_cpu_usage(verbose=verbose)
        if cpu_usage > treshold:
            print(f"Warning: CPU usage exceeded {treshold}%! Current usage: {cpu_usage}%")


async def cpu_watcher(treshold=20, verbose=False):
    cores: int = get_cores_info()
    # print(f"Current CPU cores: {cores}")
    await asyncio.gather(check_cpu_threshold(treshold, verbose))


def convert_units(value: float, to_type: str = "GB") -> float:
    to_type = to_type.upper()
    match to_type:
        case "BITS":
            return value
        case "B":
            return value / 1024
        case "MB":
            return value / pow(1024, 2)
        case "GB":
            return value / pow(1024, 3)
        case "TB":
            return value / pow(1024, 4)
        case _:
            return -1


def get_cores_info() -> int:
    return ps.cpu_count()


def get_cpu_usage_once() -> float:
    cpu_usage: list[float] = ps.cpu_percent(interval=None, percpu=True)
    return sum(cpu_usage) / len(cpu_usage)


def get_main_disk_info(disk_path: str, units: str = "GB") -> None:
    main_disk = ps.disk_usage(disk_path)
    total = convert_units(main_disk[0], units)
    free = convert_units(main_disk[2], units)
    percent = main_disk[3]
    print(f"Disk space: {free:.2f}/{total:.2f} {units}, {percent:.1f}% used")


def get_battery_info():
    b = ps.sensors_battery()
    charging = "Charging" if b.power_plugged else "Not Charging"

    if b.secsleft == POWER_TIME_UNLIMITED:
        print(f"Battery: {b.percent}%, Time left: INF, battery is {charging}")
    else:
        mm, ss = divmod(b.secsleft, 60)
        hh, mm = divmod(mm, 60)
        print(f"Battery: {b.percent}%, Time left: {hh}h {mm}min {ss}s, battery is {charging}")


if __name__ == "__main__":
    get_main_disk_info("/", "GB")
    get_battery_info()
    asyncio.run(cpu_watcher(treshold=60, verbose=True))
