
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

## Usage

### Cloning the Skeleton Plugin
To use this skeleton as a base for your own plugins, clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/runelite-plugin-skeleton.git
```

### Adding the Skeleton Plugin to Your RuneLite Project

This repository includes a script, `add-skeleton-plugin.sh`, to help you add the skeleton plugin to your RuneLite project automatically. Follow the instructions below to set it up for your system.

---

## Automation Script: `add-skeleton-plugin.sh`

### Features
1. **Clones or Updates the Skeleton Plugin**: Pulls the latest version from this repository.
2. **Adds the Plugin to the Correct Directory**: Copies the skeleton plugin into `runelite-client/src/main/java/net/runelite/client/plugins`.
3. **Prevents Accidental Overwrites**: Prompts if the plugin folder already exists.
4. **Excludes Unnecessary Files**: Avoids copying `.git`, `.gitignore`, or `README.md`.

---

### Requirements
- **Git**: Ensure Git is installed on your system.
- **Bash Shell**: The script uses bash. This is standard on macOS and Linux, and Windows users can use it via WSL (Windows Subsystem for Linux) or Git Bash.

---

### Script Setup and Usage

#### 1. Download the Script
The `add-skeleton-plugin.sh` script is included in this repository. Download or clone the repository where the script resides:
```bash
git clone https://github.com/YOUR_USERNAME/runelite-plugin-skeleton.git
```

#### 2. Move the Script to Your RuneLite Project Root
Place the `add-skeleton-plugin.sh` file in the root directory of your local RuneLite project.

#### 3. Make the Script Executable (macOS/Linux)
Run the following command in the terminal:
```bash
chmod +x add-skeleton-plugin.sh
```

---

### Running the Script

#### For macOS/Linux Users:
1. Navigate to your RuneLite project directory:
   ```bash
   cd /path/to/runelite
   ```
2. Run the script:
   ```bash
   ./add-skeleton-plugin.sh
   ```

#### For Windows Users:
1. Open **Git Bash** or **WSL** (Windows Subsystem for Linux).
2. Navigate to your RuneLite project directory:
   ```bash
   cd /path/to/runelite
   ```
3. Run the script:
   ```bash
   ./add-skeleton-plugin.sh
   ```

---

### What the Script Does
1. Checks if the RuneLite plugins directory (`runelite-client/src/main/java/net/runelite/client/plugins`) exists.
2. Clones or updates the skeleton plugin from this repository.
3. Prompts you if the skeleton plugin already exists in the RuneLite project and asks for confirmation to overwrite it.
4. Copies the skeleton plugin into the correct location without including unnecessary files like `.git`, `.gitignore`, or `README.md`.

---

## Contributing
Contributions to improve the skeleton plugin are welcome! Feel free to submit a pull request or open an issue.