---
{
  "module": "src/CompanionTheory/AutomorphicTheory/PadicCyclotomicFields/GcohTopEuler.lean",
  "declarations": [
    "CompanionTheory.LocalTateOrthogonality.Gcoh.top_euler"
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

## Local Euler characteristic

[Theorem GC.0132](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_euler/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ finite, $r>0$, and $M$ a finite discrete $\mathbb Z/\ell^r\mathbb Z$-module with continuous action of the absolute Galois group of $K$. Then $$\#H^1(K,M)=\#H^0(K,M)\,\#H^2(K,M)\,(\#M)^{[K:\mathbb Q_\ell]}.$$
