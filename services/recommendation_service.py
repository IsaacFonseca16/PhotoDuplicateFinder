def calculate_file_score(file):
    score = 0

    if file.width and file.height:
        score += (file.width * file.height) / 1000

    if file.size:
        score += file.size * 10

    extension = file.name.lower().split(".")[-1]

    if extension in ["jpg", "jpeg", "png"]:
        score += 100

    if "copia" not in file.name.lower() and "copy" not in file.name.lower():
        score += 50

    return score


def get_recommended_file(files):
    if not files:
        return None

    return max(files, key=calculate_file_score)
