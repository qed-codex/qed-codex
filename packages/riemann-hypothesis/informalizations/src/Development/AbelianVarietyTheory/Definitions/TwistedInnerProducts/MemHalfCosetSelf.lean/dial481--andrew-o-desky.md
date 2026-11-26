---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/MemHalfCosetSelf.lean",
  "declarations": [
    "GlobalTheory.RowTest.IsBottomTri",
    "GlobalTheory.RowTest.NumbersIn"
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

## Triangles of Hermitian spaces, their constants, and the definite triangle of a square

[Definition / hypothesis THETA.D020](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.UnitCharTriangle.Tri/)

A triangle consists of three Hermitian spaces $A$, $A'$, $B$ with $\operatorname{rank}A+\operatorname{rank}A'=\operatorname{rank}B$ and, for every index $t$, of Weil representations and test functions for the pairs $(A,B)$ and $(A',B)$. A constant of the triangle is a function $c^0$ of $t$ such that a theta integral over the unitary group of $A$ is $c^0(t)$ times a theta integral over the unitary group of $A'$, as functions on the unitary group of $B$. This page defines triangles, their constants, and the definite triangle of a square of a grid.

The setting and the notation are those of ([Grids of Hermitian spaces with Weil data, and properties of all grids with large parameters](https://andrewodesky.com/rh/lean/GlobalTheory.ChiGrid.GridData/)): the field $E$ with the CM type $\Psi$ and the element $\xi_0$, Hermitian spaces with recorded bases, $G_V(\mathbb A)$, $G_V(F)$, $-V$ and $W(S,T)$, frames of lattices, and an index set $\mathcal T$.

**Triangles.** A *rigidification* of a Hermitian space $V$ of rank $n$ consists of an $\mathcal O_E$-lattice $\Lambda_V\subset V$, a matrix $\beta_V\in\mathrm{GL}_n(\mathbb A_{E,f})$, and complex $n\times n$ matrices $s_V(\tau)$ and $B_V(\tau)$ for $\tau\in\Psi$. A *triangle* over $\mathcal T$ consists of

- Hermitian spaces $A$, $A'$, $B$ over $E$, each with a rigidification;
- for every $t\in\mathcal T$, representations $\omega_t$ of $G_A(\mathbb A)\times G_B(\mathbb A)$ on the complex functions on $W(A,B)$ and $\omega'_t$ of $G_{A'}(\mathbb A)\times G_B(\mathbb A)$ on the complex functions on $W(A',B)$;
- functions $\phi$ on $W(A,B)$ and $\phi'$ on $W(A',B)$;
- for every $t\in\mathcal T$, an element $e_t\in\mathbb A_E$, an integer $n_t(w)\ge0$ for every finite place $w$ of $E$, and functions $f_t$ on $W(A,B)$ and $f'_t$ on $W(A',B)$;
- measures $m$ on $G_A(\mathbb A)$ and $m'$ on $G_{A'}(\mathbb A)$, and subsets $\mathfrak F\subset G_A(\mathbb A)$ and $\mathfrak F'\subset G_{A'}(\mathbb A)$.

**Theta integrals and constants.** Let an additive character $\psi$ of $\mathbb A_F$ and a compatible family $\theta$ be given, as in the Weil data of a grid. For polynomials $P$ in the variables $z_{\tau,a,b}$ $(\tau\in\Psi,\ 1\le a\le\operatorname{rank}B,\ 1\le b\le\operatorname{rank}A)$ and $P'$ in the variables $z_{\tau,a,b}$ $(1\le a\le\operatorname{rank}B,\ 1\le b\le\operatorname{rank}A')$, let $\Phi_{t,P}$ and $\Phi'_{t,P'}$ be the functions obtained by applying $P$ to $f_t$ and $P'$ to $f'_t$ in the normalized creation operators of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)): for $\Phi_{t,P}$ these are taken for the pair of spaces $(-A,B)$ with the matrices $(-s_A,s_B)$ and $(B_A,B_B)$, and for $\Phi'_{t,P'}$ for the pair $(A',B)$ with $(s_{A'},s_B)$ and $(B_{A'},B_B)$. For $h\in G_B(\mathbb A)$ put $$I_t(P)(h)=\int_{\mathfrak F}\bigl(\omega_t(g,h)\Phi_{t,P}\bigr)(0)\,dm(g),\qquad I'_t(P')(h)=\int_{\mathfrak F'}\bigl(\omega'_t(g,h)\Phi'_{t,P'}\bigr)(0)\,dm'(g).$$ A function $c^0\colon\mathcal T\to\mathbb C$ is a *constant of the triangle* (for $\psi$ and $\theta$) if $c^0(t)\ne0$ for some $t$ and there are $P$, $P'$ such that, for every $t\in\mathcal T$: both integrands are integrable for every $h$; the function $I'_t(P')$ is not identically zero; and $$I_t(P)(h)=c^0(t)\,I'_t(P')(h)\qquad\text{for all }h\in G_B(\mathbb A).$$

**The conditions of a triangle.** Let $\alpha_t$ and $\beta_t$ $(t\in\mathcal T)$ be characters of $\mathbb A_E^\times$ with values in the unit circle, $\nu_t$ $(t\in\mathcal T)$ Hecke characters of $E$, and $\Sigma(t)$ $(t\in\mathcal T)$ finite sets of finite places of $E$. A triangle *satisfies the conditions for* $(\psi,\theta,\alpha,\beta,\nu,\Sigma)$ if the following holds.

1. $\operatorname{rank}A+\operatorname{rank}A'=\operatorname{rank}B$.
2. For each $V\in\{A,A',B\}$: the lattice $\Lambda_V$ is self-dual; $\beta_V$ is a frame of $\Lambda_V$; and for every $\tau\in\Psi$, with $G_\tau$ the Gram matrix of $V$ under $\tau$, the matrix $s=s_V(\tau)$ satisfies $s^2=1$, $s^*G_\tau s=G_\tau$ and $G_\tau s$ is positive definite, and there is an integer $p\ge0$ such that $B=B_V(\tau)$ satisfies $B^*G_\tau B=\operatorname{diag}(1_p,-1_{n-p})$ and $sB=B\operatorname{diag}(1_p,-1_{n-p})$.
3. For every $t$, $\omega_t$ is a Weil representation for $\psi$, for the pair of spaces $(-A,B)$ and the splitting characters $(\beta_t,\ \beta_t/\alpha_t)$, and $\omega'_t$ is a Weil representation for $\psi$, for the pair $(A',B)$ and the splitting characters $(\alpha_t,\ \alpha_t/\beta_t)$, in the sense of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)).
4. The function $\phi$ is a normalized simultaneous vacuum, in the sense of that page, for the pair $(-A,B)$ with the Cartan involutions $(-s_A,s_B)$ and the lattices $(\Lambda_A,\Lambda_B)$; and $\phi'$ is one for the pair $(A',B)$ with $(s_{A'},s_B)$ and $(\Lambda_{A'},\Lambda_B)$.
5. For every $t$, $e_t$ is an idempotent with $e_t\bar e_t=0$ that is a sum of idempotents selecting the places of $\Sigma(t)$, one for each place; and for $w\in\Sigma(t)$, $n_t(w)$ is the conductor exponent of $\nu_t$ at $w$: the component of $\nu_t$ at $w$ is trivial on $1+\mathfrak p_w^{n}$ exactly for $n\ge n_t(w)$, where $1+\mathfrak p_w^0$ means $\mathcal O_{E_w}^\times$.
6. For every $t$, $f_t$ is the vector prescribed, in the sense of that page, on the half $e_tW(A,B)$ for the lattices $(\Lambda_A,\Lambda_B)$ by the vacuum $\phi$ and the function $\varphi_t$ defined below; and $f'_t$ is the vector prescribed on the half $\bar e_tW(A',B)$ for the lattices $(\Lambda_{A'},\Lambda_B)$ by the vacuum $\phi'$ and the function $\varphi'_t$ defined below.
7. $m$ and $m'$ are Haar measures, and $\mathfrak F$, $\mathfrak F'$ are fundamental domains for the translation actions of $G_A(F)$ and $G_{A'}(F)$ with respect to them.

The functions $\varphi_t$ and $\varphi'_t$ are defined as follows. Put $\lambda_t=\alpha_t/\beta_t$, $a=\operatorname{rank}A$, $a'=\operatorname{rank}A'$ and $I_t=\prod_{w\in\Sigma(t)}\mathfrak p_w^{\,n_t(w)}$. For a square matrix $M$ over $\mathbb A_{E,f}$ put $u_t(M)=\lambda_t(x)^{-1}$ if there is an idele $x$ of $E$ with archimedean part $1$ and finite part $1-e_t+e_t\det M$ whose inverse has integral finite part, and $u_t(M)=0$ otherwise. For $x\in W(A,B)$ let $M(x)=\beta_B^{-1}\,x_f\,\beta_A$, a matrix with $a+a'$ rows and $a$ columns, where $x_f$ is the finite part of $x$. Then $\varphi_t(x)=u_t(M_0)$, with $M_0$ the block of the first $a$ rows of $M(x)$, if $e_tx=x$, the entries of $M(x)$ are integral, and the entries of its last $a'$ rows lie in $\widehat{I_t}$; otherwise $\varphi_t(x)=0$. For $y\in W(A',B)$ let $$M'(y)=\xi_0\,\beta_{A'}^{-1}\,\bigl(G_{A'}^{-1}\,\bar y^{\mathsf T}\,G_B\bigr)_f\,\beta_B,$$ a matrix with $a'$ rows and $a+a'$ columns, where $G_{A'}$ and $G_B$ are the Gram matrices. Then $\varphi'_t(y)=u_t(M'_0)$, with $M'_0$ the block of the last $a'$ columns of $M'(y)$, if $\bar e_ty=y$, the entries of $M'(y)$ are integral, and the entries of its first $a$ columns lie in $\widehat{I_t}$; otherwise $\varphi'_t(y)=0$.

**The definite triangle of a square.** Let a grid with Weil data $(\psi,\theta,\dots)$ be given, and let $0\le i,j<m$. A triangle over the index set $\mathcal T$ of the family of characters is a *definite triangle of the square* $(i,j)$ if

1. $\operatorname{rank}A=\rho(i+1,j+1)-2\kappa_{j+1}$ and $\operatorname{rank}A'=\rho(i,j)-2\kappa_j$;
2. each of $A$, $A'$, $B$ has Gram matrix $1$ in its recorded basis, its lattice is $\mathcal O_E^{\,n}$ with $n$ its rank, and $s_V(\tau)=B_V(\tau)=1$ for all $\tau\in\Psi$;
3. it satisfies the conditions of a triangle for $\psi$, $\theta$ and $$\alpha_t=\mu^0_j\,\xi_t\,\eta^{\epsilon},\qquad \beta_t=\chi_{m-i}\,\eta^{\epsilon}\qquad(\epsilon=\rho(i,j)\bmod 2),\qquad \nu_t=\nu_{t,i,j},\qquad \Sigma(t)=W(t),$$ where $\alpha_t$ and $\beta_t$ are formed with the circle-valued characters that match $\mu^0_j$, $\xi_t$, $\eta$ and $\chi_{m-i}$.

In a definite triangle the three spaces are positive definite at every complex embedding of $E$, and $\operatorname{rank}B=\operatorname{rank}A+\operatorname{rank}A'$. Constants of a definite triangle are taken for the $\psi$ and $\theta$ of the Weil data.

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
