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
2. **Document Creation:** Open the **Text Editor**. Write an inventory listing every physical hardware component connected to your Pi (brand of mouse, size of monitor, keyboard type).
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

Create a blank text document in the Text Editor called `temp.txt`. Save it to your desktop. Highlight it and press `Shift + Delete`. Go look in your Trash folder—explain to Dad why the file didn't show up in the Trash this time.

<div style="break-before: page;"></div>

## ⛏️ MODULE 5: HIDDEN FILES & GAME SAVES

**Objective:** Install software with Pi-Apps, locate hidden system folders, and back up a Minecraft world.

### 📜 Tech Briefing

Games write variable data—like world coordinates, player inventory, and blocks—into specific directories on your storage drive. In Linux, configuration folders and game files are frequently **hidden** to prevent accidental deletion. Any file or folder that starts with a dot (e.g., `.minecraft-pi`) is hidden by default and ignored by standard directory views.

Not every app ships with Raspberry Pi OS. Community tools like **Pi-Apps** act as an app store: you pick a program, and it runs the install steps for you.

### 🚀 Main Mission

1. **Install Pi-Apps:** Open the Terminal and run:
   ```bash
   wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
   ```
   When it finishes, you can open Pi-Apps from the application menu (**Accessories → Pi-Apps**) or by typing `pi-apps` in the terminal.
2. **Install Minecraft Pi (Modded):** In Pi-Apps, open the **Games** category, select **Minecraft Pi (Modded)**, and click **Install**. Wait until the install completes.
3. **Play and Build:** Launch Minecraft Pi (Modded) from the Games menu. Create or open a world, build a recognizable structure (like a tall tower), then quit the game completely so it saves to disk.
4. **Hidden Directory Hunt:** Open the File Manager and go to your Home directory. Turn on **Show Hidden** (often under the View menu, or press **Ctrl+H**) so folders that start with a dot appear.
5. **World Extraction:** Find the folder named `.minecraft-pi`. Inside it, locate your world data and copy that world folder into your `Documents` folder as a backup.
6. **Verification Test:** Relaunch the game, enter your world, and destroy your structure. Quit the game. Copy your backup from `Documents` back over the ruined world folder inside `.minecraft-pi`. Launch the game again and confirm your structure is restored.

### 🎮 Side Quest

Still inside `.minecraft-pi`, open `options.txt` in the Text Editor. Look at how the game stores settings (like volume or controls) as plain text you can read and edit.

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

## ⚔️ MODULE 8: PROJECT REPOSITORIES & STORY GAMES

**Objective:** Query GitHub for a software repository, clone it with `git`, and run (then edit) Python adventure games from the project.

### 📜 Tech Briefing

Software developers don't just share individual files; they package entire projects into **repositories** hosted on a platform called **GitHub**. To pull down an entire project folder with all of its code and sub-folders intact, we use a tool called `git`. The subcommand `git clone` acts like an automated copier that downloads a complete software project from the web directly into a folder on your drive.

### 🚀 Main Mission

1. **Setting the Stage:** Open your Terminal. Create a Games folder in your home directory if it does not already exist, then move into it:
   ```bash
   mkdir -p ~/Games
   cd ~/Games
   ```
2. **Finding the Repository Target:** Open your Chromium browser and navigate to `github.com`. In the search box, search for `junior-system-admin` by the user `jermatic1`. Click the project to open its main landing page. (If search is slow, go directly to `https://github.com/jermatic1/junior-system-admin`.)
3. **Acquiring the Project Link:** On the repository front page, locate the bright green button labeled **Code** (near the top right of the file list) and click it. Under the "Local" tab, select **HTTPS**. Click the small square icon next to the URL to copy the repository link to your clipboard. It should look like:
   `https://github.com/jermatic1/junior-system-admin.git`
4. **Cloning the Repository:** Return to your terminal (still inside `~/Games`). Type `git clone ` (with a space after `clone`) and paste the repository URL you just copied. Press Enter and watch the tool download the entire project.
5. **Enter the Games Bay:** Move into the cloned project and list what is inside:
   ```bash
   cd ~/Games/junior-system-admin
   ls
   cd games
   ls
   ```
   You should see files such as `iron_gates.py`, `starship_traveller.py`, and `engine.py`.
6. **Launch Iron Gates:** Run the first adventure:
   ```bash
   python3 iron_gates.py
   ```
   Play through to an ending. Use the number keys to choose your path. Press **Ctrl+C** if you ever need to exit early.
   - If Python complains that it cannot find a module named `rich`, install it with:
     ```bash
     sudo apt install python3-rich -y
     ```
     Then run `python3 iron_gates.py` again.
7. **Inspect the Source:** When you are done playing, open the game in the terminal editor:
   ```bash
   nano iron_gates.py
   ```
   Scroll through the file and find where the adventure is defined (look for the big `STORY = { ... }` dictionary near the top). Notice how each scene has a title, some text, and numbered choices that point to the next scene.
8. **Modify the Adventure:** Challenge — change something in the story! Ideas:
   - Rewrite a scene's text in your own words
   - Add a new choice that leads to a new scene
   - Rename a location or the victory message
   Save in nano with **Ctrl+O**, Enter, then exit with **Ctrl+X**. Run `python3 iron_gates.py` again and play your custom version.

### 🎮 Side Quest

Still inside the `games` folder, launch the second adventure:

```bash
python3 starship_traveller.py
```

Play a full run (watch your hull and fuel). When you finish, open it in nano:

```bash
nano starship_traveller.py
```

Look at how this story is set up. **What looks the same between `iron_gates.py` and `starship_traveller.py`?** What did the authors put in a shared file so both games could reuse it?

<div style="break-before: page;"></div>

## 🛰️ MODULE 9: MISSION CONTROL FIELD TEST

**Objective:** Reuse file, browser, terminal, and system skills on a brand-new project—no leftover files from earlier modules required.

### 📜 Tech Briefing

Real admins rarely repeat a tutorial step-for-step. They get a goal (“set up a clean workspace, document the machine, grab an asset, check disk space”) and combine tools they already know. This field test builds a fresh folder tree called **Mission Control** and walks the desktop like a map.

### 🚀 Main Mission

1. **Build the Base:** Open the Terminal. Create the Mission Control tree and confirm it exists:
   ```bash
   mkdir -p ~/Mission_Control/{logs,media,archive}
   ls ~/Mission_Control
   ```
   Optional: use the long-list flag you learned earlier (`ls -l ~/Mission_Control`) to see extra detail.
2. **Write the Briefing:** Open the **Text Editor**. Create a file named `briefing.txt` and save it as `~/Mission_Control/logs/briefing.txt`. Include:
   - Your name
   - Today’s date
   - The **absolute path** to the Mission_Control folder (use the File Manager path bar or run `pwd` after `cd ~/Mission_Control`)
3. **Hardcopy:** Open `briefing.txt` and print a physical copy on the family printer.
4. **SpaceX Asset + Wallpaper:**
   - Open **Chromium** and go to `google.com`. Confirm you are logged into your Google account.
   - Search for a cool **SpaceX** image. Save it into `~/Mission_Control/media/` (right-click → **Save Image As...**).
   - Set that image as your desktop wallpaper (right-click the desktop → **Desktop Preferences**, or use your system’s background settings). Point the wallpaper picker at the file inside `Mission_Control/media/`.
5. **Copy, Cut, Trash:**
   - **Copy** your SpaceX image from `media/` into `archive/`.
   - Create a spare duplicate somewhere under Mission_Control, then **Cut** (move) it into `archive/` so you practice move as well as copy.
   - Delete one spare copy with **Move to Trash**, open Trash to confirm it is there, then **Empty Trash**.
6. **Hidden Folder:** In File Manager, go to your Home directory and show hidden files (**Ctrl+H** or View → Show Hidden). In the Terminal, create your own hidden notes folder and a file inside it:
   ```bash
   mkdir -p ~/.agent_notes
   ```
   Use the Text Editor (or `nano`) to add a short note file inside `.agent_notes`. Find `.agent_notes` again in File Manager with hidden files visible.
7. **Disk Space Two Ways:**
   - Terminal: run `df -h` and find the line for your main disk (often `/`).
   - File Manager: open `/` (root) from the sidebar or path bar. Read the **free space** and **total space** shown in the bottom status area.
   - Add both the terminal reading and the File Manager reading as new lines in `briefing.txt`, then save.

### 📥 Downloads Desk

1. In Chromium, open your downloads list (menu → **Downloads**, or go to `chrome://downloads`).
2. Find the SpaceX image you saved. Use the folder icon / “Show in folder” control (wording varies) to jump straight to the file in File Manager.
3. Confirm it landed under `~/Mission_Control/media/` (or move it there if the browser defaulted to `Downloads`).
4. From File Manager, open `Downloads` once and sort by **Date** so the newest files float to the top—handy when you are not sure what just arrived.

### 🖥️ System Awareness

1. **Network:** Click the network icon on the panel. Confirm you are connected and note the Wi‑Fi network name.
2. **Sound:** Open sound settings, play a quick test sound if available, and move the volume up/down so you know where audio lives.
3. **Power menu:** Open the shutdown/power menu and point out the difference between **Restart** and **Shutdown** (do not shut down until the field test is finished).
4. **System Monitor:** Open **Task Manager** or **System Monitor**. With Chromium still open, find it in the process list and notice whether it is using CPU or memory. Close the monitor when you are done.

### 🎮 Side Quest

Give Dad a 60-second **tour guide**: start at the desktop wallpaper, open `~/Mission_Control`, show `briefing.txt`, the image in `media/`, your hidden `.agent_notes` folder, and the free space on `/`. Narrate each click.

<div style="break-before: page;"></div>

## 💿 MODULE 10: THE LITE ARCHITECTURE TRANSITION

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

## 📡 MODULE 11: HEADLESS OPERATIONS & REMOTE SHELLS

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
