from speed import SpeedManager
from twitter import TwitterManager

PROVIDER_DOWNLOAD_SPEED = "200"
PROVIDER_UPLOAD_SPEED = "100"

sp = SpeedManager()
speeds = sp.test_speed()
current_download_speed = speeds[0]
current_upload_speed = speeds[1]

message = (f"My download speed is {current_download_speed}Mbps "
           f"and my upload speed is {current_upload_speed}Mbps,"
           f"while it should be {PROVIDER_DOWNLOAD_SPEED}Mbps down "
           f"and {PROVIDER_UPLOAD_SPEED}Mbps up.")

if round(float(current_download_speed) / float(PROVIDER_DOWNLOAD_SPEED)) * 100 <= 50:
    tw = TwitterManager()
    tw.deploy()
    tw.send_message(message)
