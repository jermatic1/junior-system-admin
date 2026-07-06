---

---

# 🆘 "I'M STUCK!" STEP-BY-STEP WALKTHROUGHS (KEEP SEPARATE)

### Module 1 Help

* **The display is completely black:** Check the micro-HDMI cable. The Pi has two ports; ensure it is plugged into `HDMI0`, which is the port closest to the power cable connector. Make sure the monitor is turned on and set to the correct input source.

### Module 2 Help

* **The Printer isn't showing up:** In the Print Settings menu, click "Add". If it doesn't appear under network devices automatically, find your printer's IP address from Dad. Select **Find Network Printer**, type the exact IP address (e.g., `192.168.1.150`), and click **Find** to force Linux to connect directly.

### Module 3 Help

* **Can't find the Bitwarden extension:** Click the three dots in the top-right corner of Chromium, go to **Extensions** -> **Visit Chrome Web Store**. Type "Bitwarden" in the search box, click "Add to Chrome". Once installed, click the puzzle piece icon next to the address bar to open it.

### Module 4 Help

* **The Shift+Delete trick:** When you press `Shift + Delete` on a file, it completely bypasses the Trash folder container and deletes the reference links directly off your hard drive. The computer immediately reclaims that space, which is why it didn't show up in the Trash bin.

### Module 5 Help

* **I can't see hidden folders:** Open your File Manager, click **View** in the top menu bar, and check the box that says **Show Hidden**. Alternatively, hold down the `Ctrl` key and press `H`. Look for directories that start with a dot, like `.minecraft`.

### Module 6 Help

* **What did the mkdir -p flag do?:** The `-p` flag stands for "parents". It tells the `mkdir` tool: *"If the folders inside this path don't exist yet, go ahead and automatically create all the parent folders in the chain at the exact same time."*
* **The human-readable flag for df:** Running `df -h` uses the `-h` flag (human-readable) to turn long byte values into easily readable sizes like `15G` or `320M`.

### Module 7 Help

* **The web layout changed or I can't find the Raw button:** If GitHub's interface layout updates, you can also view raw text by clicking the three horizontal dots `...` on the upper-right corner of the code view frame and selecting **View raw**. The essential step is ensuring the URL in your browser bar starts with `raw.githubusercontent.com` before copying it into `wget`.

### Module 8 Help

* **The git clone command says the folder already exists:** If you ran the command twice, it will refuse to overwrite an existing folder. Type `rm -rf python-roguelike` to completely wipe out the broken download folder, then try the `git clone` sequence again from the beginning.

### Module 9 Help

* **How do I flash an image using the terminal?:** Open your desktop imager tool while your secondary SD card is plugged into the USB adapter. Select **Raspberry Pi OS (Lite)** under the OS options, select your USB drive under storage, and click **Write**.

### Module 10 Help

* **The screen is blank when I type my password:** This is standard Unix behavior. The terminal completely hides your inputs so no one looking over your shoulder can see how many characters are in your password. Type the password completely and confidently, then press `Enter`.
* **SSH Connection Refused:** Make sure both your Raspberry Pi and your secondary computer are connected to the exact same Wi-Fi network subnet channel.
