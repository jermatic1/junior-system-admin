# 🤖 HARDWARE TRACK: LEROBOT SO-101 FIELD OPS

## 🦾 MODULE 1: REMOTE SHELL & TELEOPERATION

**Objective:** SSH into the Jetson control computer, discover the robot USB serial ports, run a safe status check, and start leader→follower teleoperation—without touching calibration.

### 📜 Tech Briefing

The **SO-101** is a dual-arm robot kit: a **leader** arm you move by hand, and a **follower** arm that copies those motions. Both arms talk to a small computer (an **NVIDIA Jetson**) over USB serial adapters. Control software from Hugging Face called **LeRobot** reads joint positions from the leader and sends matching commands to the follower.

You will not sit at the Jetson with a keyboard. You will use **SSH (Secure Shell)** from your own machine to open an encrypted remote terminal on the Jetson, then run the pre-built scripts in `~/lerobot/`.

**Serial ports** are the Linux device paths that map each USB adapter to a file under `/dev/`. Stable names live under `/dev/serial/by-id/` so they survive reboots better than `/dev/ttyACM0`. LeRobot also ships `lerobot-find-port` to help you match which cable is which arm.

### ⛔ RESTRICTED ZONE — DO NOT CALIBRATE

Calibration teaches the software the physical range of each joint. **These arms are already calibrated.** Running calibration again can overwrite good settings and make the robot move incorrectly or unsafely.

| Script / command | Status |
| ---------------- | ------ |
| `~/lerobot/calibrate-follower.sh` | **OFF LIMITS** — do not run |
| `~/lerobot/calibrate-leader.sh` | **OFF LIMITS** — do not run |
| `lerobot-calibrate` | **OFF LIMITS** — do not run |
| `lerobot-setup-motors` | **OFF LIMITS** — Dad-only hardware setup |

If a command ever asks you to move joints through their full range for calibration, **stop** (`Ctrl+C`) and get Dad.

### 🚀 Main Mission

Replace the placeholders before you start:

- `YOUR_USER` — your account name on the Jetson
- `JETSON_HOST` — the Jetson hostname or IP (ask Dad if you do not know it)

1. **Pre-flight (physical):** Confirm both arms are powered, both USB cables are plugged into the Jetson, and the workspace is clear of people, pets, and fragile objects. Keep hands clear of the follower arm once teleoperation starts—it will move.
2. **Remote Handshake:** On your local computer, open a Terminal and connect:
   ```bash
   ssh YOUR_USER@JETSON_HOST
   ```
   Enter your password when prompted. You should land in a shell on the Jetson (the prompt will look different from your local machine).
3. **Home Base Check:** Confirm you are in your home directory and the LeRobot scripts exist:
   ```bash
   whoami
   hostname
   ls ~/lerobot
   ```
   You should see at least `teleoperate.sh`. You may also see the calibrate scripts—**do not run those.**
4. **Serial Port Discovery:** List the stable USB serial device paths:
   ```bash
   ls -l /dev/serial/by-id/
   ```
   Write down the two long names that look like `usb-1a86_USB_Single_Serial_...`. These are the leader and follower adapters.
5. **LeRobot Port Finder (optional probe):** If you want practice matching a cable to a port, run:
   ```bash
   cd ~/lerobot
   uv run lerobot-find-port
   ```
   Follow the on-screen prompts (it may ask you to unplug one USB cable briefly, then plug it back in). When finished, both cables must be reconnected before teleoperation.
6. **Status Snapshot:** Print LeRobot environment info:
   ```bash
   uv run lerobot-info
   ```
   Skim the output. You do not need to understand every line—just confirm the command runs without a crash. If it fails, copy the error and show Dad.
7. **Launch Teleoperation:** Start the pre-wired control script:
   ```bash
   cd ~/lerobot
   ./teleoperate.sh
   ```
   Wait until the program reports it is connected / running. Slowly move the **leader** arm. The **follower** should mirror your motion. Try small, smooth moves first (base rotation, elbow, gripper).
8. **Clean Shutdown:** When you are done, return to the terminal and press `Ctrl+C` to stop teleoperation. Confirm the follower stops responding. Type `exit` to close the SSH session.

### 🎮 Side Quest

Still on the Jetson (or reconnect with SSH), inspect the wrapper so you see what the long LeRobot command looks like under the hood:

```bash
cd ~/lerobot
ls -l
nano teleoperate.sh
```

Find these pieces inside the file:

- `lerobot-teleoperate` — the real program name
- `--robot.type=so101_follower` and `--teleop.type=so101_leader` — which arm roles are used
- `--robot.port=...` and `--teleop.port=...` — the serial paths you discovered earlier
- `--robot.id=...` and `--teleop.id=...` — names tied to the **existing** calibration files (do not change these)

Exit nano without saving unless Dad asked you to edit something (`Ctrl+X`).

**Bonus report for Dad:** Which `by-id` path is the follower, and which is the leader? How did you tell?

### 🆘 Troubleshooting

| Symptom | What to try |
| ------- | ----------- |
| `ssh: Could not resolve hostname` | Check `JETSON_HOST` spelling; try the IP address instead; confirm you are on the same Wi‑Fi/LAN |
| `Permission denied` | Wrong username or password; confirm `YOUR_USER` |
| `ls: cannot access '/dev/serial/by-id/'` | USB cables unplugged, or arms unpowered; reseat cables and rerun `ls` |
| Teleoperate cannot open the port | Another process may still be using the arms—press `Ctrl+C` in any old session; unplug/replug USB only if Dad approves |
| Follower does not move | Confirm both power supplies are on; confirm you are moving the **leader**; stop with `Ctrl+C` and get Dad if motors sound wrong |
| Anything about calibration / setup motors | **Stop immediately.** Do not continue. Get Dad. |

### 📚 Reference (read-only)

- LeRobot project: `https://github.com/huggingface/lerobot`
- SO-101 docs: `https://huggingface.co/docs/lerobot/en/so101`
- Teleoperation guide: `https://huggingface.co/docs/lerobot/en/il_robots`
