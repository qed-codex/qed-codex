---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/CpTransportedTaylorSeriesTranslateNormLe.lean",
  "declarations": [
    "GlobalTheory.MomOne.TransNorm.bd_cancel_prod"
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

## Cancellation of power series with coefficient supremum one

[Theorem PHT.0783](https://andrewodesky.com/rh/lean/GlobalTheory.MomOne.TransNorm.bd_cancel_prod/)

Let $q$ be prime and let $\mathbb C_q$ be the completed algebraic closure of $\mathbb Q_q$. Let $A$ be a set, $S\subset A$ finite, $g_i\in\mathbb C_q[[T]]$ for $i\in A$, and $B\in\mathbb R$. Assume $$|[T^n]g_i|\le1\quad(i\in A,\ n\ge0),\qquad \forall i\in A\ \forall r<1\ \exists n\ge0:\ r<|[T^n]g_i|.$$ If $f\in\mathbb C_q[[T]]$ has bounded coefficients and every coefficient of $f\prod_{i\in S}g_i$ has absolute value at most $B$, then every coefficient of $f$ has absolute value at most $B$.
