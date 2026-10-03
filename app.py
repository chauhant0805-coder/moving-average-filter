import os
import glob
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import soundfile as sf
import sounddevice as sd

class MovingAverageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Average Filter - Noise Removal Prototype")
        self.root.geometry("1000x800")

        # Base names of the files
        self.audio_names = ["Birds", "Clap", "Guitar", "FAHH"]

        self.sr = None
        self.original_audio = None
        self.noisy_audio = None
        self.filtered_audio = None

        self.setup_ui()

    def find_audio_file(self, selected_name):
        """ Dynamically finds the audio file regardless of case or extension """
        # Look in both "audio samples" and "audio_samples" folders
        possible_folders = ["audio samples", "audio_samples", "."]
        
        for folder in possible_folders:
            if os.path.exists(folder):
                for file in os.listdir(folder):
                    # Check if file name matches without case sensitivity
                    if selected_name.lower() in file.lower():
                        return os.path.join(folder, file)
        return None

    def setup_ui(self):
        # 1. Controls Frame
        control_frame = ttk.LabelFrame(self.root, text=" Filter Controls ")
        control_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(control_frame, text="Select Audio:").grid(row=0, column=0, padx=5, pady=5)
        self.audio_var = tk.StringVar(value="Birds")
        audio_menu = ttk.Combobox(control_frame, textvariable=self.audio_var, values=self.audio_names, state="readonly")
        audio_menu.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(control_frame, text="Noise Level:").grid(row=0, column=2, padx=5, pady=5)
        self.noise_var = tk.StringVar(value="Medium")
        noise_menu = ttk.Combobox(control_frame, textvariable=self.noise_var, values=["Low", "Medium", "High"], state="readonly")
        noise_menu.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(control_frame, text="Window: 101 Samples (Fixed)").grid(row=0, column=4, padx=10, pady=5)

        apply_btn = ttk.Button(control_frame, text="Apply Filter", command=self.process_audio)
        apply_btn.grid(row=0, column=5, padx=10, pady=5)

        # 2. Playback Frame
        play_frame = ttk.LabelFrame(self.root, text=" Audio Playback ")
        play_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(play_frame, text="▶ Play Original", command=lambda: self.play_signal(self.original_audio)).pack(side="left", padx=10, pady=5)
        ttk.Button(play_frame, text="▶ Play Noisy", command=lambda: self.play_signal(self.noisy_audio)).pack(side="left", padx=10, pady=5)
        ttk.Button(play_frame, text="▶ Play Filtered", command=lambda: self.play_signal(self.filtered_audio)).pack(side="left", padx=10, pady=5)
        ttk.Button(play_frame, text="⏹ Stop", command=self.stop_audio).pack(side="left", padx=10, pady=5)

        # 3. Graph Display Area
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
        self.fig.tight_layout(pad=3.0)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=5)
        self.reset_plots()

    def reset_plots(self):
        titles = ["Original Audio Waveform", "Noisy Audio Waveform", "Filtered Audio Waveform (N=101)"]
        for ax, title in zip([self.ax1, self.ax2, self.ax3], titles):
            ax.clear()
            ax.set_title(title)
            ax.set_ylabel("Amplitude")
            ax.grid(True)
        self.ax3.set_xlabel("Sample Index")
        self.canvas.draw()

    def process_audio(self):
        selected_audio = self.audio_var.get()
        file_path = self.find_audio_file(selected_audio)

        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("Error", f"Could not find audio file for '{selected_audio}' in folder.")
            return

        audio_data, self.sr = sf.read(file_path)
        if len(audio_data.shape) > 1:
            audio_data = np.mean(audio_data, axis=1)

        max_val = np.max(np.abs(audio_data))
        self.original_audio = audio_data / max_val if max_val > 0 else audio_data

        noise_levels = {"Low": 0.05, "Medium": 0.15, "High": 0.30}
        sigma = noise_levels[self.noise_var.get()]
        noise = np.random.normal(0, sigma, size=len(self.original_audio))
        self.noisy_audio = self.original_audio + noise

        N = 101
        window = np.ones(N) / N
        self.filtered_audio = np.convolve(self.noisy_audio, window, mode='same')

        self.reset_plots()
        self.ax1.plot(self.original_audio, color='blue', alpha=0.7)
        self.ax2.plot(self.noisy_audio, color='red', alpha=0.7)
        self.ax3.plot(self.filtered_audio, color='green', alpha=0.7)
        self.canvas.draw()

    def play_signal(self, audio_data):
        if audio_data is not None:
            sd.stop()
            sd.play(audio_data, self.sr)
        else:
            messagebox.showwarning("Warning", "Click 'Apply Filter' first to generate audio.")

    def stop_audio(self):
        sd.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MovingAverageApp(root)
    root.mainloop()
