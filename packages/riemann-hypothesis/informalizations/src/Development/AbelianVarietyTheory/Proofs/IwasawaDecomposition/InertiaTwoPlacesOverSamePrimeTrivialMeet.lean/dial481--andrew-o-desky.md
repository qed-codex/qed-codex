---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/InertiaTwoPlacesOverSamePrimeTrivialMeet.lean",
  "declarations": [
    "GlobalTheory.InertiaTwoPlaces.eq_of_mem_Ine_of_mem_Ine"
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

## A nontrivial common inertia element determines a place

[Theorem GC.0690](https://andrewodesky.com/rh/lean/GlobalTheory.InertiaTwoPlaces.eq_of_mem_Ine_of_mem_Ine/)

Let $E$ be a number field, $\Omega$ an algebraic closure of $E$, and $\mathfrak p$ a nonzero prime ideal of $\mathcal O_E$. Let $A,A'\subset\Omega$ be valuation subrings defining places above $\mathfrak p$, and let $I_A,I_{A'}\subset\operatorname{Gal}(\Omega/E)$ be their inertia subgroups. If $\sigma\ne1$ lies in both $I_A$ and $I_{A'}$, then $A=A'$.
