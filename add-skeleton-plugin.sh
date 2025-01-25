
#!/bin/bash

# Configuration
PLUGIN_REPO="https://github.com/YOUR_USERNAME/runelite-plugin-skeleton.git"
RUNE_DIR="runelite-client/src/main/java/net/runelite/client/plugins"
PLUGIN_NAME="skeletonplugin"
TEMP_DIR=".skeletonplugin-temp"

# Ensure we're in the RuneLite project directory
if [ ! -d "$RUNE_DIR" ]; then
    echo "Error: This script must be run from the RuneLite project root directory."
    exit 1
fi

# Clone or update the skeleton plugin
if [ -d "$TEMP_DIR" ]; then
    echo "Updating local skeleton plugin repository..."
    cd "$TEMP_DIR" && git pull && cd ..
else
    echo "Cloning skeleton plugin from GitHub..."
    git clone "$PLUGIN_REPO" "$TEMP_DIR"
fi

# Check if the plugin already exists in RuneLite
if [ -d "$RUNE_DIR/$PLUGIN_NAME" ]; then
    echo "Skeleton plugin already exists in RuneLite. Overwrite? (y/n)"
    read -r response
    if [[ "$response" != "y" ]]; then
        echo "Operation canceled."
        exit 0
    fi
    echo "Overwriting existing plugin..."
    rm -rf "$RUNE_DIR/$PLUGIN_NAME"
fi

# Copy the skeleton plugin to the RuneLite directory, excluding unnecessary files
echo "Copying skeleton plugin to $RUNE_DIR..."
mkdir -p "$RUNE_DIR/$PLUGIN_NAME"
rsync -a --exclude=".git" --exclude=".gitignore" --exclude="README.md" --exclude="LICENSE" "$TEMP_DIR/" "$RUNE_DIR/$PLUGIN_NAME/"

echo "Skeleton plugin added successfully!"
