---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsCuspidalSupportIrreducibleSmoothGL.lean",
  "declarations": [
    "GlobalTheory.CuspSupportExist.reduce"
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

## A noncuspidal irreducible representation as an induced subquotient

[Theorem REP.1360](https://andrewodesky.com/rh/lean/GlobalTheory.CuspSupportExist.reduce/)

Assume the source's Bernstein–Zelevinsky finiteness theorem and geometric lemma. Let $k$ be a nonarchimedean local field, $n\ge0$, and $\pi$ a smooth irreducible complex representation of $\operatorname{GL}_n(k)$ which is not cuspidal. There are $s\ge0$, integers $d_1,\ldots,d_s\ge0$ with $\sum_i d_i=n$, a choice identifying these ordered coordinate blocks with $\{1,\ldots,n\}$, and smooth irreducible representations $\sigma_i$ of $\operatorname{GL}_{d_i}(k)$ such that $$d_i<n\quad\text{for every }i,\qquad \pi\text{ is a subquotient of }\operatorname{Ind}_{P}^{\operatorname{GL}_n(k)}(\sigma_1\boxtimes\cdots\boxtimes\sigma_s).$$ Here $P$ is the block parabolic determined by the chosen identification and induction is normalized.
