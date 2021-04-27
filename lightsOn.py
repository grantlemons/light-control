from LightControl import *

load_dotenv()
token = os.getenv('TOKEN')
device_name = os.getenv('DEVICE_NAME')
loop = asyncio.get_event_loop()
lights_object = Light()

loop.run_until_complete( lightsOn(lights_object, device_name) )