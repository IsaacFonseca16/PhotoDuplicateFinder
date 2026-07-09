def find_similar_images(files, max_difference=5):
    images = [file for file in files if file.file_type == "Imagen" and file.phash is not None]

    similar_groups = []
    used = set()

    for i in range(len(images)):
        if i in used:
            continue

        group = [images[i]]

        for j in range(i + 1, len(images)):
            if j in used:
                continue

            difference = images[i].phash - images[j].phash

            if difference <= max_difference:
                group.append(images[j])
                used.add(j)

        if len(group) > 1:
            similar_groups.append(group)
            used.add(i)

    return similar_groups