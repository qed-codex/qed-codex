---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/InvVolConjLevelOne.lean",
  "declarations": [
    "GlobalTheory.FunObj.GridChoice"
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

## Rationality hypothesis for a grid with Weil data

[Definition / hypothesis THETA.D040](https://andrewodesky.com/rh/lean/GlobalTheory.RowTest.NumbersIn/)

The rationality hypothesis for a grid with Weil data requires that certain complex numbers attached to the grid lie in the image $\jmath(K)$ of the coefficient field: roots of unity, square roots of norms of places, local values of the Hecke characters, quotients of values of partial $L$-functions, and the theta integrals of one definite triangle for every square.

The setting and the notation are those of ([Grids of Hermitian spaces with Weil data, and properties of all grids with large parameters](https://andrewodesky.com/rh/lean/GlobalTheory.ChiGrid.GridData/)): a datum $D$ with the coefficient field $K$ and its embedding $\jmath\colon K\to\mathbb C$, a family of characters with index set $\mathcal T$ and base index $\mu_0$, a grid with the places $W(t)$, the exponents $\ell(w)$ and the characters $\chi_i$, $\nu_{t,i,j}$, partial $L$-functions of Hecke characters, and Weil data on the grid.

**Choices of bases and normalisations.** A *choice of bases and normalisations* $\mathcal S$ for a grid with Weil data consists of

1. adelic bases $\beta_{i,j}$ of the grid, as in ([Square constants of a grid: matched test data and normalised measures](https://andrewodesky.com/rh/lean/GlobalTheory.FunObj.IsSquareConst/));
2. a frame $\beta'_j$ of the lattice $\Lambda(U_j)$ for $0\le j\le m$, subject to two conditions that relate, at the places of every $W(t)$, the frames $\beta'_j$ and $\beta_{m,j}$ through the orthogonal extensions of $U_j$ to $V_{m,j}$ and of $V_{m,m}$ to $U_m$;
3. further data, in two parts, attached to the grid and to the Weil data;
4. a finite set $P_{\mathfrak A}$ of finite places of $E$, each of which divides $\mathfrak A$ or $\bar{\mathfrak A}$, such that for every place $w$ dividing $\mathfrak A$ exactly one place of $P_{\mathfrak A}$ lies above the same place of $F$ as $w$.

This page does not reproduce the two conditions of item 2 or the definition of the data of item 3; of the latter only statement 7 below makes use.

**The hypothesis.** Let $\mathcal S$ be a choice of bases and normalisations. The *rationality hypothesis* for $(\mathcal S,\mu_0)$ is the conjunction of the following statements.

1. For every finite place $w$ of $E$ and every $x\in E_w^\times$, the local values at $x$ of the characters $\mu^0_j$ $(0\le j<m)$, $\xi_t$ $(t\in\mathcal T)$ and $\chi_i$ $(1\le i\le m)$ lie in $\jmath(K)$. For every finite place $w$ at which the respective character is unramified, $\eta_w(\varpi_w)\,N(w)^{-1/2}$, $\chi_{\Psi,w}(\varpi_w)$, $\delta_w(\varpi_w)$ and $\delta'_w(\varpi_w)$ lie in $\jmath(K)$; here $\chi_\Psi$ is the character so denoted in the character frame.
2. Every complex number $z$ with $z^8=1$ lies in $\jmath(K)$.
3. For every $t\in\mathcal T$ and $w\in W(t)$, every complex number $z$ with $z^{n}=1$, $n=N(w)^{\ell(w)}$, lies in $\jmath(K)$.
4. $\sqrt{N(w)}\in\jmath(K)$ for every $w\in P_{\mathfrak A}$ and every $w$ in some $W(t)$.
5. For all $0\le i,j<m$ and $t\in\mathcal T$: if $\Lambda$ is the partial $L$-function of $\nu_{t,i,j}$ and $\Lambda_0$ that of $\nu_{\mu_0,i,j}$, then $\Lambda(s)/\Lambda_0(s)\in\jmath(K)$ for every integer $s$ with $1\le s\le k+m\,(t_0+r+7)+1$ and $\Lambda_0(s)\ne0$.
6. For all $0\le i,j<m$: if the square $(i,j)$ has a definite triangle, in the sense of ([Triangles of Hermitian spaces, their constants, and the definite triangle of a square](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.UnitCharTriangle.Tri/)), then it has a definite triangle with the following property. There are nonzero complex numbers $\Omega$, $\Omega'$ such that $$I_t(P)(h)/\Omega\in\jmath(K),\qquad I'_t(P')(h)/\Omega'\in\jmath(K)$$ for all $t\in\mathcal T$, all $h\in G_B(\mathbb A)$ with trivial archimedean part, and all monomials $P$, $P'$ for which the respective integrand is integrable.
7. Two further families of complex numbers lie in $\jmath(K)$: certain values of the additive characters $x\mapsto\psi(\operatorname{Tr}_{\mathbb A_E/\mathbb A_F}(\xi_0x))$ of the completions $E_w$, $w\in W(t)$, and certain numbers formed from the data of item 3 of $\mathcal S$. This page does not reproduce their definitions.
