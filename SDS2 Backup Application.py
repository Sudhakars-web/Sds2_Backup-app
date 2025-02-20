import pyautogui
import os
import time
from datetime import datetime
import pygetwindow as gw
import tkinter as tk
from tkinter import ttk
import schedule
from tkinter import messagebox
import threading
import sys

def maximize_sds_window(job_name):
    # Define the possible versions and stations
    versions = ["2022", "2022i", "2023", "2023i", "2024"]
    stations = ["Detailing", "Modeling", "Drafting","Viewer"]

    # Try all possible combinations of version and station
    for version in versions:
        for station in stations:
            # Get the window title based on the version, station, and job name
            window_title = f"Home - SDS2 {version} {station} - For North America - {job_name}"

            # Get all open windows
            windows = gw.getWindowsWithTitle(window_title)

            # Find the window in the taskbar
            my_app_window = None
            if windows:
                my_app_window = windows[0]

            # Maximize the window if found
            if my_app_window:
                my_app_window.maximize()
                my_app_window.activate()
                time.sleep(1)  # Give it a moment to maximize

                # Move the window to the primary screen
                primary_screen_x = 0
                primary_screen_y = 0
                my_app_window.moveTo(primary_screen_x, primary_screen_y)

                # Ensure it is maximized again
                time.sleep(1)  # Give it a moment to move
                my_app_window.maximize()
                return  # Exit the function after maximizing the window

    # If the window is not found after iterating through all combinations
    messagebox.showwarning("Warning",f"The Home window for the job '{job_name}' could not be found.")
    sys.exit()  # Abort the program

def run_remaining_program_Dark_pro(job_name, interval):

    try:
        # Get the current date
        current_date = datetime.now()

        # Create the folder name in the desired format
        folder_name = f"{current_date.day}_{current_date.month}_{current_date.year}"

        # Create the folder path for the date folder
        date_folder_path = os.path.join("D:\\Backup\\", folder_name)

        # Create the date folder
        os.makedirs(date_folder_path, exist_ok=True)

        # Create the job name folder inside the date folder
        job_folder_path = os.path.join(date_folder_path, job_name)
        os.makedirs(job_folder_path, exist_ok=True)

        # Path to the directory you want to paste
        directory_path = job_folder_path

        pyautogui.sleep(1)

        # List of possible image names for "Export" and "Project transfer"
        p = pyautogui.locateCenterOnScreen("Project transfer_D.png")
        pyautogui.moveTo(p, duration=0)
        pyautogui.leftClick()

        pyautogui.sleep(15)

        # Press the left arrow key four times
        for _ in range(3):
            pyautogui.press('tab')

        # Paste the directory path
        pyautogui.typewrite(directory_path, interval=0)

        # Press the left arrow key four times
        for _ in range(2):
            pyautogui.press('tab')

        # Get the current time
        current_time = datetime.now().strftime("%H_%M")

        # Press the End button
        pyautogui.press('end')

        # Press the left arrow key four times
        for _ in range(4):
            pyautogui.press('left')

        # Append the current time
        pyautogui.typewrite(f"_{current_time}", interval=0)

        pyautogui.sleep(1)

        # Press the left arrow key four times
        for _ in range(7):
            pyautogui.press('tab')

        pyautogui.press('enter')

    except:
        pass

def run_remaining_program_Dark_exp(job_name, interval):

    try:
        # Get the current date
        current_date = datetime.now()

        # Create the folder name in the desired format
        folder_name = f"{current_date.day}_{current_date.month}_{current_date.year}"

        # Create the folder path for the date folder
        date_folder_path = os.path.join("D:\\Backup\\", folder_name)

        # Create the date folder
        os.makedirs(date_folder_path, exist_ok=True)

        # Create the job name folder inside the date folder
        job_folder_path = os.path.join(date_folder_path, job_name)
        os.makedirs(job_folder_path, exist_ok=True)

        # Path to the directory you want to paste
        directory_path = job_folder_path

        pyautogui.sleep(1)

        ex = pyautogui.locateCenterOnScreen("Export_D.png")
        pyautogui.moveTo(ex, duration=0)
        pyautogui.leftClick()
        p = pyautogui.locateCenterOnScreen("Project transfer_D.png")
        pyautogui.moveTo(p, duration=0)
        pyautogui.leftClick()

        pyautogui.sleep(15)

        # Press the left arrow key four times
        for _ in range(3):
            pyautogui.press('tab')

        # Paste the directory path
        pyautogui.typewrite(directory_path, interval=0)

        # Press the left arrow key four times
        for _ in range(2):
            pyautogui.press('tab')

        # Get the current time
        current_time = datetime.now().strftime("%H_%M")

        # Press the End button
        pyautogui.press('end')

        # Press the left arrow key four times
        for _ in range(4):
            pyautogui.press('left')

        # Append the current time
        pyautogui.typewrite(f"_{current_time}", interval=0)

        pyautogui.sleep(1)

        # Press the left arrow key four times
        for _ in range(7):
            pyautogui.press('tab')

        pyautogui.press('enter')

    except:
        pass

def run_remaining_program_Light_pro(job_name, interval):

    try:
        # Get the current date
        current_date = datetime.now()

        # Create the folder name in the desired format
        folder_name = f"{current_date.day}_{current_date.month}_{current_date.year}"

        # Create the folder path for the date folder
        date_folder_path = os.path.join("D:\\Backup\\", folder_name)

        # Create the date folder
        os.makedirs(date_folder_path, exist_ok=True)

        # Create the job name folder inside the date folder
        job_folder_path = os.path.join(date_folder_path, job_name)
        os.makedirs(job_folder_path, exist_ok=True)

        # Path to the directory you want to paste
        directory_path = job_folder_path

        pyautogui.sleep(1)

        # List of possible image names for "Export" and "Project transfer"
        p = pyautogui.locateCenterOnScreen("Lpt.png",confidence=0.99)
        pyautogui.moveTo(p, duration=0)
        pyautogui.leftClick()

        pyautogui.sleep(15)

        # Press the left arrow key four times
        for _ in range(3):
            pyautogui.press('tab')

        # Paste the directory path
        pyautogui.typewrite(directory_path, interval=0)

        # Press the left arrow key four times
        for _ in range(2):
            pyautogui.press('tab')

        # Get the current time
        current_time = datetime.now().strftime("%H_%M")

        # Press the End button
        pyautogui.press('end')

        # Press the left arrow key four times
        for _ in range(4):
            pyautogui.press('left')

        # Append the current time
        pyautogui.typewrite(f"_{current_time}", interval=0)

        pyautogui.sleep(1)

        # Press the left arrow key four times
        for _ in range(7):
            pyautogui.press('tab')

        pyautogui.press('enter')

    except:
        pass

def run_remaining_program_Light_exp(job_name, interval):

    try:
        # Get the current date
        current_date = datetime.now()

        # Create the folder name in the desired format
        folder_name = f"{current_date.day}_{current_date.month}_{current_date.year}"

        # Create the folder path for the date folder
        date_folder_path = os.path.join("D:\\Backup\\", folder_name)

        # Create the date folder
        os.makedirs(date_folder_path, exist_ok=True)

        # Create the job name folder inside the date folder
        job_folder_path = os.path.join(date_folder_path, job_name)
        os.makedirs(job_folder_path, exist_ok=True)

        # Path to the directory you want to paste
        directory_path = job_folder_path

        pyautogui.sleep(1)

        ex = pyautogui.locateCenterOnScreen("exl.png",confidence=0.99)
        pyautogui.moveTo(ex, duration=0)
        pyautogui.leftClick()
        p = pyautogui.locateCenterOnScreen("Lpt.png",confidence=0.99)
        pyautogui.moveTo(p, duration=0)
        pyautogui.leftClick()

        pyautogui.sleep(15)

        # Press the left arrow key four times
        for _ in range(3):
            pyautogui.press('tab')

        # Paste the directory path
        pyautogui.typewrite(directory_path, interval=0)

        # Press the left arrow key four times
        for _ in range(2):
            pyautogui.press('tab')

        # Get the current time
        current_time = datetime.now().strftime("%H_%M")

        # Press the End button
        pyautogui.press('end')

        # Press the left arrow key four times
        for _ in range(4):
            pyautogui.press('left')

        # Append the current time
        pyautogui.typewrite(f"_{current_time}", interval=0)

        pyautogui.sleep(1)

        # Press the left arrow key four times
        for _ in range(7):
            pyautogui.press('tab')

        pyautogui.press('enter')

    except:
        pass

def schedule_backup_job(job_name, interval):
    # Call the scheduled_backup function for dark mode
    maximize_sds_window(job_name)
    messagebox.showwarning("Backup Running", "Scheduled backup is running, please do not interrupt.")
    run_remaining_program_Dark_pro(job_name, interval)
    run_remaining_program_Dark_exp(job_name, interval)
    run_remaining_program_Light_pro(job_name, interval)
    run_remaining_program_Light_exp(job_name, interval)

def open_window():
    selected_job_name = job_name_var.get()
    interval = interval_var.get()

    # Schedule the backup job
    schedule_backup_job(selected_job_name, interval)

    if interval in range(0,30):
        messagebox.showwarning("Backup warning", "Provide minimum of 30mins interval else the backup will run only once")
        sys.exit()
    else:
        # Schedule the backup job to run at the specified interval
        schedule.every(interval).minutes.do(schedule_backup_job, selected_job_name, interval)

        # Start the scheduling thread
        threading.Thread(target=run_scheduler, daemon=True).start()

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Create the root window
root = tk.Tk()
root.title("SDS/2 Backup Application")

# Set the window size
window_width = 310
window_height = 300

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to place the window in the right corner
position_right = screen_width - window_width - 10
position_down = screen_height - window_height - 10

# Set the geometry of the window (width x height + x_offset + y_offset)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

# Create the widgets
job_name_var = tk.StringVar()
interval_var = tk.IntVar()

# Set the icon of the window
icon_path = "Backup.ico"  # Replace with the path to your .ico file
root.iconbitmap(icon_path)

job_name_label = ttk.Label(root, text="Enter Job Name:")
job_name_label.pack(padx=10, pady=10)

job_name_entry = ttk.Entry(root, textvariable=job_name_var)
job_name_entry.pack(padx=10, pady=10)

interval_label = ttk.Label(root, text="Interval (in minutes):")
interval_label.pack(padx=10, pady=10)

interval_entry = ttk.Entry(root, textvariable=interval_var)
interval_entry.pack(padx=10, pady=10)

open_button = ttk.Button(root, text="Backup", command=open_window)
open_button.pack(padx=10, pady=10)

# Run the application
root.mainloop()
