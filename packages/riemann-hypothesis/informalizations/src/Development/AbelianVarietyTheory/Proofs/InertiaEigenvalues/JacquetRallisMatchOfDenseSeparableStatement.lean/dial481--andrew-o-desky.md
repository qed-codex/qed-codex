---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisMatchOfDenseSeparableStatement.lean",
  "declarations": [
    "GlobalTheory.T.jacquetRallis_match_of_dense_separable"
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

## Extending Jacquet–Rallis matching from a dense locus

[Theorem REP.0253](https://andrewodesky.com/rh/lean/GlobalTheory.T.jacquetRallis_match_of_dense_separable/)

Let $F,E$ be locally compact fields with nontrivial ultrametric norms, let $F$ have characteristic zero, and let $E$ be a normed $F$-algebra of degree two. Let $z\mapsto\bar z$ be a nonidentity isometric involution of $E$ fixing $F$. Assume every norm value on $E$ is a norm value on $F$. Fix $r\ge0$ and the normalized measures specified below. Write $$\mathcal G=M_r(F)\times F^r\times F^r\times F,\qquad \mathcal H=\{H\in M_r(E):H^*=H\}\times E^r\times F.$$ For $Y=(A,b,c,d)\in\mathcal G$, regard $c$ as a row vector and put $m_j(Y)=cA^jb$. Its invariant is the tuple of the $r$ lower characteristic-polynomial coefficients of $A$, the moments $m_0,\ldots,m_{r-1}$, and $d$. For $X=(H,b,d)\in\mathcal H$, use the invariant of $(H,b,b^*,d)$ after extension to $E$.

For an invariant $a=(p,b,d)\in F^r\times F^r\times F$, let $C_p$ be the companion matrix of $T^r+\sum_{i=0}^{r-1}p_iT^i$, let $e_0$ be the first coordinate vector (zero when $r=0$), and put $$Y_a=(C_p,e_0,b,d),\qquad \Delta(a)=\det(m_{i+j}(Y_a))_{0\le i,j<r}.$$ Define matching at $a$ to mean that $O_G(f',Y_a)=O_U(f,X)$ for every $X$ having invariant $a$, and $O_G(f',Y_a)=0$ when no such $X$ exists.

Let $f':\mathcal G\to\mathbb C$ and $f:\mathcal H\to\mathbb C$ be locally constant and compactly supported. If they match at every $a$ with $\Delta(a)\ne0$ and $C_p$ having separable characteristic polynomial, they match at every $a$ with $\Delta(a)\ne0$. If $r>0$, the same conclusion follows from matching at every such $a$ with $m_0(Y_a)\ne0$.
