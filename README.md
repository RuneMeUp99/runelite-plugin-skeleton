# RuneLite Plugin Skeleton

A starting template for creating RuneLite plugins. This skeleton includes:
- A basic plugin structure
- Configuration settings
- Overlay integration
- Event subscriptions
- Plugin panel

---

## Features
1. **Main Plugin Class**: The core logic of the plugin.
2. **Configuration Class**: Adds settings to the RuneLite configuration menu.
3. **Overlay**: Displays graphics or text on the RuneLite game screen.
4. **Plugin Panel**: Adds an interactive panel to the RuneLite sidebar.

---

### Download Only the Python Script

If you only need the Python script, you can download it directly from the repository:

1. Navigate to the Python script in the repository:  
   [add_skeleton_plugin.py](https://github.com/SyntaxSkater/runelite-plugin-skeleton/blob/main/add_skeleton_plugin.py)

2. Click the **Raw** button on the page.

3. Right-click and choose **Save As** to save the file locally.

4. Open your terminal and go to the Runelite root directory

5. Run this in your terminal:
```bash
python add_skeleton_plugin.py
```

---

### What the Script Does
1. Checks if the RuneLite plugins directory (`runelite-client/src/main/java/net/runelite/client/plugins`) exists.
2. Clones or updates the skeleton plugin from this repository.
3. Prompts you if the skeleton plugin already exists in the RuneLite project and asks for confirmation to overwrite it.
4. Allows you to create new plugins using the plugin skeleton.

---

## Contributing
Contributions to improve the skeleton plugin are welcome! Feel free to submit a pull request or open an issue.

---

## Submitting Plugins to the Plugin Hub
Submitting your plugin to the RuneLite Plugin Hub allows other users to download and use it.

#### Fork the RuneLite Plugin Hub Repository:
1. Go to the [RuneLite Plugin Hub GitHub Repo](https://github.com/runelite/plugin-hub).
2. Fork the repository to your GitHub account.

#### Add Your Plugin to the Plugin Hub:
1. Clone your fork of the plugin hub:
   ```bash
   git clone https://github.com/<YourUsername>/plugin-hub.git
   ```
2. Create a folder for your plugin in the `plugin-hub/plugins/` directory.
3. Add your plugin source code and metadata (e.g., `plugin.json`) to the folder.

#### Submit a Pull Request:
1. Commit and push your changes to your fork:
   ```bash
   git add .
   git commit -m "Add my custom plugin"
   git push origin main
   ```
2. Go to the original plugin hub repository and submit a pull request from your fork.

#### Wait for Approval:
- The RuneLite team will review your plugin. Once approved, it will appear in the Plugin Hub for all users to download.
