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

def sine_tone(
        frequency: float =222.0,
        duration: float =5.0,
        amplitude: float =0.01,
        sample_rate: int =8000,
        slide: float = 1
    ) -> np.ndarray:
    n_samples = int(duration * sample_rate)

    time_points = np.linspace(0, duration, n_samples, False)
    sine = np.sin(2 * np.pi * frequency * pow(time_points,slide))

    sine *= amplitude

    # if(EightBit_enabled.get()==1):
    #     for i in range(0, len(sine), 16):
    #         sine[i:i+16] = sine[i]
    return sine

def apply_envelope(sound: np.array,
                    adsr:list,
                    smaple_rate: int=44100) ->np.array:
    sound = sound.copy()

    attack_samples = int(adsr[0] * smaple_rate)
    decay_samples = int(adsr[1] * smaple_rate)
    release_samples = int(adsr[3] * smaple_rate)
    sustain_samples = len(sound) - (attack_samples + decay_samples + release_samples)

    sound[:attack_samples] *= np.linspace(0, 1, attack_samples)

    sound[attack_samples:attack_samples + decay_samples] *= np.linspace(1, adsr[2], decay_samples)

    sound[attack_samples + decay_samples:attack_samples + decay_samples + sustain_samples] *= adsr[2]

    sound[attack_samples + decay_samples + sustain_samples:] *= np.linspace(adsr[2], 0, release_samples)
    return sound