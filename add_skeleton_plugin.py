
import os
import shutil
import subprocess
import re

# Configuration
PLUGIN_REPO = "https://github.com/SyntaxSkater/runelite-plugin-skeleton.git"
RUNE_DIR = os.path.join("runelite-client", "src", "main", "java", "net", "runelite", "client", "plugins")
RESOURCE_DIR_TEMPLATE = os.path.join("runelite-client", "src", "main", "resources", "net", "runelite", "client", "plugins")
TEMP_DIR = ".skeletonplugin_temp"
PLUGIN_NAME = "skeletonplugin"

VALID_PLUGIN_NAME_REGEX = r"^[a-zA-Z][a-zA-Z0-9_]*$"

def clone_or_update_repo():
    if os.path.exists(TEMP_DIR):
        print("Updating local skeleton plugin repository...")
        subprocess.run(["git", "-C", TEMP_DIR, "pull"], check=True)
    else:
        print("Cloning skeleton plugin from GitHub...")
        subprocess.run(["git", "clone", PLUGIN_REPO, TEMP_DIR], check=True)

def validate_plugin_name(plugin_name):
    if not re.match(VALID_PLUGIN_NAME_REGEX, plugin_name):
        print("Error: Plugin name must start with a letter and contain only letters, numbers, and underscores.")
        return False
    if plugin_name.lower() == PLUGIN_NAME.lower():
        print(f"Error: '{PLUGIN_NAME}' is a reserved name and cannot be used.")
        return False
    return True

def create_new_plugin():
    while True:
        new_plugin_name = input("Enter the name for your new plugin (e.g., MyNewPlugin): ").strip()
        if validate_plugin_name(new_plugin_name):
            break

    new_plugin_package = new_plugin_name.lower()
    new_plugin_class_name = new_plugin_name.capitalize()
    target_dir = os.path.join(RUNE_DIR, new_plugin_package)
    resource_dir = os.path.join(RESOURCE_DIR_TEMPLATE, new_plugin_package)

    if os.path.exists(target_dir):
        response = input(f"A plugin named '{new_plugin_name}' already exists. Overwrite it? (y/n): ").lower()
        if response != "y":
            print("Operation canceled.")
            return
        print(f"Overwriting existing plugin '{new_plugin_name}'...")
        shutil.rmtree(target_dir)

    # Copy skeleton plugin files while ignoring unnecessary files
    shutil.copytree(
        os.path.join(RUNE_DIR, PLUGIN_NAME), target_dir,
        ignore=shutil.ignore_patterns(
            ".git", ".gitignore", ".gitattributes", "add_example_plugin.py", "add_skeleton_plugin.py", "README.md", "LICENSE", "*.png"
        )
    )

    if not os.path.exists(resource_dir):
        os.makedirs(resource_dir)

    # Copy and rename resources
    skeleton_icon_src = os.path.join(RESOURCE_DIR_TEMPLATE, PLUGIN_NAME, "skeleton_icon.png")
    if os.path.exists(skeleton_icon_src):
        shutil.copy(skeleton_icon_src, os.path.join(resource_dir, f"{new_plugin_package}_icon.png"))
        print(f"Icon copied to {resource_dir}/{new_plugin_package}_icon.png")
    else:
        print("Warning: skeleton_icon.png not found in the skeleton plugin resources!")

    # Refactor plugin names in Java files and rename files
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".java"):
                with open(file_path, "r") as f:
                    content = f.read()

                # Replace references to SkeletonPlugin, SkeletonOverlay, etc.
                updated_content = content.replace("SkeletonPlugin", new_plugin_class_name)
                updated_content = updated_content.replace("SkeletonOverlay", f"{new_plugin_class_name}Overlay")
                updated_content = updated_content.replace("skeletonplugin", new_plugin_package)

                with open(file_path, "w") as f:
                    f.write(updated_content)

                # Rename files to match the new plugin name
                if "SkeletonPlugin" in file:
                    new_file_name = file.replace("SkeletonPlugin", new_plugin_class_name)
                    os.rename(file_path, os.path.join(root, new_file_name))
                elif "SkeletonOverlay" in file:
                    new_file_name = file.replace("SkeletonOverlay", f"{new_plugin_class_name}Overlay")
                    os.rename(file_path, os.path.join(root, new_file_name))

    print(f"New plugin '{new_plugin_name}' created successfully in '{target_dir}'.")

def ensure_skeleton_is_updated():
    skeleton_dir = os.path.join(RUNE_DIR, PLUGIN_NAME)
    resource_dir = os.path.join(RESOURCE_DIR_TEMPLATE, PLUGIN_NAME)

    # Ensure RuneLite plugins directory exists
    if not os.path.exists(RUNE_DIR):
        os.makedirs(RUNE_DIR, exist_ok=True)

    if not os.path.exists(resource_dir):
        os.makedirs(resource_dir, exist_ok=True)

    # Overwrite or create the skeleton package
    if os.path.exists(skeleton_dir):
        print(f"Overwriting skeleton plugin at {skeleton_dir}...")
        shutil.rmtree(skeleton_dir)

    shutil.copytree(
        TEMP_DIR, skeleton_dir,
        ignore=shutil.ignore_patterns(
            ".git", ".gitignore", ".gitattributes", "add_example_plugin.py", "add_skeleton_plugin.py", "README.md", "LICENSE"
        )
    )

    # Copy icon to skeleton resources
    temp_icon_path = os.path.join(TEMP_DIR, "skeleton_icon.png")
    skeleton_icon_dest = os.path.join(resource_dir, "skeleton_icon.png")
    if os.path.exists(temp_icon_path):
        shutil.copy(temp_icon_path, skeleton_icon_dest)
        print(f"Skeleton icon copied to {skeleton_icon_dest}")
    else:
        print("Warning: skeleton_icon.png not found in the repository!")

    print("Skeleton plugin updated successfully!")

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
