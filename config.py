"""Simulacion visual de diferentes tipos de ruido con Matplotlib."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


# Parametros de la adquisicion simulada.
SAMPLING_RATE = 1000
V_REF = 3.3
DURATION_SECONDS = 2.0
RANDOM_SEED = 42


def generate_noise_signals(
    duration: float = DURATION_SECONDS,
    sampling_rate: int = SAMPLING_RATE,
    seed: int = RANDOM_SEED,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Genera tiempo, ruido blanco, ruido rosa aproximado y ruido combinado."""
    if duration <= 0:
        raise ValueError("duration debe ser mayor que cero")
    if sampling_rate <= 0:
        raise ValueError("sampling_rate debe ser mayor que cero")

    generator = np.random.default_rng(seed)
    sample_count = int(duration * sampling_rate)
    time = np.arange(sample_count) / sampling_rate

    white_noise = generator.normal(0, 1, sample_count)

    # Suavizar ruido blanco produce una aproximacion sencilla al ruido rosa.
    pink_noise = np.cumsum(generator.normal(0, 0.08, sample_count))
    pink_noise -= np.mean(pink_noise)
    pink_noise /= np.std(pink_noise)

    interference = 0.7 * np.sin(2 * np.pi * 50 * time)
    combined_noise = 0.35 * white_noise + 0.25 * pink_noise + interference

    return time, white_noise, pink_noise, combined_noise


def plot_noise_signals() -> None:
    """Genera y muestra una figura comparando las senales de ruido."""
    time, white_noise, pink_noise, combined_noise = generate_noise_signals()

    figure, axes = plt.subplots(3, 1, figsize=(11, 8), sharex=True)
    figure.suptitle("Simulacion de senales de ruido", fontsize=16, fontweight="bold")

    plots = (
        (axes[0], white_noise, "Ruido blanco", "tab:blue"),
        (axes[1], pink_noise, "Ruido rosa aproximado", "tab:orange"),
        (axes[2], combined_noise, "Ruido combinado con interferencia de 50 Hz", "tab:green"),
    )

    for axis, signal, title, color in plots:
        axis.plot(time, signal, color=color, linewidth=0.8)
        axis.set_title(title, loc="left", fontsize=11)
        axis.set_ylabel("Amplitud")
        axis.grid(True, alpha=0.25)

    axes[-1].set_xlabel("Tiempo (s)")
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_noise_signals()
