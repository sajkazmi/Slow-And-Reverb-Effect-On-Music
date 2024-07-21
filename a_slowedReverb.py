import tkinter as tk
from tkinter import filedialog, ttk  # Use ttk for improved styling
import librosa
import soundfile as sf
from ttkbootstrap import Style

style = Style(theme='darkly') 

# Create the main window
root = tk.Tk()
root.title("Slow Down Music with Reverb")

# Header frame
header_frame = tk.Frame(root, bd=5, relief='groove')
header_frame.pack(fill='x')

app_name_label = tk.Label(header_frame, text="Audio Manipulator", font=('Arial', 20))
app_name_label.pack(pady=10)

# Input section frame
input_frame = tk.Frame(root, bd=5, relief='groove')
input_frame.pack(fill='x', pady=10)

input_label = tk.Label(input_frame, text="Enter MP3 file name:")
input_label.pack(side='left')

input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(side='left')

browse_button = ttk.Button(input_frame, text="Browse", command=lambda: input_entry.insert(0, filedialog.askopenfilename()))
browse_button.pack(side='left')

# Control section frame
control_frame = tk.Frame(root, bd=5, relief='groove')
control_frame.pack(fill='x', pady=10)

speed_label = tk.Label(control_frame, text="Slowdown Speed:")
speed_label.pack(side='left')

speed_slider = ttk.Scale(control_frame, from_=0.5, to=1.0, orient='horizontal', value=0.77)  # Allow adjusting slowdown
speed_slider.pack(side='left')

reverb_label = tk.Label(control_frame, text="Reverb Time:")
reverb_label.pack(side='left')

reverb_slider = ttk.Scale(control_frame, from_=0.5, to=2.0, orient='horizontal', value=1.5)  # Adjust reverb time
reverb_slider.pack(side='left')

# Output format selection (optional)
output_format_label = tk.Label(control_frame, text="Output Format:")
output_format_label.pack(side='left')

output_format_dropdown = ttk.Combobox(control_frame, values=["mp3", "wav"])  # Offer format choices
output_format_dropdown.pack(side='left')

# Action button
action_button = ttk.Button(control_frame, text="Slow Down and Save", command=lambda: slow_down_and_save(speed_slider.get(), reverb_slider.get(), output_format_dropdown.get()))
action_button.pack(side='left')

# Progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', length=200)
progress_bar.pack(pady=10)

# Status label
status_label = ttk.Label(root, text="")
status_label.pack()

def slow_down_and_save(speed, reverb_time, output_format):
    input_file = input_entry.get()
    output_file = input_file.split('.')[0] + "_slowed_reverb." + output_format  # Use chosen format
    try:
        slow_down_music(input_file, output_file, speed, reverb_time)
        status_label.config(text="Slowed audio saved successfully!")
        progress_bar.stop()
    except Exception as e:
        status_label.config(text="Error: " + str(e))

def slow_down_music(input_file, output_file, speed, reverb_time):
    y, sr = librosa.load(input_file)
    y_slow = librosa.effects.time_stretch(y, rate=speed)
    # Add progress bar update logic here
    sf.write(output_file, y_slow, 16000)  # Update sample rate as needed

# Show the window
root.mainloop()
