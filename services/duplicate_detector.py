def find_duplicates(files):

    hashes = {}

    for file in files:

        sha = file.sha256

        if sha not in hashes:
            hashes[sha] = []

        hashes[sha].append(file)

    duplicates = {}

    for sha, group in hashes.items():

        if len(group) > 1:
            duplicates[sha] = group

    return duplicates