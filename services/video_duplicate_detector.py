def find_duplicate_videos(files):
    videos = [file for file in files if file.file_type == "Video"]

    hashes = {}

    for video in videos:
        sha = video.sha256

        if sha not in hashes:
            hashes[sha] = []

        hashes[sha].append(video)

    duplicates = {}

    for sha, group in hashes.items():
        if len(group) > 1:
            duplicates[sha] = group

    return duplicates