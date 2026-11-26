---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsUniquePureTensorRestrictedFamily.lean",
  "declarations": [
    "GlobalTheory.PureTensorExists.existsUnique_isPure"
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

## A restricted theta tensor characterized by Heisenberg coefficients

[Theorem THETA.1037](https://andrewodesky.com/rh/lean/GlobalTheory.PureTensorExists.existsUnique_isPure/)

Work in the source's full arithmetic theta datum over a CM extension $E/F$. Let $S,T$ be its Hermitian spaces. Fix its additive character and archimedean embeddings, Cartan involutions on both spaces, self-dual integral lattices $\Lambda_S,\Lambda_T$, and a simultaneous lattice and Fock vacuum $f_0$ in the theta-function model $\mathcal H$. Give the adelic Heisenberg parameter space $W$ a Haar measure and a fundamental domain $\mathcal F$ for its rational subgroup, with covolume one. Write $$\langle f,g\rangle=\int_{\mathcal F}f(w)\overline{g(w)}\,d\nu(w)$$ and $H(w)$ for the specified Heisenberg translation.

For every place $p$, let $x_p\in\mathcal H$ be a vector which is the lattice vacuum at every other finite place and the Fock vacuum at every other infinite place. Assume $x_p=f_0$ outside a finite set. There is a unique $f\in\mathcal H$ such that, for every $w\in W$, all but finitely many factors below equal $1$, and $$\langle f,H(w)f_0\rangle=\prod_p\langle x_p,H(w_p)f_0\rangle.$$
