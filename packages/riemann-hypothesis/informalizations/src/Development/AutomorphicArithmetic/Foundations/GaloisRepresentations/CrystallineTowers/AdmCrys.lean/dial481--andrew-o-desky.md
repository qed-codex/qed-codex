---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/AdmCrys.lean",
  "declarations": [
    "UpperTheory.Gal.Seam.isCrys_of_isAdmP"
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

## Crystallinity from an invariant period matrix

[Theorem PHT.1532](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Seam.isCrys_of_isAdmP/)

Let $\ell$ be prime. For this prime, choose data satisfying Hypothesis (local period data) in ([Local period rings and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LocRings/)). Write $B,D$ for its crystalline and de Rham rings and $\iota:B\to D$ for their comparison map.

Let $K,L\subseteq\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$, put $G_K=\operatorname{Gal}(\overline{\mathbb Q}_\ell/K)$, let $d\ge0$ be an integer, and let $$r:G_K\to\operatorname{GL}_d(\mathbb Q_\ell),\qquad r':G_K\to\operatorname{GL}_d(L)$$ be homomorphisms such that $r'(g)$ is obtained by extending the entries of $r(g)$ to $L$. Suppose there are matrices $A,B_0\in M_d(D)$, every entry of each in $\iota(B)$, with $$AB_0=1,\qquad r(g)\,g(A)=A\quad(g\in G_K).$$ Then the representation of $G_K$ on $L^d$ defined by $r'$ is crystalline.
