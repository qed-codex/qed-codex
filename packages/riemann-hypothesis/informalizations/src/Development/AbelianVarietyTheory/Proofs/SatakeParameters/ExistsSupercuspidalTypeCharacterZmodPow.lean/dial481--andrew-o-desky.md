---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsSupercuspidalTypeCharacterZmodPow.lean",
  "declarations": [
    "GlobalTheory.CuspType.exists_type"
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

## Small torsion-free compact types detecting cuspidality

[Theorem REP.0579](https://andrewodesky.com/rh/lean/GlobalTheory.CuspType.exists_type/)

Let $E$ be a number field, let $w\mid\ell$ be a finite prime above the rational prime $\ell$, and let $a\ge1$. Given any neighborhood $N$ of $1$ in $\operatorname{GL}_a(E_w)$ and integer $m_0\ge0$, there are $m\ge m_0$, a torsion-free compact open subgroup $J\subseteq N$, and a homomorphism $$\lambda:J\longrightarrow\mathbb Z/\ell^m\mathbb Z$$ with open kernel, such that the following holds. For every $\zeta\in\mathbb C^\times$ with $\zeta^{\ell^m}=1$ and $\zeta\ne1$, every smooth irreducible complex representation $\sigma$ of $\operatorname{GL}_a(E_w)$ containing $0\ne v$ with $$\sigma(j)v=\zeta^{\widetilde{\lambda(j)}}v\qquad(j\in J)$$ is cuspidal. Here $\widetilde{\lambda(j)}$ is the representative in $\{0,\ldots,\ell^m-1\}$.
