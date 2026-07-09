import cv2


def get_video_metadata(file_path):
    video = cv2.VideoCapture(str(file_path))

    if not video.isOpened():
        return None, None, None

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    duration = None
    if fps and fps > 0:
        duration = frame_count / fps

    video.release()

    return width, height, duration, fps