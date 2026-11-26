---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/PowerSeriesCoeffNormLeOneRootCoprimePadic.lean",
  "declarations": [
    "GlobalTheory.RootInt.intSer_root"
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

## Integral coefficients of a prime-to-p power-series root

[Theorem PHT.0332](https://andrewodesky.com/rh/lean/GlobalTheory.RootInt.intSer_root/)

Let $p$ be prime and $N\ge1$ an integer coprime to $p$. Let $s(T)\in\mathbb C_p[[T]]$ have constant coefficient $1$. If every coefficient of $s(T)^N$ has $p$-adic norm at most $1$, then every coefficient of $s(T)$ has norm at most $1$.
