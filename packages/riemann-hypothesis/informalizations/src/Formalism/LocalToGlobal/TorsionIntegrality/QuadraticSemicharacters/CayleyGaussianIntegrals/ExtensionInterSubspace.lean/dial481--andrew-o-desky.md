---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/CayleyGaussianIntegrals/ExtensionInterSubspace.lean",
  "declarations": [
    "Formalism.L2.Th1.H.exp_series_entire"
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

## An entire function from a normally convergent exponential series

[Theorem ALG.0835](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.exp_series_entire/)

Let $V$ be a complex normed vector space, $I$ any index set, $c_i\in\mathbb C$, and $\ell_i:V\to\mathbb C$ continuous complex-linear functionals. Assume that for every $r\in\mathbb R$, $$\sum_{i\in I}|c_i|e^{r\|\ell_i\|}<\infty.$$ Then $$f(z)=\sum_{i\in I}c_i e^{\ell_i(z)}$$ is complex analytic in a neighborhood of every point of $V$.
