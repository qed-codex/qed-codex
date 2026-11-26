---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/BplusOfEquivariant.lean",
  "declarations": [
    "GlobalTheory.FunObj.Vol.Is"
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

## Square constants of a grid: matched test data and normalised measures

[Definition / hypothesis THETA.D090](https://andrewodesky.com/rh/lean/GlobalTheory.FunObj.IsSquareConst/)

In a grid, two paths of two pairs lead from $V_{i,j+1}$ to $V_{i+1,j}$: one through $V_{i+1,j+1}$ and one through $V_{i,j}$. A square constant is a complex number $c$ such that the integral of a product of two theta kernels along the first path is $c$ times the corresponding integral along the second path, for all test data on the two paths that are matched. This page defines matched test data, the measures used in the integrals, square constants, and non-degenerate squares.

Throughout, a grid with Weil data is given, in the sense and with the notation of ([Grids of Hermitian spaces with Weil data, and properties of all grids with large parameters](https://andrewodesky.com/rh/lean/GlobalTheory.ChiGrid.GridData/)): the spaces $V_{i,j}$ of ranks $\rho(i,j)$, the pairs $p$ with their spaces $(S_p,T_p)$, the family of characters $(\xi_t)_{t\in\mathcal T}$, the sets of places $W(t)$, the exponents $\ell(w)$, the characters $\nu_{t,i,j}$, and the Weil data $\psi$, $\theta$, $s_V$, $B_V$, $\omega_p$, $\phi_i$ with the kernels $k_p$.

**Adelic bases.** *Adelic bases* of the grid consist of a frame $\beta_{i,j}$ of the lattice $\Lambda(V_{i,j})$ for $1\le i\le m$ and $0\le j\le m$. For $i=0$ let $\beta_{0,j}$ be the frame of $\Lambda_{Y,j}$ $(j<m)$ or of $\Lambda_X$ $(j=m)$ that belongs to the family of characters.

**Polynomial test functions.** For a pair $p$ let $\mathrm{Pol}_p$ be the ring of complex polynomials in the variables $z_{\tau,a,b}$, where $\tau\in\Psi$, $1\le a\le\operatorname{rank}T_p$ and $1\le b\le\operatorname{rank}S_p$. For a function $f$ on $W(S_p,T_p)$ and $P\in\mathrm{Pol}_p$, let $\Phi_p(f,P)$ be the function on $W(S_p,T_p)$ obtained by applying $P$ in the normalized creation operators to $f$, as in ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)), for the Cartan involutions and the bases of the Weil data at the two nodes of $p$; when $S_p=-V'$, the Cartan involution of $S_p$ is $-s_{V'}$ and its basis is $B_{V'}$.

**Archimedean matching data.** *Archimedean matching data* for the Weil data consist of the following.

1. For every pair $p=(V_{i,j},V_{i+1,j})$ of the first kind, a function $v_p$ on $W(S_p,T_p)$ that is a normalized simultaneous vacuum, in the sense of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)), for the Cartan involutions $(-s_{V_{i+1,j}},s_{V_{i,j}})$ and the lattices $(\Lambda(V_{i+1,j}),\Lambda(V_{i,j}))$; for $j=0$ it is the function $\phi_i$ of the Weil data.
2. For $0\le i\le m$ and $0\le j<m$, a function $v'_{i,j}$ on $W(V_{i,j},V_{i,j+1})$ that is a normalized simultaneous vacuum for the Cartan involutions $(s_{V_{i,j}},s_{V_{i,j+1}})$ and the lattices $(\Lambda(V_{i,j}),\Lambda(V_{i,j+1}))$. It serves for the pair $(V_{i,j},V_{i,j+1})$ of the second kind for every $t\in\mathcal T$.
3. For $0\le i,j<m$, a complex linear subspace $$R_{i,j}\subset\bigl(\mathrm{Pol}_{p_1}\otimes\mathrm{Pol}_{p_2}\bigr)\times\bigl(\mathrm{Pol}_{p'_1}\otimes\mathrm{Pol}_{p'_2}\bigr),$$ where $p_1,p_2$ and $p'_1,p'_2$ are the pairs of the two paths of the square $(i,j)$ defined below. Both projections of $R_{i,j}$ are surjective, and $R_{i,j}$ is a proper subspace.

**Squares, paths and kernels.** Let $0\le i,j<m$ and $t\in\mathcal T$. The *square* $(i,j)$ consists of the four spaces $V_{i,j}$, $V_{i,j+1}$, $V_{i+1,j}$, $V_{i+1,j+1}$. Its *big path* consists of the pairs $$p_1=(V_{i,j+1},V_{i+1,j+1})\ \text{(first kind)},\qquad p_2=(V_{i+1,j},V_{i+1,j+1})\ \text{(second kind, for }t),$$ and its *small path* of the pairs $$p'_1=(V_{i,j},V_{i,j+1})\ \text{(second kind, for }t),\qquad p'_2=(V_{i,j},V_{i+1,j})\ \text{(first kind)}.$$ *Test data* on a path are a finitely supported complex function $\Theta$ on the set of pairs $(f_1,f_2)$, where $f_1$ and $f_2$ are test functions for the first and the second pair of the path. For test data $\Theta$ on the big path and $\Theta'$ on the small path, and for $g\in G_{V_{i,j+1}}(\mathbb A)$ and $g_1\in G_{V_{i+1,j}}(\mathbb A)$, put $$\mathcal K^{\mathrm{big}}_\Theta(g,u,g_1)=\sum_{(f_1,f_2)}\Theta(f_1,f_2)\,k_{p_1}(f_1;g,u)\,k_{p_2}(f_2;g_1,u)\qquad(u\in G_{V_{i+1,j+1}}(\mathbb A)),$$ $$\mathcal K^{\mathrm{small}}_{\Theta'}(g,u,g_1)=\sum_{(f_1,f_2)}\Theta'(f_1,f_2)\,k_{p'_1}(f_1;u,g)\,k_{p'_2}(f_2;u,g_1)\qquad(u\in G_{V_{i,j}}(\mathbb A)).$$ In each kernel the first group variable belongs to the smaller space of the pair and the second to the bigger one.

**The local transform.** Let $w\in W(t)$, let $E_w$ be the completion of $E$ at $w$ with ring of integers $\mathcal O_w$, normalized absolute value $|\cdot|_w$ and residue cardinality $q_w$, and let $\varpi_w$ be the uniformizer of $E_w$ that is fixed once for every place. Let $\psi_w(x)=\psi(\operatorname{Tr}_{\mathbb A_E/\mathbb A_F}(\xi_0\,x))$ for $x\in E_w\subset\mathbb A_E$, and let $\nu_w$ be the component at $w$ of $\nu_{t,i,j}$. Put $$a'=\rho(i,j),\quad a=\rho(i+1,j+1),\quad d_1=\rho(i,j+1),\quad d_2=\rho(i+1,j),\quad d=d_1+d_2=a+a'.$$ A matrix with $d$ columns is written $(Y_1\mid Y_2)$, with $Y_1$ its first $d_1$ columns. For an integer $n\ge0$ and a function $\Phi$ on $M_{a'\times d}(E_w)$, the function $\mathcal F^{(n)}_w\Phi$ on $M_{a\times d}(E_w)$ is defined in three steps.

1. For $Y\in M_{a'\times d}(E_w)$ put $\Phi_1(Y)=0$ unless $\varpi_w^nY_1$ has entries in $\mathcal O_w$, and in that case $$\Phi_1(Y)=q_w^{-na'd_1}\sum_{T}\Phi(T\mid Y_2)\,\psi_w\bigl(\operatorname{tr}(T\,Y_1^{\mathsf T})\bigr),$$ where $T$ runs over a fixed set of representatives in $M_{a'\times d_1}(\mathcal O_w)$ of the classes modulo $\varpi_w^n$.
2. Let $L=\mathcal O_w^{d_1}\oplus\varpi_w^{-n}\mathcal O_w^{d_2}$, let $X_0=(1_a\mid0)\in M_{a\times d}(E_w)$ and $Y_0=(0\mid1_{a'})\in M_{a'\times d}(E_w)$, and let $\mu$ be the Haar measure on $\mathrm{GL}_{a'}(E_w)$ for which the group $\{(g^{\mathsf T})^{-1}:g\in J_w\}$ has measure $1$, with $J_w$ as below. For $X\in M_{a\times d}(E_w)$ put $\Phi_2(X)=0$ unless $X$ has rank $a$, its rows lie in $L$, and the $\mathcal O_w$-span of its rows is the intersection of their $E_w$-span with $L$. In that case choose $h\in\mathrm{GL}_d(E_w)$ with $X=X_0\,(h^{\mathsf T})^{-1}$ and put $$\Phi_2(X)=\nu_w(\det h)\,|\det h|_w^{d/2}\int_{\mathrm{GL}_{a'}(E_w)}\Phi_1(g\,Y_0\,h)\,\nu_w(\det g)\,|\det g|_w^{d/2}\,d\mu(g).$$
3. For $X\in M_{a\times d}(E_w)$ put $(\mathcal F^{(n)}_w\Phi)(X)=0$ unless $X_2$ has entries in $\mathcal O_w$, and in that case $$(\mathcal F^{(n)}_w\Phi)(X)=\sum_{S}\Phi_2\bigl(X_1\mid\varpi_w^{-n}S\bigr)\,\psi_w\bigl(\varpi_w^{-n}\operatorname{tr}(S\,X_2^{\mathsf T})\bigr),$$ where $S$ runs over the fixed set of representatives in $M_{a\times d_2}(\mathcal O_w)$ of the classes modulo $\varpi_w^n$.

The compact open subgroup $J_w\subset\mathrm{GL}_{a'}(E_w)$ is $\mathrm{GL}_{a'}(\mathcal O_w)$ if $i\ge1$ and $j\ge1$. If $j=0$, it is the group of $g\in\mathrm{GL}_{a'}(\mathcal O_w)$ with $g\equiv1$ modulo $\varpi_w^{\ell(w)}$ when $w\in W_0$, and $\mathrm{GL}_{a'}(\mathcal O_w)$ when $w\notin W_0$. If $i=0$ and $j\ge1$, it is a compact open subgroup determined by the family of characters, by $t$, $j$ and $w$; this page does not reproduce its definition.

**Matched test data.** Let adelic bases $\beta$ and archimedean matching data $\varrho=(v,v',R)$ be given, and let $0\le i,j<m$ and $t\in\mathcal T$. For a pair $p$, an idempotent $e\in\mathbb A_E$, a function $f_0$ and functions $\varphi$, $f$ on $W(S_p,T_p)$, say that $f$ is *prescribed by* $(e,f_0,\varphi)$ if $\varphi$ has bounded integral support on the half $eW(S_p,T_p)$ and $f$ is the vector prescribed on this half by the vacuum $f_0$ and the test function $\varphi$, both in the sense of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)) for the lattices of the two nodes of $p$. For $x\in W(S,T)$ and a finite place $w$, $x_w$ is the component of $x$ at $w$.

Test data $\Theta$ on the big path and $\Theta'$ on the small path of the square $(i,j)$ are *matched* at $t$ if there are

- finitely supported complex functions $A$ on $\mathrm{Pol}_{p_1}\times\mathrm{Pol}_{p_2}$ and $A'$ on $\mathrm{Pol}_{p'_1}\times\mathrm{Pol}_{p'_2}$,
- test data $\vartheta$ on the big path and $\vartheta'$ on the small path,
- for every $w\in W(t)$ an integer $n_w\ge\ell(w)$ and a function $\Phi_w$ on $M_{a'\times d}(E_w)$ that vanishes outside $M_{a'\times d}(\mathcal O_w)$ and is invariant under translation by $\varpi_w^{n_w}M_{a'\times d}(\mathcal O_w)$,
- an idempotent $e\in\mathbb A_E$ with $e\bar e=0$ that is a sum of idempotents selecting the places of $W(t)$, one for each place,

with the following four properties.

1. $\bigl(\sum A(P_1,P_2)\,P_1\otimes P_2,\ \sum A'(P'_1,P'_2)\,P'_1\otimes P'_2\bigr)\in R_{i,j}$.
2. For every $(f_1,f_2)$ in the support of $\vartheta'$ there are functions $\varphi_1,\varphi_2$ such that $f_1$ is prescribed by $(e,v'_{i,j},\varphi_1)$ for the pair $p'_1$, $f_2$ is prescribed by $(e,v_{p'_2},\varphi_2)$ for the pair $p'_2$, and for all $x_1\in W(S_{p'_1},T_{p'_1})$, $x_2\in W(S_{p'_2},T_{p'_2})$ with $ex_1=x_1$ and $ex_2=x_2$ $$\sum_{(f_1,f_2)}\vartheta'(f_1,f_2)\,\varphi_1(x_1)\,\varphi_2(x_2)=\prod_{w\in W(t)}\Phi_w\Bigl(\bigl(\beta_{i,j+1}^{-1}\,x_{1,w}\,\beta_{i,j}\bigr)^{\mathsf T}\ \Big|\ \beta_{i,j}^{-1}\,x_{2,w}\,\beta_{i+1,j}\Bigr).$$
3. For every $(f_1,f_2)$ in the support of $\vartheta$ there are functions $\varphi_1,\varphi_2$ such that $f_1$ is prescribed by $(e,v_{p_1},\varphi_1)$ for the pair $p_1$, $f_2$ is prescribed by $(e,v'_{i+1,j},\varphi_2)$ for the pair $p_2$, and for all $x_1\in W(S_{p_1},T_{p_1})$, $x_2\in W(S_{p_2},T_{p_2})$ with $ex_1=x_1$ and $ex_2=x_2$ $$\sum_{(f_1,f_2)}\vartheta(f_1,f_2)\,\varphi_1(x_1)\,\varphi_2(x_2)=\prod_{w\in W(t)}\bigl(\mathcal F^{(n_w)}_w\Phi_w\bigr)\Bigl(\bigl(\beta_{i,j+1}^{-1}\,x_{1,w}\,\beta_{i+1,j+1}\bigr)^{\mathsf T}\ \Big|\ \beta_{i+1,j+1}^{-1}\,x_{2,w}\,\beta_{i+1,j}\Bigr).$$
4. $\Theta=A\otimes\vartheta$ and $\Theta'=A'\otimes\vartheta'$, where $A\otimes\vartheta$ is the test data $$A\otimes\vartheta=\sum_{(P_1,P_2)}\ \sum_{(f_1,f_2)}A(P_1,P_2)\,\vartheta(f_1,f_2)\,\bigl[\Phi_{p_1}(f_1,P_1),\ \Phi_{p_2}(f_2,P_2)\bigr],$$ $[f,f']$ denoting the test data with value $1$ at $(f,f')$ and $0$ elsewhere, and $A'\otimes\vartheta'$ is defined in the same way with $p'_1$, $p'_2$.

In 2 and 3 the frames act through their components at $w$, and in the sums the functions $\varphi_1,\varphi_2$ are those chosen for $(f_1,f_2)$.

**Normalised measures.** A *system of measures* on the grid consists of a measure $\nu_V$ on $G_V(\mathbb A)$ and a subset $\mathfrak F_V\subset G_V(\mathbb A)$ for every node $V$ of the grid, and a measure with a subset on the group of adelic points of a unipotent group $N$ attached to the orthogonal extension of $C_m$ to $V_{m,0}$. For $t\in\mathcal T$ and a node $V$, let $K_V(t)$ be the following subgroup of the finite part of $G_V(\mathbb A)$:

- for $V=V_{i,0}$ $(0\le i\le m)$ and for $V=C_i$ $(0\le i\le m)$: the elements that stabilise the completed lattice $\widehat{\Lambda(V)}$ and act trivially on $\widehat{\Lambda(V)}/\mathfrak m\,\widehat{\Lambda(V)}$;
- for $V=V_{0,j}$ $(1\le j\le m)$: the level subgroup of $Y_j$, or of $X'$ if $j=m$, defined in ([Finite levels and character matching](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.LevCh.Is/)) for the index $t$ with the trivial subgroup-character pair;
- for $V=V_{i,j}$ with $i,j\ge1$ and for $V=U_j$ $(1\le j\le m)$: the stabiliser of $\widehat{\Lambda(V)}$.

The system is *normalised at $t$* if the following holds.

1. For every node $V$, $\nu_V$ is a Haar measure and $\mathfrak F_V$ is a fundamental domain for the translation action of $G_V(F)$ with respect to $\nu_V$.
2. For every node $V$, with signature $(p_\tau,q_\tau)$ and Gram matrix $G_\tau$ at $\tau\in\Psi$: there exist a compatible family $(\theta_\tau)$, complex matrices $A_\tau$ with $A_\tau^*\,I_{p_\tau,q_\tau}A_\tau=G_\tau$, and admissible Haar measures $m_\tau$ on the real unitary groups $U(p_\tau,q_\tau)$, and for all such choices and all measurable sets $\mathcal B_\tau\subset U(p_\tau,q_\tau)$ $$\nu_V\bigl\{h:\ h_f\in K_V(t),\ A_\tau\,h_\tau\,A_\tau^{-1}\in\mathcal B_\tau\text{ for all }\tau\bigr\}=\prod_{\tau\in\Psi}m_\tau(\mathcal B_\tau).$$ Here $I_{p,q}$ is the Hermitian matrix of signature $(p,q)$ that defines $U(p,q)$, $h_f$ is the finite part of $h$, and $h_\tau$ is the matrix of the archimedean part of $h$ under $\theta_\tau$. A Haar measure on $U(p_\tau,q_\tau)$ is admissible if it is a probability measure, in the case of a node $V_{i,j}$ with $\kappa_j=0$, of $C_m$ and of every $U_j$; for the other nodes it is admissible if its density at the identity, with respect to a normalised Lebesgue measure on the Lie algebra, is $2^{-n(n-1)/2}$, $n=\operatorname{rank}V$. This page does not reproduce the normalisation of that Lebesgue measure.
3. The measure on $N(\mathbb A)$ is a Haar measure, and its subset is a fundamental domain for $N(F)$ of measure $1$. This page does not reproduce the definition of $N$.

**Square constants.** Let adelic bases and archimedean matching data be given, and let $0\le i,j<m$ and $t\in\mathcal T$. A complex number $c$ is a *square constant* at $(t,i,j)$ if $$\Bigl(\sum_{y}z(y)\Bigr)\int_{\mathfrak F_{V_{i+1,j+1}}}\mathcal K^{\mathrm{big}}_\Theta(g,u,g_1)\,d\nu(u) = c\int_{\mathfrak F_{V_{i,j}}}\sum_{y}z(y)\,\mathcal K^{\mathrm{small}}_{\Theta'}(g,uy,g_1)\,d\nu(u)$$ for every system of measures normalised at $t$, all test data $\Theta$, $\Theta'$ matched at $t$, every finitely supported function $z\colon G_{V_{i,j}}(\mathbb A)\to\mathbb C$, and all $g\in G_{V_{i,j+1}}(\mathbb A)$, $g_1\in G_{V_{i+1,j}}(\mathbb A)$ for which the two integrands are integrable over the two fundamental domains. Each integral is taken with the measure $\nu_V$ of its node.

The square $(i,j)$ is *non-degenerate* at $t$ if there are a system of measures normalised at $t$, test data $\Theta,\Theta'$ matched at $t$, and $z$, $g$, $g_1$ as above, with both integrands integrable, for which the integral on the right is nonzero. At a non-degenerate square there is at most one square constant.
