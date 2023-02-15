import datetime
import pygame
import tkinter as tk
from tkinter import messagebox


class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")

        # Create and pack the time label
        self.time_label = tk.Label(self.master, text="", font=("Arial", 64))
        self.time_label.pack()

        # Create and pack the entry fields for the alarm time
        self.hour_entry = tk.Entry(self.master, width=2, font=("Arial", 24))
        self.hour_entry.insert(0, "00")
        self.hour_entry.pack(side="left")
        self.colon_label1 = tk.Label(self.master, text=":", font=("Arial", 24))
        self.colon_label1.pack(side="left")
        self.minute_entry = tk.Entry(self.master, width=2, font=("Arial", 24))
        self.minute_entry.insert(0, "00")
        self.minute_entry.pack(side="left")
        self.colon_label2 = tk.Label(self.master, text=":", font=("Arial", 24))
        self.colon_label2.pack(side="left")
        self.second_entry = tk.Entry(self.master, width=2, font=("Arial", 24))
        self.second_entry.insert(0, "00")
        self.second_entry.pack(side="left")

        # Create and pack the button to set the alarm
        self.set_button = tk.Button(self.master, text="Set Alarm", font=(
            "Arial", 20), command=self.set_alarm, bg="gray", fg="white", activebackground="black", activeforeground="white")
        self.set_button.pack(pady=10)

        # Initialize the alarm time to None
        self.alarm_time = None

        # Load the wake-up song
        pygame.mixer.init()
        self.wakeup_music = pygame.mixer.Sound("wakeup_music.wav")

        # Update the time label every second
        self.update_time()

    def set_alarm(self):
        # Get the current time and date
        now = datetime.datetime.now()

        # Get the alarm time from the entry fields
        alarm_hour = int(self.hour_entry.get())
        alarm_minute = int(self.minute_entry.get())
        alarm_second = int(self.second_entry.get())

        # Create a new datetime object for the alarm time
        alarm_time = datetime.datetime(
            now.year, now.month, now.day, alarm_hour, alarm_minute, alarm_second)

        # If the alarm time is in the past, set it for tomorrow
        if alarm_time < now:
            alarm_time = alarm_time + datetime.timedelta(days=1)

        # Set the alarm time and update the button text
        self.alarm_time = alarm_time
        self.set_button.configure(text="Alarm set for {:02d}:{:02d}:{:02d}.".format(
            alarm_hour, alarm_minute, alarm_second))

    def update_time(self):
        # Update the time label with the current time
        self.time_label.configure(
            text=datetime.datetime.now().strftime("%H:%M:%S"))

        # If an alarm time is set, check if it's time to ring the alarm
        if self.alarm_time is not None:
            if datetime.datetime.now() >= self.alarm_time:
                self.ring_alarm()

        # Schedule the update function to run again in 1 second
        self.master.after(1000, self.update_time)

    def ring_alarm(self):
        # Play the wake-up music
        self.wakeup_music.play()

        # Open a message box to indicate that the alarm has rung
        messagebox.showinfo("Alarm", "Time to wake up!")

        # Clear the alarm time and update the button text
        self.alarm_time = None
        self.set_button.configure(text="Set")


# Create the main window and start the main loop
root = tk.Tk()
app = AlarmClock(root)
root.mainloop()
