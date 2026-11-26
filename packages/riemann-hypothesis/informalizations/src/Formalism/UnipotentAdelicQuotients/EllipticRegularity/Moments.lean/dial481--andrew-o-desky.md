---
{
  "module": "src/Formalism/UnipotentAdelicQuotients/EllipticRegularity/Moments.lean",
  "declarations": [
    "ZetaZeros.D.EllReg.smoothOfSobolevAll"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Smoothness from all Fourier Sobolev bounds

[Theorem ANT.1047](https://andrewodesky.com/rh/lean/ZetaZeros.D.EllReg.smoothOfSobolevAll/)

Let $d\ge0$ and let $g:\mathbb R^d\to\mathbb C$ be continuous with compact support. If, for every integer $s\ge0$, $$\int_{\mathbb R^d}(1+\|\xi\|^2)^s|\widehat g(\xi)|^2\,d\xi<\infty,$$ then $g$ is infinitely differentiable.
