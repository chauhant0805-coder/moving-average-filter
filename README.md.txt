Absolutely. For your **DTSP software project — “Moving Average Filter for Noise Removal”**, here’s a simple, realistic PRD that matches the prototype we've planned.

# Product Requirements Document (PRD)

## 1. Project Title
**Moving Average Filter for Noise Removal**

### Project Type
Software-based Digital Signal Processing (DTSP) project

### Technology
- **Python**
- **NumPy**
- **Matplotlib**
- Audio processing library such as **Pydub / Librosa / SciPy**
- Simple GUI using **Tkinter**

---

## 2. Problem Statement

Audio signals can contain unwanted random variations called **noise**, which can affect the quality and clarity of the signal.

The project aims to develop a simple software tool that adds controlled noise to an audio signal and uses a **Moving Average Filter** to reduce these unwanted fluctuations.

---

## 3. Objective

The main objectives are:

- To understand the effect of noise on an audio signal.
- To simulate different levels of noise.
- To apply a Moving Average Filter to the noisy audio.
- To observe the difference between the original, noisy, and filtered signals.
- To demonstrate how averaging neighboring samples can smooth a signal.

---

## 4. Proposed Solution

The system will use **four preloaded audio samples**:

- 🐦 Birds
- 👏 Clap
- 🎸 Guitar
- 🗣️ FAHH

The user selects an audio sample and a noise level.

The system then:

```text
Original Audio
       ↓
   Add Noise
       ↓
  Noisy Audio
       ↓
Moving Average Filter
       ↓
 Filtered Audio
       ↓
Waveform Comparison
```

The window size will initially be **fixed at 101 samples** so that the user only needs to control the noise level.

---

## 5. Target Users

### Primary Users
- Students studying DSP/DTSP
- Engineering students
- Faculty demonstrating basic filtering concepts

### Secondary Users
- Beginners learning signal processing
- Users interested in basic audio filtering

---

## 6. Functional Requirements

### FR1 — Audio Selection

The system shall allow the user to select one of the four preloaded audio files.

```text
Select Audio:
[ Birds ▼ ]
[ Clap ]
[ Guitar ]
[ FAHH ]
```

---

### FR2 — Noise Level Selection

The system shall provide three noise levels:

- **Low**
- **Medium**
- **High**

Example noise strengths:

```text
Low      → 0.1
Medium   → 0.3
High     → 0.6
```

These values represent the amount of artificial noise added to the signal.

---

### FR3 — Noise Generation

The system shall automatically generate random noise and add it to the selected clean audio.

The user does **not** need to manually create noisy audio files.

```text
Clean Audio + Generated Noise = Noisy Audio
```

---

### FR4 — Moving Average Filtering

The system shall apply a Moving Average Filter to the noisy audio.

The initial fixed window size will be:

**Window Size = 101 samples**

The filter will calculate the average of neighboring samples and move across the signal.

---

### FR5 — Waveform Display

The system shall display:

1. Original audio waveform
2. Noisy audio waveform
3. Filtered audio waveform

This allows the user to visually compare the effect of filtering.

---

### FR6 — Audio Playback

The system should provide playback options:

```text
▶ Play Original
▶ Play Noisy
▶ Play Filtered
```

This allows the user to hear the effect of noise and filtering.

---

## 7. User Interface

Proposed interface:

```text
┌──────────────────────────────────────┐
│   MOVING AVERAGE FILTER              │
│       FOR NOISE REMOVAL              │
├──────────────────────────────────────┤
│                                      │
│  Select Audio:  [ Birds ▼ ]          │
│                                      │
│  Noise Level:   [ Medium ▼ ]         │
│                                      │
│  Window Size:   101 samples          │
│                                      │
│       [ APPLY FILTER ]               │
│                                      │
├──────────────────────────────────────┤
│                                      │
│       WAVEFORM COMPARISON            │
│                                      │
│  Original                            │
│  ─────────────────────────           │
│                                      │
│  Noisy                               │
│  ─────────────────────────           │
│                                      │
│  Filtered                            │
│  ─────────────────────────           │
│                                      │
│ [▶ Original] [▶ Noisy] [▶ Filtered] │
└──────────────────────────────────────┘
```

---

## 8. Technical Workflow

### Step 1 — Load Audio

Load the selected MP3 file and convert it into numerical samples.

### Step 2 — Normalize

Scale the audio samples into a suitable numerical range.

### Step 3 — Generate Noise

Generate random noise based on the selected noise level.

### Step 4 — Add Noise

```text
Noisy Signal = Original Signal + Noise
```

### Step 5 — Apply Moving Average

For a window size of `N = 101`:

\[
y[n]=\frac{1}{N}\sum_{k=0}^{N-1}x[n-k]
\]

The filter averages neighboring samples to reduce rapid fluctuations.

### Step 6 — Display

Plot the original, noisy, and filtered signals.

### Step 7 — Playback

Allow the user to listen to the three versions.

---

## 9. Non-Functional Requirements

### Simplicity
The interface should be easy for a beginner to understand.

### Performance
Filtering should happen within a few seconds for short audio clips.

### Consistency
The same fixed window size should be used for all four audio samples.

### Usability
The user should be able to operate the prototype without entering code.

---

## 10. Expected Output

The expected result is:

```text
Original Audio
      ↓
Clean waveform

Noisy Audio
      ↓
More random fluctuations

Filtered Audio
      ↓
Smoother waveform
```

The filtered audio should show **reduced rapid fluctuations** compared with the noisy signal.

Because a Moving Average Filter is essentially a smoothing/low-pass operation, very large windows may also remove useful high-frequency audio details. Therefore, the project should present the result as **noise reduction/smoothing**, rather than claiming perfect noise removal.

---

## 11. Limitations

- A Moving Average Filter cannot identify noise perfectly.
- It may also remove some useful high-frequency components.
- A fixed window size may not be optimal for every type of audio.
- The project uses artificially generated noise rather than real-world recorded noise.
- The prototype is intended as a demonstration of basic DSP filtering.

---

## 12. Future Scope

Possible future improvements:

- Allow users to change the window size.
- Add more advanced filters such as:
  - Median Filter
  - Butterworth Filter
  - FIR Filter
- Add real-time microphone input.
- Add different types of noise.
- Add quantitative comparison such as **SNR** and **MSE**.
- Compare Moving Average with other filtering techniques.

---

## 13. Success Criteria

The project will be considered successful if:

- The user can select an audio sample.
- The user can select Low/Medium/High noise.
- The system generates the corresponding noisy signal.
- The Moving Average Filter processes the noisy signal.
- Original, noisy, and filtered waveforms are displayed.
- The user can hear the difference between the signals.
- The filtering process can be clearly explained during the DTSP viva.

### One-line project summary

> **A Python-based audio processing tool that demonstrates how a Moving Average Filter can reduce unwanted fluctuations in noisy audio signals through simple sample averaging.**