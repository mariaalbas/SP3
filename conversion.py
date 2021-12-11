import subprocess

def conversion():
    # Conversion to vp8
    def mp4_to_vp8(res_720, res_480, res_360x240, res_160x120):
        subprocess.call(['ffmpeg', '-i', str(res_720), '-c:v', 'libvpx', '-b:v', '1M', '-c:a', 'libvorbis', 'BBB_720_vp8.webm'])
        subprocess.call(['ffmpeg', '-i', str(res_480), '-c:v', 'libvpx', '-b:v', '1M', '-c:a', 'libvorbis', 'BBB_480_vp8.webm'])
        subprocess.call(['ffmpeg', '-i', str(res_360x240), '-c:v', 'libvpx', '-b:v', '1M', '-c:a', 'libvorbis', 'BBB_360x240_vp8.webm'])
        subprocess.call(['ffmpeg', '-i', str(res_160x120), '-c:v', 'libvpx', '-b:v', '1M', '-c:a', 'libvorbis', 'BBB_160x120_vp8.webm'])

    # Conversion to vp9
    def mp4_to_vp9(res_720, res_480, res_360x240, res_160x120):
        subprocess.call(['ffmpeg', '-i', str(res_720), '-c:v', 'libvpx-vp9', '-c:a', 'libopus', 'BBB_720_vp9.webm'])
        subprocess.call(['ffmpeg', '-i', str(res_480), '-c:v', 'libvpx-vp9', '-c:a', 'libopus', 'BBB_480_vp9.webm'])
        subprocess.call(['ffmpeg', '-i', str(res_360x240), '-c:v', 'libvpx-vp9', '-c:a', 'libopus', 'BBB_360x240_vp9.webm'])
        subprocess.call(['ffmpeg', '-i', str(res_160x120), '-c:v', 'libvpx-vp9', '-c:a', 'libopus', 'BBB_160x120_vp9.webm'])

    # Conversion to h265
    def mp4_to_h265(res_720, res_480, res_360x240, res_160x120):
        subprocess.call(['ffmpeg', '-i', str(res_720), '-c:v', 'libx265', '-c:a', 'copy', '-x265-params', 'crf=25', 'BBB_720_h265.mp4'])
        subprocess.call(['ffmpeg', '-i', str(res_480), '-c:v', 'libx265', '-c:a', 'copy', '-x265-params', 'crf=25', 'BBB_480_h265.mp4'])
        subprocess.call(['ffmpeg', '-i', str(res_360x240), '-c:v', 'libx265', '-c:a', 'copy', '-x265-params', 'crf=25', 'BBB_360x240_h265.mp4'])
        subprocess.call(['ffmpeg', '-i', str(res_160x120), '-c:v', 'libx265', '-c:a', 'copy', '-x265-params', 'crf=25', 'BBB_160x120_h265.mp4'])

    # Conversion to AV1
    def mp4_to_av1(res_720, res_480, res_360x240, res_160x120):
        subprocess.call(['ffmpeg', '-i', str(res_720), '-c:v', 'libaom-av1', '-crf', '30', '-b:v', '0', 'BBB_720_av1.mp4'])
        subprocess.call(['ffmpeg', '-i', str(res_480), '-c:v', 'libaom-av1', '-crf', '30', '-b:v', '0', 'BBB_480_av1.mp4'])
        subprocess.call(['ffmpeg', '-i', str(res_360x240), '-c:v', 'libaom-av1', '-crf', '30', '-b:v', '0', 'BBB_360x240_av1.mp4'])
        subprocess.call(['ffmpeg', '-i', str(res_160x120), '-c:v', 'libaom-av1', '-crf', '30', '-b:v', '0', 'BBB_160x120_av1.mp4'])

    res1 ='BBB_resized_720.mp4'
    res2 = 'BBB_resized_480.mp4'
    res3 = 'BBB_resized_360x240.mp4'
    res4 = 'BBB_resized_160x120.mp4'

    mp4_to_vp8(res1, res2, res3, res4)
    mp4_to_vp9(res1, res2, res3, res4)
    mp4_to_h265(res1, res2, res3, res4)
    mp4_to_av1(res1, res2, res3, res4)

conversion()