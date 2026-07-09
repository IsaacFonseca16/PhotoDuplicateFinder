from send2trash import send2trash


def move_files_to_trash(files):
    deleted = []

    for file in files:
        send2trash(file.path)
        deleted.append(file)

    return deleted
