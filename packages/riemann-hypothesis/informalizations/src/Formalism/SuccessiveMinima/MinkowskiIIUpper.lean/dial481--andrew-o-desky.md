---
{
  "module": "src/Formalism/SuccessiveMinima/MinkowskiIIUpper.lean",
  "declarations": [
    "Formalism.FN.minkowskiIIUpper"
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

## The upper bound in Minkowski's second theorem

[Theorem ANT.1062](https://andrewodesky.com/rh/lean/Formalism.FN.minkowskiIIUpper/)

Let $E$ be a finite-dimensional real normed vector space of dimension $d$, equipped with its Borel measurable structure and an additive Haar measure $\mu$. Let $L\subseteq E$ be a discrete full $\mathbb Z$-lattice. Let $K\subseteq E$ be compact, convex, symmetric under $x\mapsto-x$, with $0$ in its interior. Then $$\mu(K)\prod_{i=1}^d\lambda_i(L,K)\le 2^d\operatorname{covol}_\mu(L).$$
