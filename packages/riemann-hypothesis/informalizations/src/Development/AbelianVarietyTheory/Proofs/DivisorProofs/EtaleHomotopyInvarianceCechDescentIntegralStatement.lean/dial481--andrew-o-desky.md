---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleHomotopyInvarianceCechDescentIntegralStatement.lean",
  "declarations": [
    "GlobalTheory.T.etaleHomotopyInvariance_cechDescent_integral"
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

## Descending étale homotopy invariance along an integral cover

[Theorem AG.0382](https://andrewodesky.com/rh/lean/GlobalTheory.T.etaleHomotopyInvariance_cechDescent_integral/)

Let $q\ge1$ and let $A\to B$ be an integral homomorphism of commutative rings. Assume its kernel is contained in the nilradical of $A$ and $q$ is invertible in $A$. Suppose that for every $k\ge0$, every integer twist $i$, and every cohomological degree $n\in\mathbb Z$, projection induces an isomorphism $$H^n_{\mathrm{\acute et}}(\operatorname{Spec}(B^{\otimes_A(k+1)}),\mathbb Z/q\mathbb Z(i)) \longrightarrow H^n_{\mathrm{\acute et}}(\mathbb A^1_{B^{\otimes_A(k+1)}},\mathbb Z/q\mathbb Z(i)).$$ Then the same homotopy-invariance assertion holds over $A$, for every $i$ and $n$.
