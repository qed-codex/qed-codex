---
{
  "module": "src/Development/EtaleCohomology/EtaleSheaves/LeafUnitsPfF.lean",
  "declarations": [
    "LateralTheory.E.E4.LeafIntBoth_of"
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

## An element integral over two polynomial rings is algebraic

[Theorem ALG.0516](https://andrewodesky.com/rh/lean/LateralTheory.E.E4.LeafIntBoth_of/)

Assume that for every field extension $L'/k'$, every $t'\in L'$ transcendental over $k'$, and every $x'\in L'$ integral over $k'[t']$, the minimal polynomial of $x'$ over $k'(t')$ has all its coefficients in $k'[t']$.

Let $L/k$ be a field extension and $t\in L$ transcendental over $k$. If $x\in L$ is integral over both $k[t]$ and $k[t^{-1}]$, then $x$ is integral over $k$.
