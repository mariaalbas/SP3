import subprocess


# We download the video comparison.mp4 that shows both vp9 and h265 versions of the same video
def compare_two_videos(left, right):
    subprocess.call(['ffmpeg', '-i', str(left), '-i', str(right), '-filter_complex', 'hstack', 'comparison.webm'])


# We initialize both versions of the same video
vp9 = 'BBB_480_vp9.webm'
h265 = 'BBB_480_h265.mp4'

# We call the method
compare_two_videos(left=vp9, right=h265)

