---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/DefiniteNHolds.lean",
  "declarations": [
    "UpperTheory.BaseChangeIdentities.baseChangeN"
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

## Base change from a definite unitary group

[Theorem AGR.0051](https://andrewodesky.com/rh/lean/UpperTheory.BaseChangeIdentities.baseChangeN/)

Let $E/E^+$ be a CM extension unramified at every finite place and let $n\ge1$. Let $\pi$ be an automorphic representation of the unitary group of the identity Hermitian form in $n$ variables. There is a finite decomposition $n=\sum_jn_j$ into positive ranks. There are discrete automorphic representations $V_j$ of $\mathrm{GL}_{n_j}(\mathbb A_E)$, with local factors $\sigma_{j,w}$ at finite places $w$, and irreducible local representations $\Pi_w$ of $\mathrm{GL}_n(E_w)$. They have the following properties. Each $V_j$ has an injective equivariant realization in the prescribed induced forms built from a unitary normalized conjugate-self-dual cuspidal subspace and absolute-power Hecke twists.

$\Pi_w$ is a subquotient of the normalized parabolic product of the $\sigma_{j,w}$. It is spherical wherever $\pi$ is unramified. At split places it agrees with the local component of $\pi$ under the split unitary identification. At an inert place, assume the prescribed compatibility of local involution, uniformizer, and residue cardinality. If that place admits an unramified unitary Satake parameter $\alpha=(\alpha_1,\ldots,\alpha_{\lfloor n/2\rfloor})$, the Satake multiset of $\Pi_w$ is $$\{\alpha_i,\alpha_i^{-1}:1\le i\le\lfloor n/2\rfloor\}\ \sqcup\ \{1\}^{\,n\bmod2}.$$ If $\pi$ has highest weight $\lambda$ at an embedding, the multiset union of the infinitesimal characters of the $V_j$ there is $$\{\lambda_i+(n+1)/2-i:1\le i\le n\}.$$
