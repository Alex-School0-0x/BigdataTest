import kagglehub
import pandas as pd
import glob, os, shutil


# Download latest version
def extract_data(kaggle_data):
    source_dir = kagglehub.dataset_download(kaggle_data)
    print("Path to dataset files:", source_dir)
    return source_dir


def load_data(source_dir, destination_dir):
    # Making the destination directory if it doesn't exists
    os.makedirs(destination_dir, exist_ok=True)
    # Getting all the csv files from download 
    csv_files = glob.glob(os.path.join(source_dir, '*.csv'))

    # moving all csv files to the data folder
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_dir, file_name)
        shutil.move(file_path, destination_path)
        print(f"Moved {file_name} to {destination_dir}")

def Clear_cache(source_dir, kaggle_data):
    # Clearing the cache
    kaggle_dir = kaggle_data.replace('/', '\\')
    cache_index = source_dir.find(kaggle_dir)

    if cache_index != -1:
        # Extract the path
        cache_dir = source_dir[:cache_index + len(kaggle_dir)]

        # Check if the directory exists before attempting to delete
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)  # Deletes the entire kagglehub cache directory
            print(f"Cache cleared at: {cache_dir}")
        else:
            print("The specified cache directory does not exist.")
    else:
        print("No '.cache\\kagglehub' directory found in the path.")

if __name__ == "__main__":
    kaggle_data = "usgs/earthquake-database"
    destination_dir = r".\Data"
    source_dir = extract_data(kaggle_data)
    pass