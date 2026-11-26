---
{
  "module": "src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/KOneConsequence.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.G7.Top.e_one_identity",
    "Formalism.InvariantFactorPaths.G7.Top.e_one_integral",
    "Formalism.InvariantFactorPaths.G7.Top.hitsCapPos",
    "Formalism.InvariantFactorPaths.G7.Top.minorHits"
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

## Jets and directional Hasse derivatives

[Theorem ALG.0116](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.e_one_identity/)

Let $K$ be a field, $X=(X_1,\ldots,X_n)$, $Q\in K[X]$, $G\in K[[X]]$, and $b_j\in K^n$ for a finite index set $J$. Put $L_j(X)=\sum_a b_{j,a}X_a$. For a multi-index $\beta\in\mathbb N^J$, define $$D_b^{[\beta]}Q=[T^\beta]Q\!\left(X+\sum_{j\in J}T_jb_j\right).$$ The notation $[X^\alpha]$ and $[T^\beta]$ denotes coefficient extraction, and $\alpha!=\prod_a\alpha_a!$. Writing $Q(\partial)G(0)=\sum_\alpha\alpha!\,[X^\alpha]Q\,[X^\alpha]G$, one has $$Q(\partial)\left(\prod_{j\in J}L_j^{\beta_j}G\right)(0)=\left(\prod_{j\in J}\beta_j!\right)(D_b^{[\beta]}Q)(\partial)G(0).$$

## Directional derivatives of products of minors

[Theorem ALG.0135](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.hitsCapPos/)

Over a field $K$, let $X_s$ be independent $r_0\times r_1$ matrices indexed by positions $s$. For $c=1,\ldots,C$, choose a position $s_c$, a matrix $A_c\in M_{l_c\times r_0}(K)$ and a list of $l_c$ columns $I_c$, and put $$Q(X)=\prod_{c=1}^C\det\big((A_cX_{s_c})_{I_c}\big).$$ Let $J$ be a finite set indexing directions that add a vector $\xi_j\in K^{r_0}$ to column $b_j$ at position $s_j$. Let $\beta\in\mathbb N^J$, fix a position $s_0$, and let $S\subseteq J$. Suppose $s_j=s_0$ and $\xi_j=\xi_{j'}$ for all $j,j'\in S$. If $$\sum_{j\in S}\beta_j>\#\{c:s_c=s_0\},$$ then $$D^{[\beta]}Q=0.$$ The derivative is the coefficient of $T^\beta$ after adding all the indicated $T_j$-directions, including those outside $S$. The column lists are arbitrary; distinctness and nonvanishing of the minors are not assumed.

## Vanishing of incompatible directional Hasse derivatives of a minor

[Theorem ALG.0888](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.minorHits/)

Let $K$ be a field, $\Sigma$ a set, $A,B$ finite sets of sizes $r_0,r_1$, and $\mathcal K$ a finite set. Fix $s\in\Sigma$, an $l\times r_0$ matrix $T$ over $K$, a map $I:\{1,\ldots,l\}\to B$, and independent variables $X_{t,a,b}$. Put $$Q(X)=\det\left(\sum_{a\in A}T_{ia}X_{s,a,I(j)}\right)_{1\le i,j\le l}.$$ For each $k\in\mathcal K$, choose $s_k\in\Sigma$, $b_k\in B$, and $\xi_k\in K^A$, and set $v_k(t,a,b)=\xi_k(a)$ if $(t,b)=(s_k,b_k)$, and $0$ otherwise. For a multi-index $\beta\in\mathbb N^{\mathcal K}$, let $D^{[\beta]}Q$ be the coefficient of $\prod_k u_k^{\beta_k}$ in $Q(X+\sum_k u_kv_k)$. Then $D^{[\beta]}Q=0$ if any of the following holds:

- Some $\beta_k\ge2$.
- There are distinct $k,k'$ with $\beta_k,\beta_{k'}\ge1$, $s_k=s_{k'}$, and either $\xi_k=\xi_{k'}$ or $b_k=b_{k'}$.
- Some $\beta_k\ge1$ has $s_k\ne s$ or $b_k\notin I(\{1,\ldots,l\})$.

## Integrality and degree of directional Hasse derivatives

[Theorem ALG.0842](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.e_one_integral/)

Let $K$ be an ultrametric normed field, let $I$ be any set, and let $J$ be finite. Choose vectors $b_j\in K^I$ and a multi-index $\beta\in\mathbb N^J$. For $Q\in K[X_i:i\in I]$, define $$D_b^{[\beta]}Q(X)=[T^\beta]\,Q\left(X_i+\sum_{j\in J}b_{j,i}T_j:i\in I\right),\qquad |\beta|=\sum_{j\in J}\beta_j.$$ If all coefficients of $Q$ and all $b_{j,i}$ have norm at most one, then all coefficients of $D_b^{[\beta]}Q$ have norm at most one. If $Q$ is homogeneous of degree $d$, then $D_b^{[\beta]}Q$ is homogeneous of degree $\max(d-|\beta|,0)$, and it is zero when $d<|\beta|$.
