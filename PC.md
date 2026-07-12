# 💻 PC CORE INFRASTRUCTURE TRACK (STANDALONE ARCHITECTURE)

## ⚙️ MODULE 1: THE BIOS HANDSHAKE & FIRMWARE NAVIGATION

**Objective:** Learn how to access low-level motherboard firmware, navigate system settings without a mouse, and safely exit without altering core system configurations.

### 📜 Tech Briefing

Before any operating system (like Linux or Windows) can load, your computer runs a tiny, built-in program stored directly on a chip on the motherboard called the **BIOS** (Basic Input/Output System) or **UEFI**. The BIOS initializes the physical hardware components, checks that your RAM and processor are working, and decides which storage drive to hand control over to next.

Because the BIOS runs *before* the operating system, it has its own special command menu. However, you only have a split-second window to open it right when the physical power turns on.

### 🚀 Main Mission

1. **The Interception Window:** Shut down the Lenovo laptop completely. Turn it back on and watch the screen closely. Computer manufacturers assign a specific button to open the BIOS, but it only works if you tap it rapidly *immediately* after pressing the power button.
2. **The BIOS Probe:** If you miss the window and the computer boots up normally into your usual desktop, shut down the computer and try again. Try tapping one of these common diagnostic keys repeatedly right after pressing power: `F1`, `F2`, `F12`, or `Enter`. *(Hint: Lenovo ThinkPads usually use `F1` or require you to press `Enter` to interrupt normal startup).*
3. **Firmware Navigation:** Once inside the BIOS utility, your mouse will not work. You must use only your keyboard **arrow keys** to shift between menus, and the `Enter` key to look inside options. Look across the top tabs and find the one labeled **Boot** or **Startup** to see where the computer lists the available storage drives.
4. **Safe Discard:** To ensure we don't accidentally alter how the computer functions, look at the bottom or side legends for the function key assigned to **Exit and Discard Changes** (usually `Esc` or `F10` followed by choosing "No"). Execute this command to restart the computer safely without saving any edits.

### 🎮 Side Quest

While exploring the main page of the BIOS, look for a section listing the hardware. Find the exact speed of your CPU (Processor) and the total amount of RAM (Memory) installed in this laptop. Write them down to show Dad.

<div style="break-before: page;"></div>

## 🚦 MODULE 2: BOOTLOADERS & DUAL-BOOT NAVIGATION

**Objective:** Interrupt a bootloader countdown and navigate a GRUB menu to successfully jump between different operating systems.

### 📜 Tech Briefing

When a computer has more than one operating system installed on its drive, it relies on a specialized piece of software called a **Bootloader**. On Linux systems, the standard bootloader is called **GRUB** (Grand Unified Bootloader).

GRUB acts like a traffic cop at a major intersection. When the computer turns on, it pauses the startup sequence, displays a menu of your available operating systems, and runs a countdown timer. If you don't touch anything, it automatically loads the default choice (in this case, Ubuntu Linux). If you interrupt it, you can manually tell the hardware to route you into an entirely different environment, like Windows.

### 🚀 Main Mission

1. **The Countdown Interruption:** Turn on or restart the laptop. Wait for the dark **GRUB menu** to appear displaying your Ubuntu and Windows options. Look at the bottom of the screen to find the 10-second countdown timer. Before it hits zero, press the **Up** or **Down** arrow keys. Verify that touching the arrows freezes the countdown timer entirely.
2. **Windows Boot Execution:** Use your arrow keys to highlight **Windows Boot Manager** and press `Enter`. Let Windows load fully, log into the desktop, and explore for a moment.
3. **The Return Sequence:** Click the Windows Start Menu, select **Power**, and click **Restart**.
4. **Linux Boot Execution:** When the GRUB menu reapplies itself on restart, interrupt the timer again, but this time select **Ubuntu** and press `Enter`.
5. **The Multi-Boot Cycle:** Repeat this entire switching cycle (Booting to Windows, restarting, and booting back to Linux) two more times until you can comfortably toggle between both operating systems without hesitation.

### 🎮 Side Quest

While looking closely at the GRUB menu selections, look below the main Linux and Windows paths. Find the option labeled **Advanced options for Ubuntu** and navigate into it using your arrows. Look at the different version numbers listed. Ask Dad what a Linux "kernel" is and why GRUB keeps older versions safely stored away in this menu.

<div style="break-before: page;"></div>

## 💾 MODULE 3: HARDWARE DUMPING & CROSS-PLATFORM STORAGE

**Objective:** Navigate the Windows desktop environment, safely assemble and align physical cartridge dumping hardware, and extract physical game data to an external flash drive completely offline.

### 📜 Tech Briefing

Unlike Linux, which treats every drive as a directory folder starting at root (`/`), Windows organizes its storage drives using **Drive Letters**. Your main system drive is usually `C:`, and when you plug in a temporary USB flash drive, Windows assigns it a new letter like `D:` or `E:`.

Today, you are going to act as a digital preservation archivist. You will use a hardware device called the **RetroBlaster 2.0** to read the game data (the **ROM**) directly out of a physical Nintendo 64 game cartridge. The software will copy the binary code from the cartridge's chips over the USB cable and write it into a file on the computer. Then, you will locate that file and copy it to a portable flash drive so it can be brought over to your Linux system later.

<div style="break-before: page;"></div>

### 🔍 HARDWARE REFERENCE SHEET

Before handling the electronics, review these rules. Because the device has bare circuits, you must read the board directly with your eyes:

* **The Voltage Toggle:** Look at the small physical switch on the main RetroBlaster board. It has two positions: **5V** and **3V**. Nintendo 64 cartridges run on **3V**. Ensure this switch is pushed toward the **3V** marking before inserting anything.
* **Adapter Alignment:** The N64 extension adapter slots into the top of the main RetroBlaster board. Ensure the pins line up perfectly. Push it straight down firmly—never rock it side-to-side, or you might bend the delicate pins.
* **Cartridge Orientation:** When sliding the N64 game cartridge into the slot, the **front label of the game must face forward** (the same side as the status light on the RetroBlaster mainboard).

<div style="break-before: page;"></div>

### 🚀 Main Mission

1. **The Windows Environment Boot:** Turn on the laptop. At the dark GRUB menu, press the down arrow key to highlight **Windows Boot Manager** and press `Enter`. Log into the desktop user account.
2. **Physical Hardware Assembly:**
* Verify the RetroBlaster toggle switch is set to **3V**.
* Insert the N64 adapter slot into the RetroBlaster main board.
* Slide your N64 game cartridge firmly into the slot with the front label facing forward.
* Connect the USB cable from the RetroBlaster into a USB port on the laptop.


3. **The Graphical Execution:** Look on the Windows Desktop layout for an icon named **RetroBlaster**. Double-click it to launch the software interface.
4. **Target Alignment:** Inside the application window, look at the row of tabs near the top running left to right. Locate and click on the **N64** tab.
5. **The Archival Extraction:**
* Click the button labeled **Dump ROM**.
* A window will pop up asking you where to save the file and what to name it. Type the actual name of the game (like `MarioKart64`) and click **Save**.
* Watch the physical light on the hardware board turn on. A progress bar inside the software will fill up. *Do not bump, touch, or move the laptop or hardware while this bar is active.*


6. **Locating the Loot:** Once the status bar finishes and says the dump was successful, close the RetroBlaster application. Click the folder icon on the taskbar at the bottom of the screen to open **File Explorer** (the Windows version of File Manager). Click on **Documents** in the left sidebar to locate your newly created game file.
7. **External Media Export:** Insert your physical USB flash drive into an open port on the laptop. Look at the left sidebar of your File Explorer window under **This PC** and watch a new drive letter appear (like `D:` or `E:`). Right-click your game file, select **Copy**, click on your USB drive icon in the sidebar, right-click an empty space inside it, and select **Paste**.
8. **Secure Demounting:** To avoid corrupting your data, do not just yank the USB drive out. Look at the bottom-right corner of the Windows taskbar, click the tiny up-arrow icon, find the tiny USB shape labeled **Safely Remove Hardware and Eject Media**, click it, and click your specific drive name. Wait for the message that says it is safe before pulling it out of the machine.

### 🎮 Side Quest

Open File Explorer, go into your USB drive, right-click your game file, and select **Properties**. Look at the line labeled **Size on disk**. In the world of the Nintendo 64, game sizes are almost always exact powers of two (specifically 8MB, 12MB, 16MB, 32MB, or 64MB). Report the exact file size back to Dad and tell him if it fits the rules of classic 90s hardware constraints!
