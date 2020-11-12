# avsync
A tool for helping find audio/video offsets for synchronization.

This was built for use in synchronizing the audio and video in a livestreaming setup.


## Usage

Use a test video with visual cues and timings like the one mentioned here (not this actual YouTube video): https://www.youtube.com/watch?v=LXY69tuBfV4

Play the video (with audio) on your phone/laptop/whatever and record the audio and video of it through your livestreaming setup.

Process the recorded video with this tool:

    ./sync_frames.sh "RecordedTestVideo.mp4"

It will find the 10 highest audio amplitude "peaks" and output the image from the video from the time that each peak occurs in the video. You can then look at the resulting images to determine the correct audio/video offset to use.


## Dependencies

* python3
* pydub python module
* ffmpeg
