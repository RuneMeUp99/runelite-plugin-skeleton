
import os
import shutil
import subprocess

# Configuration
PLUGIN_REPO = "https://github.com/SyntaxSkater/runelite-plugin-skeleton.git"
RUNE_DIR = os.path.join("runelite-client", "src", "main", "java", "net", "runelite", "client", "plugins")
PLUGIN_NAME = "skeletonplugin"
TEMP_DIR = ".skeletonplugin_temp"

def clone_or_update_repo():
    if os.path.exists(TEMP_DIR):
        print("Updating local skeleton plugin repository...")
        subprocess.run(["git", "-C", TEMP_DIR, "pull"], check=True)
    else:
        print("Cloning skeleton plugin from GitHub...")
        subprocess.run(["git", "clone", PLUGIN_REPO, TEMP_DIR], check=True)

def copy_plugin_to_rune_dir():
    target_dir = os.path.join(RUNE_DIR, PLUGIN_NAME)

    if os.path.exists(target_dir):
        response = input("Skeleton plugin already exists in RuneLite. Overwrite? (y/n): ").lower()
        if response != "y":
            print("Operation canceled.")
            return

        print("Overwriting existing plugin...")
        shutil.rmtree(target_dir)

    print(f"Copying skeleton plugin to {RUNE_DIR}...")
    shutil.copytree(
        TEMP_DIR, target_dir, 
        ignore=shutil.ignore_patterns(".git", ".gitignore", "README.md", "LICENSE")
    )

    print("Skeleton plugin added successfully!")

def main():
    # Ensure we're in the RuneLite project directory
    if not os.path.exists(RUNE_DIR):
        print("Error: This script must be run from the RuneLite project root directory.")
        return

    try:
        clone_or_update_repo()
        copy_plugin_to_rune_dir()
    except subprocess.CalledProcessError as e:
        print(f"Error running a git command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
