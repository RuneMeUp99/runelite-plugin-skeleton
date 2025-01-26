
import os
import shutil
import re

# Configuration
RUNE_DIR = os.path.join("runelite-client", "src", "main", "java", "net", "runelite", "client", "plugins")
RESOURCE_DIR_TEMPLATE = os.path.join("runelite-client", "src", "main", "resources", "net", "runelite", "client", "plugins")
VALID_PLUGIN_NAME_REGEX = r"^[a-zA-Z][a-zA-Z0-9_]*$"

def validate_plugin_name(plugin_name):
    if not re.match(VALID_PLUGIN_NAME_REGEX, plugin_name):
        print("Error: Plugin name must start with a letter and contain only letters, numbers, and underscores.")
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

    # Create the plugin directory and boilerplate files
    os.makedirs(target_dir)
    os.makedirs(resource_dir)

    # Create the Java files with updated author and donation information
    java_files = {
        f"{new_plugin_class_name}Plugin.java": f"""package net.runelite.client.plugins.{new_plugin_package};

import com.google.inject.Provides;
import javax.inject.Inject;
import lombok.extern.slf4j.Slf4j;
import net.runelite.api.Client;
import net.runelite.client.config.ConfigManager;
import net.runelite.client.plugins.Plugin;
import net.runelite.client.plugins.PluginDescriptor;

@Slf4j
@PluginDescriptor(
        name = "{new_plugin_class_name} Plugin",
        description = "A custom plugin created using the boilerplate script by SyntaxSkater",
        tags = {{"example", "template", "plugin"}}
)
public class {new_plugin_class_name}Plugin extends Plugin
{{
    @Inject
    private Client client;

    @Provides
    {new_plugin_class_name}Config provideConfig(ConfigManager configManager)
    {{
        return configManager.getConfig({new_plugin_class_name}Config.class);
    }}

    @Override
    protected void startUp() throws Exception
    {{
        log.info("{new_plugin_class_name} Plugin started! Created by SyntaxSkater (GitHub: https://github.com/SyntaxSkater, OSRS: Rune Me Up99)");
    }}

    @Override
    protected void shutDown() throws Exception
    {{
        log.info("{new_plugin_class_name} Plugin stopped!");
    }}
}}
""",
        f"{new_plugin_class_name}Config.java": f"""package net.runelite.client.plugins.{new_plugin_package};

import net.runelite.client.config.Config;
import net.runelite.client.config.ConfigGroup;

@ConfigGroup("{new_plugin_package}")
public interface {new_plugin_class_name}Config extends Config
{{
    // Configuration options go here
}}
""",
        f"{new_plugin_class_name}Overlay.java": f"""package net.runelite.client.plugins.{new_plugin_package};

import javax.inject.Inject;
import net.runelite.client.ui.overlay.Overlay;
import net.runelite.client.ui.overlay.OverlayPosition;

public class {new_plugin_class_name}Overlay extends Overlay
{{
    @Inject
    private {new_plugin_class_name}Plugin plugin;

    @Override
    public OverlayPosition getPosition()
    {{
        return OverlayPosition.DYNAMIC;
    }}

    @Override
    public Dimension render(Graphics2D graphics)
    {{
        // Rendering logic here
        return null;
    }}
}}
""",
        f"{new_plugin_class_name}Panel.java": f"""package net.runelite.client.plugins.{new_plugin_package};

import javax.swing.*;
import net.runelite.client.ui.PluginPanel;

public class {new_plugin_class_name}Panel extends PluginPanel
{{
    public {new_plugin_class_name}Panel()
    {{
        JLabel label = new JLabel("Plugin created by SyntaxSkater (GitHub: https://github.com/SyntaxSkater, OSRS: Rune Me Up99)");
        add(label);

        JLabel donationLabel = new JLabel("Donations appreciated in the form of OSRS GP to Rune Me Up99");
        add(donationLabel);
    }}
}}
"""
    }

    # Write the Java files to the target directory
    for file_name, content in java_files.items():
        with open(os.path.join(target_dir, file_name), "w") as f:
            f.write(content)

    # Add the resource file (icon)
    icon_path = os.path.join(resource_dir, f"{new_plugin_package}_icon.png")
    with open(icon_path, "wb") as f:
        f.write(b"")  # Placeholder for the actual PNG content

    print(f"New plugin '{new_plugin_name}' created successfully in '{target_dir}'.")

def main():
    # Ensure the RuneLite directory exists
    if not os.path.exists(RUNE_DIR):
        print("Error: This script must be run from the RuneLite project root directory.")
        return

    try:
        create_new_plugin()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
