---
{
  "module": "src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementE.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.G7.HitsCapPos"
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

## Directional derivatives of products of minors

[Theorem ALG.0135](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.hitsCapPos/)

Over a field $K$, let $X_s$ be independent $r_0\times r_1$ matrices indexed by positions $s$. For $c=1,\ldots,C$, choose a position $s_c$, a matrix $A_c\in M_{l_c\times r_0}(K)$ and a list of $l_c$ columns $I_c$, and put $$Q(X)=\prod_{c=1}^C\det\big((A_cX_{s_c})_{I_c}\big).$$ Let $J$ be a finite set indexing directions that add a vector $\xi_j\in K^{r_0}$ to column $b_j$ at position $s_j$. Let $\beta\in\mathbb N^J$, fix a position $s_0$, and let $S\subseteq J$. Suppose $s_j=s_0$ and $\xi_j=\xi_{j'}$ for all $j,j'\in S$. If $$\sum_{j\in S}\beta_j>\#\{c:s_c=s_0\},$$ then $$D^{[\beta]}Q=0.$$ The derivative is the coefficient of $T^\beta$ after adding all the indicated $T_j$-directions, including those outside $S$. The column lists are arbitrary; distinctness and nonvanishing of the minors are not assumed.
