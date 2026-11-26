---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/OneSubTwoOmegaSq.lean",
  "declarations": [
    "GlobalTheory.HondaCM3.cm3"
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

## An integral height-two parameter for an inert CM elliptic model

[Theorem PHT.0091](https://andrewodesky.com/rh/lean/GlobalTheory.HondaCM3.cm3/)

Use the notation of ([Weierstrass series and good CM models](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.CM.cW/)). Let $d$ be a nonnegative squarefree integer with $d\equiv3\pmod4$, and let $\Lambda\subset\mathbb C$ be a rank-two period lattice stable under multiplication by $\omega_d$. Let $\ell\ge5$ be prime, with $\ell\nmid d$ and $X^2=-d$ having no solution modulo $\ell$. Choose a field isomorphism $\iota:\mathbb C\simeq\mathbb C_\ell$ and a good model $g_2,g_3$ of $(\Lambda,\iota)$ at $\ell$. There is $\epsilon\in K^{\mathrm{ur}}_\ell$ with $|\epsilon|_\ell=1$ such that every coefficient of $$U\left(\epsilon\sum_{j\ge0}\frac{T^{\ell^{2j}}}{\ell^j}\right)$$ belongs to $K^{\mathrm{ur}}_\ell$ and has $\ell$-adic absolute value at most one.
