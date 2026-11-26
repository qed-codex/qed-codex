---
{
  "module": "src/Formalism/ThetaLogCoordinates/JacobiPathWeights/JacobiMinorProofs/LinearIndependentOfLead.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.GelfandTsetlinBases.path_basis_lemma"
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

## Linear independence of semistandard products of minors

[Theorem REP.0666](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.GelfandTsetlinBases.path_basis_lemma/)

Let $k$ be a field and let $n,C\ge0$. Write $X=(x_{ij})_{0\le i,j<n}$ for the generic matrix. For a family $T=(T_c)_{0\le c<C}$ of subsets of $\{0,\ldots,n-1\}$, write the elements of each $T_c$ in increasing order. Call $T$ semistandard if, for consecutive indices $c,c+1$ and every $0\le r<|T_{c+1}|$, the $r$th element of $T_c$ is at most the $r$th element of $T_{c+1}$, with a missing element of $T_c$ assigned the value $n$.

The polynomials $$\prod_{c=0}^{C-1}\det X_{\{0,\ldots,|T_c|-1\},T_c}$$ indexed by all such semistandard families are linearly independent over $k$.
