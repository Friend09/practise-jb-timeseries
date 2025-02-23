#!/usr/bin/env python3
import json
import glob
import os


def create_notebook_template(notebook_name):
    return {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": [f"# {notebook_name}"]},
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": ".venv",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.12.9"},
        },
        "nbformat": 4,
        "nbformat_minor": 2,
    }


def update_notebooks():
    # Find all .ipynb files in the current directory
    notebook_files = glob.glob("*.ipynb")

    for notebook_file in notebook_files:
        # Create template with the current notebook name
        template = create_notebook_template(notebook_file)

        # Write the template to the notebook file
        with open(notebook_file, "w", encoding="utf-8") as f:
            json.dump(template, f, indent=1)
        print(f"Updated {notebook_file}")


if __name__ == "__main__":
    update_notebooks()
