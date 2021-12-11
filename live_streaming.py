import subprocess


def live_stream(input, ip_address):
    subprocess.call(['ffmpeg', '-i', str(input), '-v', '0', '-vcodec', 'mpeg4', '-f', 'mpegts', 'udp://', str(ip_address), ':', '44100'])


# We initialize the input video and the IP address
video = 'BBB.mp4'
IP = '192.168.56.1'

# We call the method to start the live-streaming
live_stream(input=video, ip_address=IP)