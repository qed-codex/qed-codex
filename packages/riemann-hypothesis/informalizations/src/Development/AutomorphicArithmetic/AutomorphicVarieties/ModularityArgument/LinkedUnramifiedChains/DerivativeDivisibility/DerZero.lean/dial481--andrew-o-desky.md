---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/DerivativeDivisibility/DerZero.lean",
  "declarations": [
    "UpperTheory.V.J.derZero"
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

## Vanishing of point derivations at a simple polynomial root

[Theorem ALG.0454](https://andrewodesky.com/rh/lean/UpperTheory.V.J.derZero/)

Let $O,B$ be commutative rings, $\Lambda$ an integrally closed domain of characteristic zero, and $K$ a field, with $O$-algebra structures on $\Lambda,B,K$. Fix an $O$-algebra map $\lambda:\Lambda\to B$, an ideal $J\subseteq B$, an element $t\in B$, and polynomials $g_1,\ldots,g_s\in\Lambda[X]$ satisfying the comparison conditions below. Put $$I_i=\{b\in B:b\prod_{j\ne i}g_j(t)\in J\},$$ where polynomial evaluation uses $\lambda$. Let $x:B\to K$ be an $O$-algebra map with $I_i\subseteq\ker x$. Suppose $x(t)$ has multiplicity exactly one as a root of $\prod_jg_j$ after applying $x\circ\lambda$ to its coefficients. Every $O$-linear point derivation $\delta:B\to K$ satisfying $$\delta(ab)=x(a)\delta(b)+x(b)\delta(a),\quad\delta(J)=0,\quad\delta(\lambda(\Lambda))=0$$ is zero.
