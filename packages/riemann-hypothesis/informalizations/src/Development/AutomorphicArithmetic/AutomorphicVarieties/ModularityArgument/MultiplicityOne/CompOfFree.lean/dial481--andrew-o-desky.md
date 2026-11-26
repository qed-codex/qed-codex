---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/MultiplicityOne/CompOfFree.lean",
  "declarations": [
    "UpperTheory.V.Z.Mult.mult_free"
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

## A uniform positive multiplicity on a definite unitary group

[Theorem AGR.0031](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Mult.mult_free/)

Let $E$ be a CM number field unramified at every finite prime over its maximal real subfield $F$, and let $1\le n\le4$. Fix dominant integral weights $\lambda_v$ at the infinite places of $E$. In the definite unitary group $U(n)$ of the identity Hermitian form over $E/F$, as in ([Base change from a definite unitary group](https://andrewodesky.com/rh/lean/UpperTheory.BaseChangeIdentities.baseChangeN/)), there is an integer $a>0$ with the following property.

Let $\pi$ be a regular algebraic cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb A_E)$, realized as an irreducible invariant subspace of cusp forms, such that $\pi^\vee$ is its complex-conjugate representation, its infinitesimal characters are those associated to the weights $\lambda_v$, and it is unramified at every finite place of $E$ which is nonsplit over $F$. Choose one place of $E$ over each finite place of $F$, forming a set $S$. For every finite place $w$ of $E$, choose an open subgroup $K'_w$ of the compact group $K_w$ stabilizing the standard integral lattice in the local realization $U(n)(F_v)$, where $v$ lies below $w$, with $K'_w=K_w$ for almost all $w$ and for every nonsplit $w$. Suppose that for every split $w\in S$, the local component of $\pi$ has a nonzero $K'_w$-fixed vector under the split-place identification with $\mathrm{GL}_n(E_w)$.

Let $(\sigma_i)_{i\in I}$ be any finite family of irreducible automorphic subspaces for $U(n)$ of weight $\lambda$, each with nonzero fixed vectors under the global level $K'$ whose component at $v$ belongs to $K'_w$ for the chosen $w\in S$ above $v$. Assume their fixed-vector spaces form an internal direct sum equal to the full automorphic space of that weight and level. Then exactly $a$ indices $i$ have the following property: at all but finitely many split places $w$, a smooth irreducible local component of $\sigma_i$ and $\pi_w$ have a common Satake multiset.
