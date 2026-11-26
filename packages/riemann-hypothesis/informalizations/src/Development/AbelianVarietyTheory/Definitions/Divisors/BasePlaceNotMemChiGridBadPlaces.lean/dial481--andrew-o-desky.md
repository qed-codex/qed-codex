---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/BasePlaceNotMemChiGridBadPlaces.lean",
  "declarations": [
    "GlobalTheory.ChiGrid.GridData",
    "GlobalTheory.ChiGrid.GridData.Weil"
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

## Grids of Hermitian spaces with Weil data, and properties of all grids with large parameters

[Definition / hypothesis THETA.D092](https://andrewodesky.com/rh/lean/GlobalTheory.ChiGrid.GridData/)

A grid is a family of Hermitian spaces $V_{i,j}$, $0\le i,j\le m$, over a CM field, in which neighbouring spaces are joined in pairs and every pair carries a Hecke character. Weil data on a grid give every pair a Weil representation and test vectors. This page defines families of characters, grids, partial $L$-functions of Hecke characters, Weil data on a grid, and the phrase "for all large parameters".

**Setting.** Let $D$ be a datum of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). It contains the CM field $E$ with its subfield $F$ and its quadratic subfield $E_0$, the integers $k$, $m$, $f$ and $r=k+m-1$, the generator primes $g_0,g_1$ and the auxiliary primes of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)); the odd integer $t$ of that page is written $t_0$ here, and its auxiliary primes $p_\Delta,p'_\Delta$ are written $p_\delta,p'_\delta$, as in ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). The datum also contains the coefficient field $K$ with its embedding $\jmath\colon K\to\mathbb C$ of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), the fixed CM type $\Psi$ of $E$, the distinguished imaginary element $\xi_0\in E$, and the Hermitian spaces $Y_j$ $(0\le j<m)$ and $X'$ of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). Write $x\mapsto\bar x$ for complex conjugation on $E$ and on $\mathbb A_E=\mathbb A_F\otimes_FE$, and $\mathbb A_{E,f}$ for the finite part of $\mathbb A_E$. Let $\mathfrak A=\mathfrak c\,\mathcal O_E\cdot\mathfrak b^{-1}$ be the fractional ideal of $E$ formed from the ideal $\mathfrak c$ of $E_0$ and the integral ideal $\mathfrak b$ of $E$ that belong to the fields of $D$, and let $\bar{\mathfrak A}$ be its complex conjugate.

A Hermitian space over $E$ is taken with a recorded basis, as in ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), and matrices are written in this basis. For such a space $V$, $G_V(\mathbb A)$ is its unitary group over $\mathbb A_F$ and $G_V(F)$ is the subgroup of rational points; $-V$ is the same space with the negative of its form, so that $G_{-V}=G_V$. A *space with lattice* is a Hermitian space $V$ with an $\mathcal O_E$-submodule $\Lambda(V)\subset V$. The lattice is *self-dual* if it is a full lattice and $\Lambda(V)=\{y\in V:h(x,y)\in\mathcal O_E\text{ for all }x\in\Lambda(V)\}$. For Hermitian spaces $S$ and $T$ put $$W(S,T)=M_{\operatorname{rank}T\times\operatorname{rank}S}(\mathbb A_E).$$ For integers $i,j\ge0$ put $$\rho(i,j)=r+j\,t_0+i\,(r+6),\qquad \kappa_j=\Bigl⌊\frac{m-j}{2}\Bigr⌋\quad(0\le j\le m).$$

**Families of characters.** A Hecke character of $E$ is a continuous homomorphism from the idele group of $E$ to $\mathbb C^\times$ that is trivial on $E^\times$. A *family of characters* for $D$ consists of

- a set $\mathcal T$ and a *base index* $\mu_0\in\mathcal T$;
- a character frame for $D$ in the sense of ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)), whose Hecke characters $\mu_{0,j}$ $(0\le j<m)$, $\eta$, $\delta$, $\delta'$ are written $\mu^0_j$, $\eta$, $\delta$, $\delta'$ here;
- a Hecke character $\xi_t$ of $E$ and a finite set $Q(t)$ of finite places of $E$ for every $t\in\mathcal T$, and a finite set $P_g$ of finite places of $E$;
- the further data of ([Finite levels and character matching](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.LevCh.Is/)): characters of $\mathbb A_E^\times$ with values in the unit circle, one for each $\mu^0_j$, for $\eta$ and for each $\xi_t$; residue characters at the places of $P_g$ and of $Q(t)$; lattices $\Lambda_{Y,j}\subset Y_j$ and $\Lambda_X\subset X'$ and lattices in the spaces $V_j$, $W_j$ of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)); and a frame of each of these lattices. A *frame* of a lattice $\Lambda$ in a space of rank $n$ is a matrix $\beta\in\mathrm{GL}_n(\mathbb A_{E,f})$ with $\widehat\Lambda=\beta\,\widehat{\mathcal O}_E^{\,n}$.

These data are subject to the conditions of ([Finite levels and character matching](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.LevCh.Is/)) on the matching of the circle-valued characters with the Hecke characters, on the characters $\xi_t$, on the sets $P_g$ and $Q(t)$, on the residue characters and on the frames, which are all the conditions that precede the finite-group identification on that page; the base tuple $t_0$ of that page is $\mu_0$, its $\mu^H_{j+1}$ is $\mu^0_j$, and its $Q_t$ is $Q(t)$. Among these conditions: the map $t\mapsto\xi_t$ is injective, $\xi_{\mu_0}=1$, every $\xi_t$ has finite order, and $\xi_t$ is ramified exactly at the places of $Q(t)$ and their complex conjugates. A circle-valued character that matches a Hecke character is denoted by the same letter.

**Grids.** Let a family of characters for $D$ and real numbers $c_1,c_2,c_3$ be given. A *grid* for the family with constants $(c_1,c_2,c_3)$ consists of places, characters and spaces with the following properties.

*Places.* Let $S_1$ be the set of finite places of $F$ that divide $g_0g_1p_\delta p'_\delta$, and let $q_0$ be the rational prime so denoted in ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)). The places of the grid are a finite place $v_0$ of $F$ above $q_0$ and a finite place $w(v)$ of $E$ for every finite place $v$ of $F$. Put $S_0=S_1\cup\{v_0\}$ and $W_0=\{w(v):v\in S_0\}$. The conditions are:

1. for $v\in S_0$, the place $w(v)$ lies above $v$, and there is an idempotent $e\in\mathbb A_E$ selecting $w(v)$, in the sense of ([Finite levels and character matching](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.LevCh.Is/)), with $e\bar e=0$ (so $v$ splits in $E$);
2. $w(v)\in P_g$ for every $v$ that divides $g_0$ or $g_1$;
3. for each $p\in\{p_\delta,p'_\delta\}$ there is a prime $\mathfrak p$ of $E_0$ such that $w(v)$ lies above $\mathfrak p$ for every $v$ dividing $p$;
4. for every $t\in\mathcal T$, a place of $Q(t)$ that lies above a place $v\in S_1$ is equal to $w(v)$, and no place of $Q(t)$ lies above $v_0$.

For $v\in S_0$ put $\ell(v)=2$ if $v\ne v_0$ and $$\ell(v_0)=\Bigl⌊\frac{c_2\,f^2\,(r+1)^6\,\log\bigl(c_3\,(r+1)\,g_0g_1p_\delta p'_\delta\,|\operatorname{disc}E|\bigr)}{\log q_0}\Bigr⌋+1 .$$ The *modulus* of the grid is the ideal $\mathfrak m=\prod_{v\in S_0}w(v)^{\ell(v)}$ of $\mathcal O_E$. For $t\in\mathcal T$ put $$W(t)=W_0\cup Q(t),\qquad N_t=\prod_{w\in Q(t)\setminus W_0}N(w),\qquad a(v)=\begin{cases}1,&v=v_0,\\2,&v\in S_1,\end{cases}$$ where $N(w)$ is the cardinality of the residue field of $w$. For a finite place $w$ of $E$ put $\ell(w)=\ell(v)$ if $w=w(v)$ with $v\in S_0$, and $\ell(w)=1$ otherwise.

*Characters.* For $1\le i\le m$ the grid has a Hecke character $\chi_i$ of $E$ and a character of $\mathbb A_E^\times$ with values in the unit circle that matches it and is denoted by the same letter. For each $i$:

1. the restriction of $\chi_i$ to $F$ is trivial, in the sense of ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/));
2. there are integers $c_\tau(i)$, $\tau\in\Psi$, with $\chi_{i,\infty}(x)=\prod_{\tau\in\Psi}\bigl(\tau(x)/|\tau(x)|\bigr)^{2c_\tau(i)}$ for $x\in E^\times$; the integers $c_\tau(i)$ are determined by the weight arrays of $D$ and the constant $c_1$, by a rule that this page does not reproduce;
3. $\chi_i$ is unramified at every finite place of $E$ that does not lie above $S_0$;
4. at a place $w$ above $v\in S_0$, the local component $\chi_{i,w}$ is trivial on $1+\mathfrak p_w^{a(v)}$; it is nontrivial on $1+\mathfrak p_w$ if $v\in S_1$ and nontrivial on $\mathcal O_{E_w}^\times$ if $v=v_0$;
5. at a place $w$ above $p_\delta$ or $p'_\delta$, $\chi_{i,w}(x)=1$ for every $x\in E_w^\times$ with $x^{N(w)-1}=1$.

Thus $a(v)$ is the conductor exponent of every $\chi_i$ at the places above $v\in S_0$. For $0\le i,j<m$ and $t\in\mathcal T$ put $$\nu_{t,i,j}=\mu^0_j\,\xi_t\,/\,\chi_{m-i}.$$

*Partial $L$-functions.* For a Hecke character $\chi$ of $E$ that is unramified at a finite place $w$, $\chi_w(\varpi_w)$ is the value of its component at $w$ on a uniformizer. The *partial $L$-function* of a Hecke character $\chi$ of $E$ is an entire function $\Lambda$ such that, for $\operatorname{Re}s>1$, $$\Lambda(s)=\prod_{w}\bigl(1-\chi_w(\varpi_w)\,N(w)^{-s}\bigr)^{-1},$$ where the product runs over the finite places $w$ of $E$ at which $\chi$ is unramified and converges. A Hecke character has at most one partial $L$-function.

*Spaces.* An *orthogonal extension* of a Hermitian space $A$ to a Hermitian space $B$ by $n$ vectors with sign $\epsilon\in\{1,-1\}$ consists of an isometric linear map $\iota\colon A\to B$ and vectors $a_1,\dots,a_n\in B$ orthogonal to $\iota(A)$, where $\operatorname{rank}A+n=\operatorname{rank}B$ and $$h_B(a_p,a_q)=\begin{cases}1,&p+q=n+1,\ p\ne q,\\ \epsilon,&p+q=n+1,\ p=q,\\ 0,&p+q\ne n+1.\end{cases}$$ The grid has spaces with lattice $V_{i,j}$ $(1\le i\le m,\ 0\le j\le m)$, $C_i$ $(0\le i\le m)$ and $U_j$ $(1\le j\le m)$; in addition $V_{0,j}=Y_j$ with the lattice $\Lambda_{Y,j}$ for $0\le j<m$, $V_{0,m}=X'$ with the lattice $\Lambda_X$, and $U_0=C_m$. The conditions are as follows; the signature recorded with each space is required to be the signature of its form.

1. For $1\le i\le m$ and $0\le j\le m$, the space $V_{i,j}$ has rank $\rho(i,j)$ and signature $(\rho(i,j)-\kappa_j,\ \kappa_j)$ at every complex embedding of $E$, and its lattice is self-dual.
2. For $0\le i\le m$, the space $C_i$ has rank $r+1+i\,(r+5)$ and negative index $\lfloor(m-i+1)/2\rfloor$ at every complex embedding, and its lattice is self-dual.
3. For $1\le j\le m$, the space $U_j$ has rank $r+1+m\,(r+5)+j\,(t_0+1)$, is positive definite at every complex embedding, and its lattice is self-dual.
4. There is an orthogonal extension of $Y_0$ to $C_0$ by one vector with sign $1$, and $\Lambda(C_0)=\iota(\Lambda_{Y,0})+\mathcal O_E\,a_1$.
5. For $1\le i\le m$ there is an orthogonal extension of $C_i$ to $V_{i,0}$ by $i-1$ vectors with sign $-1$, and $$\Lambda(V_{i,0})=\iota(\Lambda(C_i))+\sum_{p=1}^{i-1}\mathfrak a^{\,i-p}\,\mathfrak a'^{\,-p}\,a_p,\qquad \mathfrak a=\mathfrak A\,\bar{\mathfrak m}^{-1},\quad \mathfrak a'=\bar{\mathfrak A}\,\mathfrak m^{-1}.$$
6. For $1\le j<m$ there is an orthogonal extension of $U_j$ to $V_{m,j}$ by $n=m-1-j$ vectors with sign $-1$, and $\Lambda(V_{m,j})=\iota(\Lambda(U_j))+\sum_{p=1}^{n}\mathfrak A^{\,n+1-p}\,\bar{\mathfrak A}^{\,-p}\,a_p$.
7. There is an orthogonal extension of $V_{m,m}$ to $U_m$ by one vector with sign $1$, and $\Lambda(U_m)=\iota(\Lambda(V_{m,m}))+\mathcal O_E\,a_1$.

The orthogonal extensions in 4 to 7 are part of the grid. The spaces $V_{i,j}$, $C_i$, $U_j$ are the *nodes* of the grid.

**Pairs and their characters.** A *pair* of the grid consists of two nodes, a smaller one and a bigger one, and a character of $\mathbb A_E^\times$ with values in the unit circle. There are four kinds of pairs.

- Pairs of the first kind: $(V_{i,j},V_{i+1,j})$ for $0\le i<m$, $0\le j\le m$, with the character $\chi_{m-i}$.
- Pairs of the second kind, for $t\in\mathcal T$: $(V_{i,j},V_{i,j+1})$ for $0\le i\le m$, $0\le j<m$, with the character $\mu^0_j\,\xi_t$.
- The pairs $(C_i,C_{i+1})$ for $0\le i<m$, with the character $\chi_{m-i}$.
- For $t\in\mathcal T$, the pairs $(U_j,U_{j+1})$ for $0\le j<m$, with the character $\mu^0_j\,\xi_t$.

To a pair $p$ with smaller node $V$, bigger node $V'$ and character $\chi$ we attach two Hermitian spaces: $(S_p,T_p)=(-V',V)$ if $\chi$ is one of the $\chi_i$, and $(S_p,T_p)=(V,V')$ otherwise. Its *splitting characters* are $\chi_{S}=\chi\,\eta^{-\epsilon_S}$ and $\chi_{T}=\chi\,\eta^{-\epsilon_T}$, where $\epsilon_S,\epsilon_T\in\{0,1\}$ are the ranks of $S_p$ and $T_p$ modulo $2$.

**Weil data.** *Weil data* on a grid consist of the following.

1. An additive character $\psi$ of $\mathbb A_F$ that is standard, and a compatible family $\theta=(\theta_\tau)_{\tau\in\Psi}$ of ring homomorphisms $\mathbb A_{F,\infty}\otimes_FE\to\mathbb C$, both in the sense of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)). Compatible means that $\theta_\tau(1\otimes x)=\tau(x)$ for $x\in E$ and that $a\mapsto\theta_\tau(a\otimes1)$ is continuous. Standard means that $\psi$ is continuous, unitary, trivial on $F$ and nontrivial, that compatible families exist, and that for every compatible family $(\theta'_\tau)$ and every $a\in\mathbb A_{F,\infty}$ $$\psi(a)=\exp\Bigl(-2\pi i\sum_{\tau\in\Psi}\theta'_\tau(a\otimes1)\Bigr).$$
2. For every node $V$ and every $\tau\in\Psi$, with $G_\tau$ the Gram matrix of $V$ under $\tau$: a Cartan involution $s_V(\tau)$, which is a complex matrix with $s^2=1$, $s^*G_\tau s=G_\tau$ and $G_\tau s$ positive definite; and an invertible complex matrix $B_V(\tau)$ such that, for some diagonal matrix $J$ with entries $\pm1$, $B^*G_\tau B=J$ and $sB=BJ$.
3. For every pair $p$, a representation $\omega_p$ of $G_{S_p}(\mathbb A)\times G_{T_p}(\mathbb A)$ on the space of complex functions on $W(S_p,T_p)$ that is a Weil representation for $\psi$ and the splitting characters $(\chi_S,\chi_T)$ of $p$, in the sense of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)).
4. For $0\le i<m$, with $p$ the pair $(V_{i,0},V_{i+1,0})$: a function $\phi_i$ on $W(S_p,T_p)$ that is a normalized simultaneous vacuum, in the sense of the same page, for the Cartan involutions $(-s_{V_{i+1,0}},\,s_{V_{i,0}})$ and the lattices $(\Lambda(V_{i+1,0}),\Lambda(V_{i,0}))$.
5. For $0\le i<m$, let $H_i$ be the $\mathcal O_E$-module of matrices that map $\Lambda(V_{i+1,0})$ into $\Lambda(V_{i,0})$. For every class $y\in H_i/\mathfrak mH_i$ the Weil data contain a function $\phi_{i,y}$ on $W(S_p,T_p)$. There is an idempotent $e\in\mathbb A_E$ with $e\bar e=0$ that is a sum of idempotents selecting the places of $W_0$, one for each place, such that for all $i$ and $y$ the function $\phi_{i,y}$ is the vector prescribed, in the sense of the same page, on the half $eW(S_p,T_p)$, for the lattices $(\Lambda(V_{i+1,0}),\Lambda(V_{i,0}))$, by the vacuum $\phi_i$ and the characteristic function of the set $$\{x: x=ex,\ x-e\,x_0\in\widehat{\mathfrak mH_i}\ \text{for some }x_0\in H_i\text{ in the class }y\}.$$

A *test function* for a pair $p$ is a complex function on $W(S_p,T_p)$. Its *kernel* is the function of $g\in G_V(\mathbb A)$ and $h\in G_{V'}(\mathbb A)$, with $V$ the smaller and $V'$ the bigger node of $p$, given by $$k_p(f;g,h)=\bigl(\omega_p(g_S,g_T)f\bigr)(0),$$ where $(g_S,g_T)=(h,g)$ for a pair whose character is one of the $\chi_i$ and $(g_S,g_T)=(g,h)$ otherwise.

**Properties of all grids with large parameters.** Size data for $D$ are those of ([Local size and support data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.SizeData%E2%82%82/)); they include real numbers $x>1$ and $0<\varepsilon<1/52$, and we put $b=\exp(x^{\varepsilon})$. The *standing conditions* on $D$ with size data are:

1. $F$ is the maximal real subfield of $E$;
2. $|\operatorname{Re}\,(\mathcal L_d'/\mathcal L_d)(1)|\le x^{\varepsilon}$, where $\mathcal L_d(s)$ is the Dirichlet $L$-function of the quadratic character modulo the prime $d$ of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/));
3. Hypothesis (weight gaps for analytic comparisons) of ([Weight gaps for analytic comparisons](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.HostHyp/));
4. the conditions of ([Numerical size conditions for family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.SizesAt/)); the existence of a choice of parameters for $D$ and its size data, one of whose constants is equal to $10$, with theta parameters for this choice in the sense of ([Theta parameters and precision inequalities](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ParamsT/)); and inequalities between the ranks, the primes, the weight arrays and the size data, among them $$44\le m,\qquad m^4\le f,\qquad f\,m\le(r+1)^3,\qquad \log g_a\le 9x^{\varepsilon}+1\ (a=0,1),\qquad \log q_0\le x^{\varepsilon},$$ $$x^2\,m^3\,x^{\varepsilon}\,\log\operatorname{rd}_E\le k,\qquad m\,f\,(k+m(t_0+1))^2\,d\le b,$$ and that the ideal $\mathfrak c$ is the unit ideal. This page does not list the remaining inequalities of this item.

A property $\mathcal Q$ of grids, each taken with its family of characters and its base index, is said to hold *for all large parameters* if there is a real number $C_F^0$ such that for all real numbers $\varepsilon$ and $C_F\ge C_F^0$ there is a real number $x_0$ with the following property: $\mathcal Q$ holds for every datum $D$ with size data that have the given $\varepsilon$, satisfy $x\ge x_0$ and satisfy the standing conditions, every family of characters for $D$, and every grid for the family with constants $(1,C_F,b)$.
