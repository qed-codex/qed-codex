---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/WittTowerNormStepOfSmallRank.lean",
  "declarations": [
    "GlobalTheory.T.witt_tower_norm_step_of_small_rank"
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

## Descending a theta tower with controlled algebraic scalar ratios

[Theorem THETA.1641](https://andrewodesky.com/rh/lean/GlobalTheory.T.witt_tower_norm_step_of_small_rank/)

Assume the source's local theta-input package, agreement of its two theta-integral constructions, and local matching theorem. There is $C_{F,0}\in\mathbb R$ such that, for every $\varepsilon\in\mathbb R$ and $C_F\ge C_{F,0}$, there are $C_0,x_0\in\mathbb R$ with the following property for $C\ge C_0$ and $x\ge x_0$. Fix the source's global Hermitian datum, size datum with exponent $\varepsilon$ and scale $x$, recursion package, normalized level-character family indexed by $T$ with distinguished $t_0$, and character grid with constants $(1,C_F,b)$. The recursion package requires its size and host conditions, identification of the base with the maximal real subfield, and the logarithmic-derivative bound $|d|\le x^\varepsilon$. Fix compatible Weil data and grid frames, a standard additive character with real parameter $-1$, and the source's algebraic-values package in a number field $K$ with embedding $\iota:K\hookrightarrow\mathbb C$.

Fix a grid position $(i,j)$ and $p,q\ge0$. Write $P_j,Q_j$ for its two maximal negative indices and $r_{ij}$ for the specified grid ranks. Let $X$ be a triangle of theta-integral data on Hermitian spaces $A,A',W$ with negative indices $p,q+1,p+q+1$, satisfying the grid's prescribed character and local-place conditions, and $$p\le P_j,\quad q+1\le Q_j,\quad\dim A+2P_j=r_{i+1,j+1}+2p,\quad\dim A'+2Q_j=r_{ij}+2(q+1).$$ Assume the two integral families have the common-quotient factorization specified below with scalar $\lambda_t\ne0$, and $\dim A=\dim A'+2e$ for $e\ge0$. Let $L_t(s)$ be Hecke L-functions for the prescribed grid characters.

There are Hermitian spaces $B,B',W_1$, a theta triangle $Y$ at the same position with negative indices $p,q,p+q$, with the same stage conditions and the corresponding rank equations, and scalars $c_t,y_t$ such that $y_t\ne0$ and $$\lambda_t L_t(e+1)=y_t c_t\qquad(t\in T).$$ For fixed polynomial test functions the two integral families of $Y$ are convergent, the second is nonzero as a function for every $t$, and their ratio is $c_t$; at least one $c_t$ is nonzero. For every $t$ there are $a_t\in\mathcal O_K[1/Q(t)]^\times$ and $g_{t,v},g'_{t,v}\in\mathcal O_K$, each dividing $q_v^{d_v}$ for every $v$ in the grid's finite set $S_0$, such that $$y_t=\iota\!\left(a_t\prod_{v\in S_0}\frac{g_{t,v}}{g'_{t,v}}\right)y_{t_0}.$$ Here $Q(t)$, the nonnegative exponents $d_v$, and $q_v=|\mathcal O_F/\mathfrak p_v|$ are the grid's prescribed integer and conductor data.
