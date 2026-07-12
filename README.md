# 📂 JUNIOR SYSTEM ADMINISTRATOR PROTOCOL

## 🖥️ MODULE 1: HARDWARE ASSEMBLY & ACCOUNT PROVISIONING

**Objective:** Assemble a functioning workstation and provision an administrator user account.

### 📜 Tech Briefing

A computer requires a complete hardware circuit to function. Power enters the mainboard via USB-C, the processor executes code stored on the MicroSD card, and signals are distributed to input devices (keyboard/mouse) and output devices (monitor via HDMI). Once the hardware handshake succeeds, the operating system requires an initial user account provisioned with administrator privileges to establish security boundaries.

### 🚀 Main Mission

1. **Physical Assembly:** Connect the micro-HDMI cable to the port labeled `HDMI0` on the Pi, then connect the other end to the monitor. Plug the USB keyboard and mouse into the ports. Do not apply power yet.
2. **Boot Initialization:** Insert the pre-flashed MicroSD card into the slot on the bottom of the Pi. Connect the power adapter to the wall, then plug it into the Pi.
3. **Account Provisioning:** Follow the on-screen wizard to create your primary user account. Choose a unique username and a secure password.
4. **Network Integration:** Use the desktop taskbar icon to connect the device to the family Wi-Fi network.

### 🎮 Side Quest

Find the application named **Terminal** in your menus and click it to open.
 - type `whoami`, and hit Enter. Verify that the output matches the exact username you configured during setup.
 - type `ping google.com`, and hit Enter. After it runs for a few seconds and you see output press `Ctrl-C` to stop it. About how many ms was the average ping time?

<div style="break-before: page;"></div>

## 📄 MODULE 2: FILE SYSTEMS & NETWORK PRINTING

**Objective:** Map directory trees and configure hardware peripherals over the local network.

### 📜 Tech Briefing

Linux organizes everything into a unified hierarchy starting at the root directory (`/`). Users store personal data inside their Home directory (`/home/username/`). Applications reference files using strict **absolute paths**. To output digital documents to physical paper, Linux uses a printing subsystem called **CUPS** (Common UNIX Printing System) to discover hardware addresses on the local area network (LAN).

### 🚀 Main Mission

1. **Directory Generation:** Open the File Manager utility. Navigate to your Home directory, open the `Documents` folder, and create a new folder named `System_Logs`.
2. **Document Creation:** Open the **Mousepad** text editor. Write an inventory listing every physical hardware component connected to your Pi (brand of mouse, size of monitor, keyboard type).
3. **Structured Save:** Save this document as `hardware_inventory.txt` directly inside your new `System_Logs` folder.
4. **Peripheral Mapping:** Open the system settings menu and select **Print Settings** (or **Printers**). Click "Add", select "Network Printer", and wait for the system to discover the family printer on the network.
5. **Hardcopy Execution:** Open your `hardware_inventory.txt` file and print a physical copy to confirm the driver and network path are operational.

### 🎮 Side Quest

In the File Manager, go into your `System_Logs` folder. Click on the path bar at the top of the window to change it from icons to text. Copy or write down that exact absolute path string.

<div style="break-before: page;"></div>

## 🌐 MODULE 3: USER AUTHENTICATION & THE WEB

**Objective:** Configure identity access management tools and securely download assets.

### 📜 Tech Briefing

A web browser translates remote source code over network protocols into a visual user interface. To browse securely, professionals use password managers like **Bitwarden** to handle credentials through encrypted vaults. Logging into browser sessions ensures search engine filters are active, protecting your machine from untrusted scripts.

### 🚀 Main Mission

1. **Browser Initialization:** Open the **Chromium** web browser from your desktop taskbar.
2. **Extension Deployment:** Navigate to the Chrome Web Store, search for **Bitwarden**, and install the extension.
3. **Identity Authentication:** Click the Bitwarden extension icon in the top right, log in using the your credentials.
4. **Google Login** Navigate to `google.com` and sign in to your account. Bitwarden should popup and provide your credentials.
4. **Targeted Research:** Use Google to find the official wiki page for your favorite video game. Locate a high-resolution image of a character on that wiki.
5. **Disk Write:** Right-click the image, select "Save Image As...", and save it directly into your local directory.

### 🎮 Side Quest

Set the downloaded image as your system desktop background. Right-click the desktop, open **Desktop Preferences**, and locate the exact folder where your image was saved.

<div style="break-before: page;"></div>

## ✂️ MODULE 4: DATA MANIPULATION & UNLINKING (THE TRASH)

**Objective:** Master copying, cutting, pasting, and securely deleting files.

### 📜 Tech Briefing

When you interact with files, you can alter their location on the disk in two ways: **Copying** creates an identical duplicate of the file in a new location, leaving the original alone. **Cutting** (or moving) unlinks the file from its old location and places it in a new one. When you delete a file normally, it isn't erased from the disk immediately; it is moved to a hidden storage container called the **Trash** (or Recycle Bin), which holds files until you choose to empty it.

### 🚀 Main Mission

1. **The Duplicate Target:** Open your File Manager and go to your `Pictures` folder. Locate the character image you saved during Module 3.
2. **The Copy Sequence:** Right-click the image and select **Copy** (or click it and press `Ctrl + C`). Navigate to your `Documents` folder, right-click an empty space, and select **Paste** (`Ctrl + V`). Verify that you now have two identical copies of this image in different folders.
3. **The Cut Sequence:** Go back to your `Pictures` folder. Create a new folder inside it called `Wallpapers`. Right-click your original image, select **Cut** (`Ctrl + X`), open the `Wallpapers` folder, and **Paste** it inside. Check your main Pictures folder to confirm the original image disappeared from there.
4. **The Disposal:** Go to the `Documents` folder where you pasted the duplicate image. Right-click that duplicate file and select **Move to Trash** (or click it and press the `Delete` key).
5. **Purging the System:** Look at your desktop layout or side panel for the **Trash** icon. Open it to verify your file is waiting inside. Right-click the Trash icon and select **Empty Trash** to permanently clear the storage space.

### 🎮 Side Quest

Create a blank text document in Mousepad called `temp.txt`. Save it to your desktop. Highlight it and press `Shift + Delete`. Go look in your Trash folder—explain to Dad why the file didn't show up in the Trash this time.

<div style="break-before: page;"></div>

## ⛏️ MODULE 5: COMPILING & MANAGING GAME SAVES

**Objective:** Locate hidden system files and manage backup directories using Minecraft.

### 📜 Tech Briefing

Games write variable data—like world coordinates, player inventory, and blocks—into specific directories on your storage drive. In Linux, configuration folders and game files are frequently hidden to prevent accidental deletion. Any file or folder that starts with a dot (e.g., `.minecraft`) is hidden by default and ignored by standard directory views.

### 🚀 Main Mission

1. **Runtime Execution:** Open the application menu, go to "Games", and launch **Minecraft Pi Edition**. Generate a new world, build a recognizable structure (like a tall tower), and exit the game to force the software to commit its save state to the disk.
2. **Hidden Directory Hunt:** Open your File Manager and navigate to your Home directory. Reveal the hidden files in this directory.
3. **World Extraction:** Locate the folder where Minecraft stores its worlds (look for a folder named `~/.minecraft/games/com.mojang/minecraftWorlds`). Copy your world folder and paste it into your `Documents` folder as a secure backup.
4. **Verification Test:** Relaunch the game, enter your world, and completely destroy your structure. Close the game. Now, copy your backup folder from `Documents` and overwrite the ruined folder inside the hidden directory. Relaunch the game to verify your structure is restored.

### 🎮 Side Quest

While inside the hidden Minecraft folder, look for a text file named `options.txt`. Open it in Mousepad to see how the game stores settings like volume or control layouts as plain text variables.

<div style="break-before: page;"></div>

## 🧭 MODULE 6: THE COMMAND HELP SYSTEM & SYSTEM UTILITIES

**Objective:** Learn how to read command-line manuals using flags and arguments.

### 📜 Tech Briefing

When using the Terminal, you execute programs by typing their names. But how do you know what a command can do without guessing? Developers build a help manual directly into almost every command. You access this manual by appending a **flag** to the end of your command. Flags usually start with dashes, like `-h` or `--help`. A flag changes how a tool behaves, or instructs it to tell you its own instructions.

### 🚀 Main Mission

1. **Terminal Help Probe:** Open your Terminal. Type the system manual command `mkdir --help` and press Enter. Read the text that outputs to the screen. Find the section that explains what the `-p` flag does.
2. **Directory Trees:** Use what you just learned. Instead of making one folder at a time, use the helper flag you just discovered to build a deep nested chain of folders all with one single command: `mkdir -p ~/Downloads/Games/Retro/Python/Sources`.
3. **The List Helper:** Type `ls --help` into the terminal. Look through the options until you find the flag that lists files in a "long" format showing exact file sizes and creation dates. Run `ls` with that flag inside your Downloads folder to test it.
4. **The Disk Space Analyzer:** Type `df` and press Enter. The numbers look confusing because they are in raw blocks. Now type `df --help` to find the flag that makes the output "Human Readable" (showing gigabytes and megabytes instead of giant blocks of numbers). Run the command with that flag.

### 🎮 Side Quest

Type `man mkdir` into the terminal. This opens the complete "Manual Page" book layout for that tool. Use your arrow keys to scroll, and press the `q` key on your keyboard when you want to exit the manual and return to your terminal prompt.

<div style="break-before: page;"></div>

## 🦍 MODULE 7: WEBSCRAPING RAW SOURCE CODE & GORILLAS PHYSICS

**Objective:** Mine a direct download URL from a source code hosting platform and modify Python runtime variables.

### 📜 Tech Briefing

To download code files from the web using the Terminal, we use a command-line tool named `wget` (Web Get). You feed `wget` a specific web link, and it fetches that file directly to your current folder.

However, if you point `wget` at a normal webpage link (like a standard GitHub page), it will download the visual HTML formatting instead of the actual script. To get the raw, unformatted text file, you must find the **Raw Source URL**. Today you will download a Python remake of *Gorillas*—a 1990 MS-DOS game where gorillas throw exploding bananas over a city skyline.

### 🚀 Main Mission

1. **Targeting the Directory:** Open your Terminal. Navigate into the retro game folder you created during your Help system training: `cd ~/Downloads/Games/Retro/Python/Sources`.
2. **Navigating the Code Vault:** Open your Chromium web browser. Go to `github.com`. In the search bar at the top, type `ByScreams/Gorillas-Python` and press Enter. Click on the matching project repository from the search results.
3. **Locating the Main Script:** Look at the list of project files on the page. Find the main game file named `gorillas.py` and click on it. The screen will load a preview showing lines of code.
4. **Extracting the Raw Link:** Above the box displaying the code, look at the menu buttons on the right side. Locate and click the button labeled **Raw**. Notice how the webpage changes to a completely blank white background containing only pure text code.
5. **Executing Web Get:** Click into your browser's address bar at the very top. Highlight and copy the entire URL (it should start with `https://raw.githubusercontent.com/...`). Return to your Terminal window, type `wget `, paste the URL directly after the space, and press Enter.
6. **Execution & Modification:** Once the download reaches 100%, launch the game by typing `python3 gorillas.py`. Play a round, then close the game window. Open the file by typing `nano gorillas.py`. Find the constant variable labeled `GRAVITY = 9.8` or `SPEEDCONST`. Change the number to `2.0` to create moon-gravity physics. Save (`Ctrl + O`, `Enter`) and exit nano (`Ctrl + X`). Run the game again to test your custom build.

### 🎮 Side Quest

Re-open the script in `nano`. Scroll down and find where the game draws the city skyline or calculates player names. See if you can change the text string to rename "Player 1" to your own custom gaming handle.

<div style="break-before: page;"></div>

## ⚔️ MODULE 8: PROJECT REPOSITORIES & TERMINAL DUNGEON CRAWLERS

**Objective:** Query GitHub for a software repository and clone all assets via the command line.

### 📜 Tech Briefing

Software developers don't just share individual files; they package entire projects into "Repositories" hosted on a platform called **GitHub**. To pull down an entire project folder with all of its code, images, and sub-folders intact, we use a tool called `git`. The subcommand `git clone` acts like an automated copier that downloads a complete software project from the web directly into a folder on your drive.

### 🚀 Main Mission

1. **Setting the Stage:** Open your Terminal. Change directories back to your main development folder: `cd ~/Downloads/Games/Retro`.
2. **Finding the Repository Target:** Open your Chromium browser and navigate to `github.com`. In the search box, search for a terminal-based dungeon crawler project named `python-roguelike` by the user `the-gorgon`. Click on the project to open its main landing page.
3. **Acquiring the Project Link:** On the repository front page, locate the bright green button labeled **Code** (near the top right of the file list) and click it. Under the "Local" tab, select **HTTPS**. Click the small square icon next to the URL to copy the repository link to your clipboard.
4. **Cloning the Repository:** Return to your terminal. Type `git clone ` and paste the repository URL you just copied (it should end in `.git`). Press Enter and watch the tool download the entire architecture.
5. **Reading the Manual:** While the download finishes, look back at your browser window. Scroll down past the file list on the GitHub page to read the `README.md` documentation file. Read through the text to discover which keyboard keys control player movement, attacking, and inventory.
6. **Text-Dimension Launch:** Go back to your terminal. Move into the newly created folder by typing `cd python-roguelike`. Type `ls` to view the asset structure. Launch the engine by typing `python3 main.py` (or the script filename specified in the readme). Navigate through the dungeon using your keyboard based on the instructions you read.

### 🎮 Side Quest

Use your system package manager to download a classic server visualization tool by executing `sudo apt install cmatrix -y`. Once installed, type `cmatrix` to turn your screen into a cascading wall of terminal code. Press `q` to terminate it.

<div style="break-before: page;"></div>

## 💿 MODULE 9: THE LITE ARCHITECTURE TRANSITION

**Objective:** Build and configure a minimalist, non-graphical operating system image.

### 📜 Tech Briefing

Production-grade enterprise servers almost never waste RAM or processor cycles rendering a graphical user desktop interface. They run on minimalist deployments called **Lite Images** which boot directly into a text-only interface. Today, you will use your primary Pi setup to write a fresh, terminal-only operating system onto a secondary storage drive.

### 🚀 Main Mission

1. **Media Preparation:** Insert a secondary, blank MicroSD card (using a USB adapter) into one of the Pi's blue USB 3.0 ports.
2. **Utility Deployment:** Open the Terminal. Install the official command-line imaging tool or download the repository packages required to flash images via the command line.
3. **Target Image Acquisition:** Use your browser or terminal to download the official **Raspberry Pi OS Lite (64-bit)** image file (`.img.xz`).
4. **The Flash Sequence:** Use the command line to write (flash) the Lite OS image directly onto your secondary USB/MicroSD card.
5. **Hardware Transition:** Once the flash completes successfully, safely unmount the drive. Shut down your Raspberry Pi using the terminal command `sudo poweroff`. Unplug the power cable, remove your primary MicroSD card, insert the new Lite MicroSD card, and plug the power back in.

### 🎮 Side Quest

When the system boots up to a completely black screen with white text asking for a login, enter your username and password. Note how when typing your password, the screen shows absolutely nothing (no stars, no letters) for security. Type it blind and hit Enter to log in.

<div style="break-before: page;"></div>

## 📡 MODULE 10: HEADLESS OPERATIONS & REMOTE SHELLS

**Objective:** Provision network architecture and configure secure remote shell access from the command line.

### 📜 Tech Briefing

System administrators rarely sit in front of the physical hardware servers they manage. Instead, they use a network protocol called **SSH (Secure Shell)** to open an encrypted text terminal over the network. Because your Lite operating system has no mouse or desktop menu, you must use command-line utilities to configure network configurations and enable the background system service (daemon) that listens for remote connections.

### 🚀 Main Mission

1. **CLI Network Provisioning:** Log into your new Lite system. Launch the text-based configuration menu by typing `sudo raspi-config`. Navigate using your arrow keys to **Network Options**, select **Wi-Fi**, and enter your home network name (SSID) and password.
2. **Repository Sync:** Once connected to the network, pull down the latest system security patches by running `sudo apt update && sudo apt upgrade -y`.
3. **SSH Service Initialization:** Re-enter `sudo raspi-config`. Navigate to **Interface Options**, select **SSH**, and choose **Yes** to enable the secure shell daemon. Exit the menu.
4. **Network Identification:** Type `hostname -I` in the terminal to find your Pi's current local IP address. Write this down.
5. **Remote Handshake:** Leave the physical Pi. Walk over to your secondary Linux desktop computer, open its terminal, and type `ssh username@[IP_ADDRESS_OF_THE_PI]`. Enter your password to control your Raspberry Pi completely over the network without a monitor attached to it.

### 🎮 Side Quest

While remoted into the Pi from your other computer, type `sudo apt install bastet -y` to install a command-line Tetris clone. Run it by typing `bastet` and play a game entirely through your network stream.
