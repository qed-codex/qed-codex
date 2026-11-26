---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTorsionFreeSurjZmod.lean",
  "declarations": [
    "GlobalTheory.CongW.TypeExists.exists_type_surj"
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

## Surjective cyclic types detecting cuspidality in small subgroups

[Theorem REP.0261](https://andrewodesky.com/rh/lean/GlobalTheory.CongW.TypeExists.exists_type_surj/)

Let $E$ be a number field, $w$ a nonzero prime of $\mathcal O_E$, and $\ell$ a rational prime belonging to $w$. Let $a\ge2$, let $N$ be a neighborhood of $1$ in $\operatorname{GL}_a(E_w)$, and let $m_0\ge0$. There exist $m\ge m_0$, a compact open subgroup $J\subseteq N$, and a surjective homomorphism $\lambda:J\to\mathbb Z/\ell^m\mathbb Z$ such that $J$ has no nonidentity element of finite order. Moreover, for every $\zeta\in\mathbb C^\times$ with $\zeta^{\ell^m}=1$ and $\zeta\ne1$, every smooth irreducible complex representation $\sigma$ of $\operatorname{GL}_a(E_w)$ containing a nonzero vector $v$ with $$\sigma(g)v=\zeta^{\lambda(g)}v\qquad(g\in J)$$ is cuspidal.
