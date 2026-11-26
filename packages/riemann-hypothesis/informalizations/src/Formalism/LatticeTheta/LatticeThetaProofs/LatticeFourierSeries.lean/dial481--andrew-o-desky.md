---
{
  "module": "src/Formalism/LatticeTheta/LatticeThetaProofs/LatticeFourierSeries.lean",
  "declarations": [
    "Formalism.H.lattice_fourier_series"
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

## Fourier expansion of a continuous lattice-periodic function

[Theorem ANT.1182](https://andrewodesky.com/rh/lean/Formalism.H.lattice_fourier_series/)

Let $V$ be a finite-dimensional real inner product space with its Borel sigma-algebra, and let $\Lambda\subset V$ be a discrete full $\mathbb Z$-lattice. Let $G:V\to\mathbb C$ be continuous and $\Lambda$-periodic, and let $D\subset V$ be an additive fundamental domain for $\Lambda$ with respect to Euclidean volume. Define $$\Lambda^*=\{\mu\in V:\langle\mu,\lambda\rangle\in\mathbb Z\ \text{for every }\lambda\in\Lambda\},\qquad c_\mu=\int_D G(y)e^{-2\pi i\langle\mu,y\rangle}\,dy.$$ If $(c_\mu)_{\mu\in\Lambda^*}$ is unconditionally summable, then, for every $x\in V$, $$G(x)=\frac1{\operatorname{covol}(\Lambda)}\sum_{\mu\in\Lambda^*}c_\mu e^{2\pi i\langle\mu,x\rangle}.$$
