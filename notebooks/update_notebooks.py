import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


def update_notebook(notebook_path, notebook_name, python_files):
    try:
        # Load the existing notebook
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        # Clear existing cells
        nb.cells = []

        # Add level one header with notebook filename
        nb.cells.append(new_markdown_cell(f"# {notebook_name}"))

        # Prepare new cells
        for py_file in python_files:
            header = new_markdown_cell(f"## {py_file}")
            code_block = new_code_cell("")
            nb.cells.extend([header, code_block])

        # Save the modified notebook
        with open(notebook_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
    except FileNotFoundError:
        print(f"Notebook not found: {notebook_path}")
    except Exception as e:
        print(f"Error processing {notebook_path}: {e}")


def main():
    source_root = "/Users/vamsi_mbmax/Library/CloudStorage/OneDrive-Personal/01_vam_PROJECTS/LEARNING/proj_ML/books_proj_ML/python_ml_bundle_7books/time_series_forecasting_with_python/code"
    destination_folder = "/Users/vamsi_mbmax/Library/CloudStorage/OneDrive-Personal/01_vam_PROJECTS/LEARNING/proj_ML/dev_proj_ML/pract-jb-timeseries/notebooks"

    # Process all notebooks in destination folder
    for notebook_file in os.listdir(destination_folder):
        if notebook_file.endswith(".ipynb"):
            notebook_path = os.path.join(destination_folder, notebook_file)
            notebook_name = notebook_file.replace(".ipynb", "")
            chapter_name = notebook_file.replace("practise_", "").replace(".ipynb", "")
            source_folder = os.path.join(source_root, chapter_name)

            if os.path.exists(source_folder):
                python_files = [
                    f[:-3] for f in os.listdir(source_folder) if f.endswith(".py")
                ]
                try:
                    update_notebook(notebook_path, notebook_name, python_files)
                except Exception as e:
                    print(f"Error updating {notebook_file}: {e}")
            else:
                print(f"Source folder not found for {chapter_name}, skipping...")


if __name__ == "__main__":
    main()
