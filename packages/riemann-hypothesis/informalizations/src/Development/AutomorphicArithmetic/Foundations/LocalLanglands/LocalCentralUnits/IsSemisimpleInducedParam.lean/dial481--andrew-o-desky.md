---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/LocalLanglands/LocalCentralUnits/IsSemisimpleInducedParam.lean",
  "declarations": [
    "UpperTheory.Zero.LLC.indEx"
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

## A Weil–Deligne parameter with a prescribed cyclic inertia orbit

[Theorem AGR.1649](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.indEx/)

Let $E$ be a number field, $\Omega$ an algebraic closure, $w$ a finite place, and $A\subseteq\Omega$ a valuation ring above $w$. Write $W_w$ for the associated Weil group, $I_w$ for inertia, and $\deg:W_w\to\mathbb Z$ for the degree map. Fix $\phi\in W_w$ with $\deg\phi=1$, an integer $n>0$, and characters $\eta_j:I_w\to\mathbb C^\times$ indexed by $j\in\mathbb Z$. Assume $\ker\eta_0$ is open, $$\eta_j(\phi t\phi^{-1})=\eta_{j+1}(t),\qquad \eta_j=\eta_{j'}\ \Longleftrightarrow\ n\mid j-j'.$$ For every $c\in\mathbb C^\times$, there exists an irreducible complex Weil–Deligne parameter $V$ of dimension $n$ with $$\det V(\phi)=c,\qquad \det(TI-V(t))=\prod_{j=0}^{n-1}(T-\eta_j(t))\quad(t\in I_w).$$ If every $\eta_j$ is trivial on wild inertia, $V$ can be chosen tame.
