
import os
import shutil
import subprocess

# Configuration
PLUGIN_REPO = "https://github.com/YOUR_USERNAME/runelite-plugin-skeleton.git"
RUNE_DIR = os.path.join("runelite-client", "src", "main", "java", "net", "runelite", "client", "plugins")
RESOURCE_DIR = os.path.join("runelite-client", "src", "main", "resources", "net", "runelite", "client", "plugins", "skeletonplugin")
PLUGIN_NAME = "skeletonplugin"
TEMP_DIR = ".skeletonplugin_temp"

def clone_or_update_repo():
    if os.path.exists(TEMP_DIR):
        print("Updating local skeleton plugin repository...")
        subprocess.run(["git", "-C", TEMP_DIR, "pull"], check=True)
    else:
        print("Cloning skeleton plugin from GitHub...")
        subprocess.run(["git", "clone", PLUGIN_REPO, TEMP_DIR], check=True)

def ensure_skeleton_is_updated():
    target_dir = os.path.join(RUNE_DIR, PLUGIN_NAME)
    resource_icon = os.path.join(RESOURCE_DIR, "skeleton_icon.png")

    # Ensure the RuneLite plugins directory exists
    if not os.path.exists(RUNE_DIR):
        os.makedirs(RUNE_DIR, exist_ok=True)

    # Ensure the resources directory exists
    if not os.path.exists(RESOURCE_DIR):
        os.makedirs(RESOURCE_DIR, exist_ok=True)

    # Overwrite or create the plugin package
    if os.path.exists(target_dir):
        print(f"Overwriting existing package at {target_dir}...")
        shutil.rmtree(target_dir)
    else:
        print(f"Creating new package at {target_dir}...")
    
    shutil.copytree(
        TEMP_DIR, target_dir, 
        ignore=shutil.ignore_patterns(".git", ".gitignore", "README.md", "LICENSE")
    )

    # Copy the icon to the resources directory
    temp_icon_path = os.path.join(TEMP_DIR, "skeleton_icon.png")
    if os.path.exists(temp_icon_path):
        shutil.copy(temp_icon_path, resource_icon)
        print(f"Icon copied to {resource_icon}")
    else:
        print("Warning: skeleton_icon.png not found in the repository!")

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
        os.path.join(RUNE_DIR, PLUGIN_NAME), target_dir,
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
