"""Small fixed-font recognizer used by the scan preview tool."""
import numpy as np


def recognize(image, templates, priors=None, noise=0.5):
    image = np.asarray(image, dtype=float)
    names = sorted(templates)
    if not names or noise <= 0 or not np.isfinite(image).all():
        raise ValueError('invalid recognition input')
    bank = np.array([templates[n] for n in names], dtype=float)
    if bank.shape[1:] != image.shape:
        raise ValueError('different crop and template shapes')
    p = np.array([1 if priors is None else priors[n] for n in names], dtype=float)
    if (p <= 0).any() or not np.isfinite(p).all():
        raise ValueError('invalid prior')
    p /= p.sum()
    scores = -((bank - image) ** 2).sum(axis=(1, 2)) / (2 * noise ** 2) + np.log(p)
    z = scores.max() + np.log(np.exp(scores - scores.max()).sum())
    return {'log_probabilities': dict(zip(names, (scores-z).tolist())),
            'best': names[int(scores.argmax())]}
