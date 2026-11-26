---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AfBridge.lean",
  "declarations": [
    "UpperTheory.V.Af.AutOnAlt"
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

## Automorphy with a conditional local window condition

[Definition / hypothesis GC.D007](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.AutOnAlt/)

Let $K$ be a CM field, $\Omega$ an algebraic closure of $\mathbb Q$, $\ell$ a prime and $\iota\colon\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism. Let $a$ assign a $3\times3$ matrix over $\overline{\mathbb Q}_\ell$ to each element of $\operatorname{Gal}(\Omega/\mathbb Q)$.

The **automorphy and window condition** on $a$ is the existence of an embedding $K\hookrightarrow\Omega$ and a representation $\rho\colon\operatorname{Gal}(\Omega/K)\to\mathrm{GL}_3(\overline{\mathbb Q}_\ell)$ whose matrices are the restrictions of $a$, such that the twist $\rho\otimes\chi_\ell^{-1}$ has both properties below. Here $\chi_\ell$ is the $\ell$-adic cyclotomic character.

1. There is a regular algebraic conjugate self-dual cuspidal representation of $\mathrm{GL}_3(\mathbb A_K)$ to which the twist is attached via $\iota$ (the attachment condition is not expanded).
2. If the twist is continuous, then at every prime above $\ell$ an invariant-flag condition implies a stronger invariant-flag condition; and, for every regular algebraic cuspidal representation to which the twist is attached, there is a real number $t$ such that a window condition with parameter $t$ holds at every prime not above $\ell$ and at every prime above $\ell$ satisfying the stronger invariant-flag condition. The flag and window conditions are not expanded.
