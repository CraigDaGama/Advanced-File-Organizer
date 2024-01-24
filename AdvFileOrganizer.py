import os
import shutil

def get_extension(file):
    _, extension = os.path.splitext(file)
    return extension[1:]

def organize_media(input_path, output_path):
    files = os.listdir(input_path)
    media_folder = os.path.join(output_path, 'media')

    for file in files:
        extension = get_extension(file)

        # Check if the file is an image or video
        image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp','svg']
        video_extensions = ['mp4', 'avi', 'mkv', 'mov']

        if extension.lower() in image_extensions:
            destination_dir = os.path.join(media_folder, 'images', extension)
        elif extension.lower() in video_extensions:
            destination_dir = os.path.join(media_folder, 'videos', extension)
        else:
            # Skip files with unsupported extensions
            continue

        if not os.path.isdir(destination_dir):
            os.makedirs(destination_dir)

        shutil.move(os.path.join(input_path, file), os.path.join(destination_dir, file))

if __name__ == "__main__":
    input_path = input("Enter the input path: ")
    output_path = input("Enter the output path: ")

    organize_media(input_path, output_path)
    print("Media organized successfully.")
