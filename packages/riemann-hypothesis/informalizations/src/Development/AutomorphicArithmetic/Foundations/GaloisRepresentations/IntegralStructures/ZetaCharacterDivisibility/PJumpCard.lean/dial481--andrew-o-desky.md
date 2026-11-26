---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PJumpCard.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Div.jumpCard_of"
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

## Number of de Rham filtration jumps

[Theorem PHT.1685](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Div.jumpCard_of/)

Fix a prime $\ell$ and the source's compatible local period-ring datum, including a prime in its coefficient ring, its infinite-level ring, and a comparison tying these together. Let $E$ be a number field, $\Omega/E$ an algebraic closure, and $A$ a valuation subring of $\Omega$. Let $O$ be a topological commutative $\mathbb Z_\ell$-algebra equipped with the source's local comparison datum for the decomposition group $D_A$ and its local field $K_w$.

Let $r:D_A\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ be de Rham in this datum, with $a\ge0$. For any embedding $\tau:E\to\overline{\mathbb Q}_\ell$ and any finite extension $L'/\mathbb Q_\ell$ with an embedding $\tau':K_w\to L'$ inducing $\tau$ in the local comparison, there is a multiset $J$ of integers describing the de Rham filtration jumps at $\tau$, and $$|J|=a.$$ Jumps are counted with their graded multiplicities.
