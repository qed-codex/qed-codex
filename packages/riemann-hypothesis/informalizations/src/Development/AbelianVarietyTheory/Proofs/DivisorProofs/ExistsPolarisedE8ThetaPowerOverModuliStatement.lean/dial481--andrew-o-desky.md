---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPolarisedE8ThetaPowerOverModuliStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_polarised_E8ThetaPower_over_moduli"
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

## A polarized eightfold power over a Siegel moduli family

[Theorem AV.1400](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_polarised_E8ThetaPower_over_moduli/)

Let $g\ge1$ and let $n\ge3$ be odd. Fix the source's Siegel moduli-family data of dimension $g$ and level $n$ over its cyclotomic base with $n$ inverted, with base scheme $X$, universal principally polarized abelian scheme $A/X$, and its chosen biextension line bundle $\mathcal P$ on $A\times_XA$. Let $W\in M_8(\mathbb Z)$ satisfy $$W+W^{\mathsf T}>0,\qquad\det(W+W^{\mathsf T})=1.$$ There is a principally polarized abelian scheme $B/X$ of relative dimension $8g$, identified as a group scheme with $A^8$, with polarization line bundle $$L\simeq\bigotimes_{a,b=1}^8(p_a,p_b)^*\mathcal P^{\otimes W_{ab}},$$ and a trivialization of $L$ along the identity section. Moreover $B$ has group endomorphisms $w,w'$ whose pointwise sum is the identity and such that $$L\simeq\Delta_L(\operatorname{id},w),\qquad\Delta_L(wp_1,p_2)\simeq\Delta_L(p_1,w'p_2),$$ where $\Delta_L(f,h)=(f+h)^*L\otimes f^*L^{-1}\otimes h^*L^{-1}\otimes0^*L$.
