---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/NormalizedValuationOfPrimeOfGaloisExtensionStatement.lean",
  "declarations": [
    "GlobalTheory.T.normalizedValuationOfPrime_of_galoisExtension"
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

## Normalized valuations and the inertia group

[Theorem PHT.0444](https://andrewodesky.com/rh/lean/GlobalTheory.T.normalizedValuationOfPrime_of_galoisExtension/)

Let $L/F$ be a finite Galois extension of nonarchimedean local fields with compatible valuations. Let $p,E\ge0$ be integers such that the normalized additive valuation on $\mathcal O_L$ satisfies $v_L(p)=E<\infty$. There is an integer $e\ge0$ such that $$v_F(p)=e,\qquad E=e(L/F)e,\qquad e(L/F)=|G_0(L/F)|,$$ where $e(L/F)$ is the ramification index and $G_0(L/F)$ is the zeroth lower ramification group.
