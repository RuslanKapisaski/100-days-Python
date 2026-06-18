import os
import shutil

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}


def organize_downloads():

    for filename in os.listdir(DOWNLOADS_FOLDER):

        file_path = os.path.join(
            DOWNLOADS_FOLDER,
            filename
        )

        if not os.path.isfile(file_path):
            continue

        moved = False

        for folder, extensions in FILE_TYPES.items():

            if filename.lower().endswith(
                    tuple(extensions)
            ):

                destination = os.path.join(
                    DOWNLOADS_FOLDER,
                    folder
                )

                os.makedirs(
                    destination,
                    exist_ok=True
                )

                shutil.move(
                    file_path,
                    os.path.join(
                        destination,
                        filename
                    )
                )

                moved = True
                break

        if not moved:

            destination = os.path.join(
                DOWNLOADS_FOLDER,
                "Others"
            )

            os.makedirs(
                destination,
                exist_ok=True
            )

            shutil.move(
                file_path,
                os.path.join(
                    destination,
                    filename
                )
            )