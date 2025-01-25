
import os
import shutil
import subprocess
import filecmp

# Configuration
PLUGIN_REPO = "https://github.com/SyntaxSkater/runelite-plugin-skeleton.git"
RUNE_DIR = os.path.join("runelite-client", "src", "main", "java", "net", "runelite", "client", "plugins")
SKELETON_NAME = "skeletonplugin"
TEMP_DIR = ".skeletonplugin_temp"

def clone_or_update_repo():
    if os.path.exists(TEMP_DIR):
        print("Updating local skeleton plugin repository...")
        subprocess.run(["git", "-C", TEMP_DIR, "pull"], check=True)
    else:
        print("Cloning skeleton plugin from GitHub...")
        subprocess.run(["git", "clone", PLUGIN_REPO, TEMP_DIR], check=True)

def ensure_skeleton_is_updated():
    skeleton_dir = os.path.join(RUNE_DIR, SKELETON_NAME)

    # Check if the skeleton plugin exists locally
    if os.path.exists(skeleton_dir):
        print("Checking if the local skeleton plugin is up-to-date...")
        if not filecmp.dircmp(skeleton_dir, TEMP_DIR).diff_files:
            print("The local skeleton plugin is up-to-date.")
        else:
            response = input("The local skeleton plugin differs from the repo. Update it? (y/n): ").lower()
            if response == "y":
                shutil.rmtree(skeleton_dir)
                shutil.copytree(
                    TEMP_DIR, skeleton_dir,
                    ignore=shutil.ignore_patterns(".git", ".gitignore", "README.md", "LICENSE")
                )
                print("Skeleton plugin updated successfully!")
    else:
        print("Local skeleton plugin does not exist. Creating it...")
        shutil.copytree(
            TEMP_DIR, skeleton_dir,
            ignore=shutil.ignore_patterns(".git", ".gitignore", "README.md", "LICENSE")
        )
        print("Skeleton plugin added successfully!")

def create_new_plugin():
    new_plugin_name = input("Enter the name for your new plugin: ").strip()
    target_dir = os.path.join(RUNE_DIR, new_plugin_name)

    if os.path.exists(target_dir):
        response = input(f"A plugin named '{new_plugin_name}' already exists. Overwrite it? (y/n): ").lower()
        if response != "y":
            print("Operation canceled.")
            return
        print(f"Overwriting existing plugin '{new_plugin_name}'...")
        shutil.rmtree(target_dir)

    shutil.copytree(
        os.path.join(RUNE_DIR, SKELETON_NAME), target_dir,
        ignore=shutil.ignore_patterns(".git", ".gitignore", "README.md", "LICENSE")
    )
    print(f"New plugin '{new_plugin_name}' created successfully!")

def main():
    # Ensure we're in the RuneLite project directory
    if not os.path.exists(RUNE_DIR):
        print("Error: This script must be run from the RuneLite project root directory.")
        return

    try:
        clone_or_update_repo()
        ensure_skeleton_is_updated()

        response = input("Would you like to create a new plugin? (y/n): ").lower()
        if response == "y":
            create_new_plugin()
    except subprocess.CalledProcessError as e:
        print(f"Error running a git command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
