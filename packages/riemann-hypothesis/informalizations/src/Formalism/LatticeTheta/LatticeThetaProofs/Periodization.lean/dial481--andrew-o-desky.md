---
{
  "module": "src/Formalism/LatticeTheta/LatticeThetaProofs/Periodization.lean",
  "declarations": [
    "Formalism.H.poisson_periodization"
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

## Continuous periodization of a decaying function

[Theorem ANT.1221](https://andrewodesky.com/rh/lean/Formalism.H.poisson_periodization/)

Let $V$ be a finite-dimensional real inner product space with its Borel measurable structure, and let $\Lambda\subset V$ be a discrete full $\mathbb Z$-lattice. Let $f:V\to\mathbb C$ be continuous and suppose $$f(x)=O(\|x\|^{-b})\quad\text{outside compact sets},\qquad b>\dim_{\mathbb R}V.$$ Then $f$ is integrable, $\sum_{\lambda\in\Lambda}f(\lambda+x)$ is absolutely convergent for every $x\in V$, and the resulting function $$P_f(x)=\sum_{\lambda\in\Lambda}f(\lambda+x)$$ is continuous and satisfies $P_f(x+\lambda_0)=P_f(x)$ for all $\lambda_0\in\Lambda$.
