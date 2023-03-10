import zipfile


def extract_zip(base_location, target_location):
    zip_ref = zipfile.ZipFile(base_location,'r')
    zip_ref.extractall(target_location)
    zip_ref.close()
