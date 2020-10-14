# NetworkCameraReader

This repo is used to read frames a Network camera. This repo is a solution to the problem that opencv's frame reading results in a queue, that will build up. 

## Installation

```
pip3 install -r requirements.txt
```
## Usage

From outside this folder, you can initialize and read a video stream as follows:
```python3
from NetworkCameraReader import VideoCapture

cap = VideoCapture('admin','admin888888','192.168.50.108')
frame = cap.read()
```
this will always give you the most updated frame. 