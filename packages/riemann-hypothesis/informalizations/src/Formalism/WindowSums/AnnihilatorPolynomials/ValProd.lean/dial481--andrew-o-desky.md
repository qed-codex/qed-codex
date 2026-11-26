---
{
  "module": "src/Formalism/WindowSums/AnnihilatorPolynomials/ValProd.lean",
  "declarations": [
    "Formalism.WindowSums.valProd_of"
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

## Valuations of products of powers of a principal unit

[Theorem PHT.0891](https://andrewodesky.com/rh/lean/Formalism.WindowSums.valProd_of/)

Assume ([Valuation of a nonzero integer power of a principal unit](https://andrewodesky.com/rh/lean/Formalism.WindowSums.arc_ZpowVal/)).

Let $\ell$ be prime, $u\in\mathbb Z_\ell^\times$, and $s\ge1$ an integer such that $v_\ell(u-1)=s$; assume also $s\ge2$ if $\ell=2$. For every $M\in\mathbb N$, $$\prod_{i=1}^M(1-u^i)\ne0,\qquad v_\ell\left(\prod_{i=1}^M(1-u^i)\right)=Ms+v_\ell(M!).$$ For every finite $J\subseteq\mathbb Z\setminus\{0\}$, $$\prod_{j\in J}(1-u^{-j})\ne0,\qquad v_\ell\left(\prod_{j\in J}(1-u^{-j})\right)=|J|s+\sum_{j\in J}v_\ell(j).$$
