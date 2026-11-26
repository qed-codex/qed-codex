---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HarishChandraInductionCharacterRestrictionDecompStatement.lean",
  "declarations": [
    "GlobalTheory.T.harishChandra_induction_character_restriction_decomp"
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

## Harish–Chandra induction and restriction preserve characters

[Theorem REP.1540](https://andrewodesky.com/rh/lean/GlobalTheory.T.harishChandra_induction_character_restriction_decomp/)

Let $p$ be prime and $a,b,n\ge0$ with $n=a+b$. Put $G_m=\operatorname{GL}_m(\mathbb F_p)$ and let $P\subseteq G_n$ be the upper block parabolic with Levi $G_a\times G_b$ and unipotent radical $U$. If $\alpha,\beta$ are characters of complex representations of $G_a,G_b$, then Harish–Chandra induction of $\alpha\otimes\beta$ is a character of $G_n$.

For every character $\chi$ of $G_n$, there is a finite list of pairs of irreducible characters $(\alpha_j,\beta_j)$ of $G_a,G_b$ such that $$\frac1{|U|}\sum_{u\in U}\chi(\operatorname{diag}(x,y)u) =\sum_j\alpha_j(x)\beta_j(y)\qquad(x\in G_a,\ y\in G_b).$$ Repetitions in the list record multiplicities.
