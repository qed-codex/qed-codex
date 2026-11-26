---
{
  "module": "src/Formalism/TorsionNormIteration/InverseIntegralClasses/InvInt.lean",
  "declarations": [
    "Formalism.LT.InvIntP.invIntegralOfClass"
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

## Recovering integral coefficients from a class of formal composites

[Theorem PHT.0929](https://andrewodesky.com/rh/lean/Formalism.LT.InvIntP.invIntegralOfClass/)

Let $K$ be an ultrametric normed field, $I$ a finite set, and $\mathcal C\subseteq K[[X_i:i\in I]]$. Call a series integral if all its coefficients have norm at most one. Let $f\in K[[T]]$ satisfy $f(0)=0$ and $[T]f=1$. Suppose:

- $A-B\in\mathcal C$ whenever $A,B\in\mathcal C$;
- $f(P)\in\mathcal C$ for every integral $P\in K[[X_i:i\in I]]$ with $P(0)=0$;
- for every $D\in\mathcal C$ and $m\ge1$, if all coefficients of $D$ of total degree below $m$ vanish, then all its coefficients of total degree $m$ have norm at most one.

If $h\in K[[X_i:i\in I]]$ has $h(0)=0$ and $f(h)\in\mathcal C$, then $h$ is integral.
