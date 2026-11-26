---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.SR.descWeak"
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

## Weak descent to a definite unitary group

[Theorem AGR.1711](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.SR.descWeak/)

Let $E$ be a CM number field, $F=E^+$ its maximal real subfield, and suppose $E/F$ is unramified at every finite place. Let $p$ be a rational prime and $S$ a finite set of finite places of $F$. Assume every place of $E$ above a member of $S$ is split over $F$, and $S$ contains the places below all places of $E$ dividing $p$.

Let $2\le n\le4$, and let $\pi$ be a regular algebraic cuspidal automorphic representation of $\operatorname{GL}_n(\mathbb A_E)$ with $\pi^\vee\simeq\pi^c$. Assume $\pi$ has an unramified Satake parameter at every place of $E$ lying outside $S$.

There is an automorphic representation $\sigma$ of the definite unitary group $U(n)$ of the identity Hermitian form in ([Base change from a definite unitary group](https://andrewodesky.com/rh/lean/UpperTheory.BaseChangeIdentities.baseChangeN/)) that is unramified at every nonsplit finite place of $E$. At all but finitely many split places $w$ of $E$, $\sigma$ has an irreducible smooth local component under $U(n)(F_v)\simeq\operatorname{GL}_n(E_w)$, and this component and $\pi_w$ have the same Satake parameter.
