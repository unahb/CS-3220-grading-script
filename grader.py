import sys
import os
import zipfile
import subprocess


def unzip_all_folders():
    for file in os.listdir():
        if file.endswith(".zip"):
            foldername = file.split(".zip")[0]
            with zipfile.ZipFile(file, "r") as zip_ref:
                zip_ref.extractall(foldername)
            os.system("rm -rf " + file)


def remove_all_makefile():
    for folder in os.listdir():
        if (
            os.path.isdir(folder)
            and not folder.startswith("temp")
            and not folder.startswith("images")
        ):
            os.system("rm " + folder + "/Makefile")


def copy_defaults_to_all_folders():
    for folder in os.listdir():
        if (
            os.path.isdir(folder)
            and not folder.startswith("temp")
            and not folder.startswith("images")
        ):
            os.system("cp -a ./temp/. " + folder)


def run_tests_store_results():
    with open("scores.csv", "a+") as f:
        for folder in os.listdir():
            # checks if the folder is a directory, starts with group, and does not already exist in the scores.csv
            if (
                os.path.isdir(folder)
                and not folder.startswith("group")
                and not folder.startswith("images")
                and (open("scores.csv", "r").read().find(folder) == -1)
            ):
                # os.system("cd " + folder)
                output = subprocess.Popen(
                    "cd {folder} && ./run_tests.sh exam".format(folder=folder),
                    shell=True,
                    stdout=subprocess.PIPE,
                )
                err = output.stdout.read().decode("utf-8")
                lines = err.split("\n")
                for i in range(0, len(lines)):
                    if lines[i].startswith("Number of passed tests:"):
                        # lines[i + 1] line with number of test cases passed
                        f.write(
                            "{folder}, {score}\n".format(
                                folder=folder, score=lines[i + 1]
                            )
                        )
                # os.system("cd ..")


if __name__ == "__main__":
    # unzip_all_folders()  # step 6
    # remove_all_makefile()  # step 7
    # copy_defaults_to_all_folders()  # step 8
    run_tests_store_results()  # step 9
