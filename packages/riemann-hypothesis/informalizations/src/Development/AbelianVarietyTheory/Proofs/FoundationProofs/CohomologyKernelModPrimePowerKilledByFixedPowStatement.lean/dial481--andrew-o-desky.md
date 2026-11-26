---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/CohomologyKernelModPrimePowerKilledByFixedPowStatement.lean",
  "declarations": [
    "GlobalTheory.T.cohomologyKernel_modPrimePower_killed_by_fixed_pow"
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

## A uniform denominator for integral approximate coboundaries

[Theorem GC.1112](https://andrewodesky.com/rh/lean/GlobalTheory.T.cohomologyKernel_modPrimePower_killed_by_fixed_pow/)

Let $\ell$ be prime, $\Omega$ a field with a $\mathbb Q$-algebra structure, and $G=\operatorname{Aut}_{\mathbb Q}(\Omega)$. Let $O\subseteq\overline{\mathbb Q}_\ell$ be a discrete valuation $\mathbb Z_\ell$-subalgebra finite as a $\mathbb Z_\ell$-module. Let $W:G\to\operatorname{GL}_2(\overline{\mathbb Q}_\ell)$ be a group homomorphism with all matrix entries in $O$. Assume $\det(W(g)-1)\ne0$ for some $g\in G$.

There is $r\ge0$ such that for every $n\ge0$, every function $a:G\to O^2$, and every $y\in\overline{\mathbb Q}_\ell^2$ with $\ell^k y\in O^2$ for some $k\ge0$, if $$|a_i(s)-(W(s)y-y)_i|_\ell\le\ell^{-n}\qquad(s\in G,\ i=1,2),$$ then there is $x\in O^2$ such that $$|\ell^r a_i(s)-(W(s)x-x)_i|_\ell\le\ell^{-n}\qquad(s\in G,\ i=1,2).$$
