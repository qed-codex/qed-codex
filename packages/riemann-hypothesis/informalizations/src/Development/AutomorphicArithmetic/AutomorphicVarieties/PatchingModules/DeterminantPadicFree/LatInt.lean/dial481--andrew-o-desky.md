---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/DeterminantPadicFree/LatInt.lean",
  "declarations": [
    "UpperTheory.V.Pa.Det.latInt"
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

## An integral basis for a uniformly bounded representation

[Theorem PHT.0462](https://andrewodesky.com/rh/lean/UpperTheory.V.Pa.Det.latInt/)

Let $A$ be a discrete valuation domain with fraction field $F$, let $G$ be a group, and let $r:G\to\operatorname{GL}_m(F)$ be a representation. Suppose there is $d\in A\setminus\{0\}$ such that every entry of $d\,r(g)$ lies in $A$ for every $g\in G$. Then there are $Q\in\operatorname{GL}_m(F)$ and $r_0:G\to\operatorname{GL}_m(A)$ such that $$r(g)Q=Qr_0(g)\qquad(g\in G),$$ where $A$-valued matrices are viewed in $F$.

**Compact representations.** Let $\ell$ be prime, $G$ a group with a compact topology, $n\ge0$, and $E\subseteq\overline{\mathbb Q}_\ell$ an intermediate field over $\mathbb Q_\ell$. Let $O$ be a discrete valuation $\mathbb Z_\ell$-subalgebra, finite as a $\mathbb Z_\ell$-module, of $\overline{\mathbb Q}_\ell$ with $$O=\{x\in E:|x|_\ell\le1\}.$$ Let $r:G\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ be a group homomorphism with continuous matrix entries, all lying in $E$. There are $Q\in\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ and a group homomorphism $r_0:G\to\operatorname{GL}_n(O)$ with $$r(g)Q=Qr_0(g)\qquad(g\in G),$$ where $r_0(g)$ is viewed over $\overline{\mathbb Q}_\ell$.
