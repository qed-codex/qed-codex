---
{
  "module": "src/Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/IntWAPlaces.lean",
  "declarations": [
    "Formalism.L2.KerInert.weak_approximation_places"
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

## Simultaneous isometries at the primes above a rational prime

[Theorem ANT.0623](https://andrewodesky.com/rh/lean/Formalism.L2.KerInert.weak_approximation_places/)

Let $E$ be a totally complex number field with an involution $a\mapsto\bar a$ inducing complex conjugation under every embedding into $\mathbb C$. Assume that, for every maximal ideal $P\subset\mathcal O_E$, there is $a\in\mathcal O_E$ with $a-\bar a\notin P$. Give $E^n$ the form $$h(x,y)=\sum_{i=1}^n\bar x_i y_i,$$ and write $U(h)(E)$ for its group of $E$-linear isometries. Let $p$ be a rational prime and $L\subseteq E^n$ any $\mathcal O_E$-submodule. Suppose that for every maximal $P\subset\mathcal O_E$ containing $p$, some $g_P\in U(h)(E)$ satisfies $$g_P(\mathcal O_E^n)_{(P,\bar P)}=L_{(P,\bar P)}.$$ Then one $\gamma\in U(h)(E)$ satisfies these equalities for every such $P$ simultaneously.
