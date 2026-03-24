import numpy as np

def white_noise(
    duration: float =1.0,
    amplitude: float =0.01,
    sample_rate: int =11000
) -> np.ndarray:
    n_samples = int(duration * sample_rate)

    noise = np.random.uniform(-1, 1, n_samples)

    noise *= amplitude

    return noise
