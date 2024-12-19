def check_and_save(response, image_template, image_number, extension, filepath):
    response.raise_for_status()
    filename = image_template.format(image_number, extension)
    image_path = os.path.join(filepath, filename)
    with open(image_path, 'wb') as file:
        file.write(response.content)


def define_extension(url):
    unquoted_url = urllib.parse.unquote(url)
    path = urllib.parse.urlsplit(unquoted_url).path
    extension = str(splitext(path)[1])
    return extension