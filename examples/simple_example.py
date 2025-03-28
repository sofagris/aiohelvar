from aiohelvar.parser.address import HelvarAddress
import asyncio
from aiohelvar.router import Router
import logging


async def main():
    """
    A simple test script.

    """

    # Replace with your router's IP address
    router_ip_address = "10.47.14.20"
    router_helvarnet_port = 50000

    # Replace with the cluster ID and router ID of your router
    # If you don't know them, you can leave them as None and they will be derived from the IP address
    cluster_id = None
    router_id = None

    # Replace with the address of the device you want to flash
    device_address_to_flash = HelvarAddress(14, 20, 1, 1)

    # We will assume the cluster ID and router ID are the same as the IP address
    if cluster_id is None:
        cluster_id = router_ip_address.split(".")[2]
    if router_id is None:
        router_id = router_ip_address.split(".")[3]

    # set up some verbose logging.
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger().addHandler(console)

    # Connect to router. Router object will keep the connection alive.
    print(f"Connecting to router at address: {router_ip_address}...")
    router = Router(router_ip_address, router_helvarnet_port, cluster_id, router_id)
    await router.connect()

    print(f"Connected to router on workgroup: {router.workgroup_name}.")

    print("Initializing router...")
    await router.initialize()

    # Read out all devices
    print("Router devices: ")
    for key, value in router.devices.devices.items():
        print(f"    {value}")
        # print(f"        Device {key} states are: {value._get_states()}")

    print("Router groups: ")
    # Read out all groups
    for key, value in router.groups.groups.items():
        print(f"    {value}")

    # Read out all scenes
    print("Router scenes: ")
    for key, value in router.scenes.scenes.items():
        print(f"    {value}")

    device_to_flash = list(router.devices.devices.values())[0]

    # flash a load on for 10s
    await router.devices.set_device_load_level(device_to_flash.address, 95.2, 100)
    await asyncio.sleep(10)
    await router.devices.set_device_load_level(device_to_flash.address, 0.0, 100)

    # flash a load on for 10s
    await router.devices.set_device_load_level(device_address_to_flash, 95.2, 100)
    await asyncio.sleep(10)
    await router.devices.set_device_load_level(device_address_to_flash, 0.0, 100)

    await router.disconnect()


asyncio.run(main())
