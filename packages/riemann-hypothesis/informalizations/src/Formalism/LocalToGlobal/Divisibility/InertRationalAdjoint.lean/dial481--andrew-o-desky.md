---
{
  "module": "src/Formalism/LocalToGlobal/Divisibility/InertRationalAdjoint.lean",
  "declarations": [
    "Formalism.L2.DIV.DefFam3",
    "Formalism.L2.DIV.DefFam3.Ok3"
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

## Class sums and finite Hecke families

[Definition / hypothesis ARAK.D202](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)

Hypothesis (class sums). Let $K$ be a number field with involution, and let $$K_{\rm c}=\{a\in K:\sigma(\bar a)=\overline{\sigma(a)}\text{ for every }\sigma:K\hookrightarrow\mathbb C\}.$$ A class-sum datum consists of a finite set $C$, a finite-dimensional $K$-vector space $V$ with its restricted $\mathcal O_K$-module structure and a specified finite basis, a sesquilinear pairing $b:V\times V\to K$ conjugate-linear in its first variable, and, for each $c\in C$, a finite group $\Gamma_c$, a representation $\rho_c:\Gamma_c\to\operatorname{End}_K(V)$ and two $\mathcal O_K$-submodules $N_c,D_c\subset V$. Its space of forms and weighted pairing are $$\mathcal F=\{f:C\to V:\rho_c(\gamma)f(c)=f(c)\text{ for all }c,\gamma\},\qquad (f,g)=\sum_{c\in C}\frac{b(f(c),g(c))}{|\Gamma_c|}.$$ Fix a basis of $\mathcal F$ whose values have coordinates in $K_{\rm c}$ whenever such a basis exists; otherwise fix an arbitrary basis. Denote its coordinate evaluation map by $I:K^{\dim\mathcal F}\to(C\to V)$ and the Gram matrix of the displayed pairing by $H$. The two coordinate integral modules are $\{x:I(x)(c)\in N_c\ \forall c\}$ and $\{x:I(x)(c)\in D_c\ \forall c\}$. No positivity, symmetry or lattice condition is included in the definition of these data.

**Rational families.** Fix a finite group $G$, sets $\mathcal P,\mathcal I,\mathcal A,\mathcal T$, and a finite set $J$. A block datum $B$ over $\mathcal P$ consists of a class-sum datum with form space $\mathcal F$, a $K$-linear representation $\rho$ of $G$ on $\mathcal F$, a set $\mathcal P_B$ with a map $p_B:\mathcal P_B\to\mathcal P$, natural numbers $n_B,t_B$, a function $q_B:\mathcal P_B\to\mathbb N$, endomorphisms $T^B_{P,d}$ of $\mathcal F$ for $P\in\mathcal P_B,d\in\mathbb N$, and a finite list of functions $\nu_{B,s}:\mathcal P_B\to K$. Additional inert data consist of a set $\mathcal I_B$, a map $i_B:\mathcal I_B\to\mathcal I$ and endomorphisms $U^B_{P,a}$ of $\mathcal F$ for $P\in\mathcal I_B,a\in\mathcal A$.

A rational family consists of an infinite place $v_0$ of $K$, a base tuple $t_0\in\mathcal T$, a finite set $\mathcal X\subset K^G$, a right block datum $B^R_t$ for every $t\in\mathcal T$, a lifted block datum $B^L_{j,t}$ for every $j\in J,t\in\mathcal T$, inert data on each of these block data, and maps $$\tau_j:(\mathcal P\to K[X])\longrightarrow(\mathcal P\to K[X]),\qquad \tau_j^I:(\mathcal I\times\mathcal A\to K)\longrightarrow(\mathcal I\times\mathcal A\to K).$$ Write $R_t$ and $L_{j,t}$ for the right and lifted form spaces. A full spectral label is a pair $(S,u)$ of a function $S:\mathcal P\to K[X]$ and a function $u:\mathcal I\times\mathcal A\to K$; its transfer at $j$ is $(\tau_j(S),\tau_j^I(u))$.

**Finite Hecke families.** A particular class of rational families has $J=\{0,\ldots,m-1\}$ for a natural number $m$, and $\mathcal A=\mathbb N^{<\omega}$ is the set of finite sequences of natural numbers. Choose natural numbers $r_A,t_A$, natural numbers $q_P$ for $P\in\mathcal P$, units $\mu_{j,t,P},\eta_P\in K^\times$, and subsets $\mathcal P_t\subset\mathcal P$, $\mathcal I_t\subset\mathcal I$. For the right and lifted block data at $t$, take $\mathcal P_B=\mathcal P_t$, $\mathcal I_B=\mathcal I_t$, both place maps to be inclusions, and $q_B(P)=q_P$. Use the degrees, block lists and polynomial transfer specified below; choose the class-sum data, representations, endomorphisms and inert transfer maps arbitrarily.

## Integral frames and Hecke operator laws

[Definition / hypothesis ARAK.D221](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DefFam3.Ok3/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Row-side families of Hermitian spaces](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)) and ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)). Write $K$ for the coefficient field, $E/F$ for the CM extension, $t_0$ for the distinguished tuple, and $\jmath:K\hookrightarrow\mathbb C$ for its distinguished embedding. The involution of $K$ satisfies $\jmath(\bar a)=\overline{\jmath(a)}$. The tuple set is finite. Every selected finite-group character is the character of an irreducible representation over an algebraic closure of $K$.

Hypothesis (Hecke operator laws). Impose the following conditions on every base and lifted row datum. Its coefficient pairing is Hermitian and nondegenerate, and each class stabilizer acts by isometries. Every specified numerator module $N_c$ is a full integral lattice, and the denominator module $D_c$ satisfies $$D_c\subseteq N_c,\qquad N_c^\vee\subseteq D_c,\qquad D_c\subseteq N_c^\vee.$$ Each $D_c$ is stable under the class stabilizer. Here $N_c^\vee=\{y:\langle x,y\rangle\in\mathcal O_K\text{ for all }x\in N_c\}$.

The Gram matrix of the stabilizer-weighted class-sum pairing has coefficients in the subfield $K^{\dagger}$ defined in Hypothesis (primitive row comparisons) of ([Analytic theta maps and primitive row comparisons](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.ExAt/)), and is positive definite under every infinite embedding of $K$. The finite-group action preserves that pairing and both integral class-function modules, and its matrices in the specified class-function basis have coefficients in $K^{\dagger}$. The Hecke operators commute pairwise, and each is split over $K$, meaning that its generalized eigenspaces over $K$ span the full form space. Every Hecke operator commutes with the group action. The block length is at least one, the block list is nonempty and every block parameter at every prime is nonzero. Every recorded residue cardinality is positive, and the prime-label map is injective.

The combined Hecke and inert operators commute pairwise. Each inert operator is split over $K$ in the same generalized-eigenspace sense, commutes with the group action, and has an injective prime-label map.

Hypothesis (integral frames). Let $Y_j,X_j,W_j$, their fixed rational bases and inclusions $X_j\to Y_j$, and the adelic bases $\beta_{Y,j},\beta_{W,j}$ be those of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)) and ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)). Let $P_g$ be the finite set of selected generator places. All localized equalities below mean equality after multiplication by every finite-adelic idempotent supported at the indicated place.

There exist vectors $e_{j,i},f_{j,i},z_j\in Y_j(E)$ and nonzero scalars $\kappa_{j,i},s_j\in E$. Put $a_j=m-1-j$ and define an ordered list of $a_j$ vectors by $$v_{j,i}=\begin{cases}e_{j,i}&i<\lfloor a_j/2\rfloor,\\ z_j&a_j\text{ odd and }i=\lfloor a_j/2\rfloor,\\ f_{j,a_j-1-i}&\text{otherwise}.\end{cases}$$ For $j<m$ the $e$'s and $f$'s with indices below $\lfloor a_j/2\rfloor$ form hyperbolic pairs: $h(e_{j,i},f_{j,l})=\delta_{il}$ and $h(e_{j,i},e_{j,l})=h(f_{j,i},f_{j,l})=0$. When $a_j$ is odd, $h(z_j,z_j)=-T$ and $z_j$ is orthogonal to all these pairs. The image of $X_j$ is orthogonal to every $v_{j,i}$. Define $$c_{j,0}=s_j,\qquad c_{j,i+1}=\kappa_{j,i}c_{j,i}.$$ For every $P\in P_g$, $j<m$ and $i<a_j$, the multiplicative $P$-valuation of $c_{j,i}$ is one. At $P$, column $k+i$ of $\beta_{Y,j}$ is $$(NP)^{i+1}c_{j,i}v_{j,i}.$$ Every column outside this consecutive list belongs locally to the image of $X_j$.

There is also a specified base-stage list $v_i^0$: it consists of the fixed hyperbolic vectors $e_i$ for $i<r_S$, the fixed vector $z_-$ for $i=r_S$, and $-T f_{2r_S-i}$ thereafter, with zero in the cases not covered by these indices. At every $P\in P_g$, column $N_0+i$ of $\beta_{Y,0}$ is $(NP)^{i+1}v_i^0$ for $i<m-1$, and each earlier column belongs locally to $X_0$.

For each selected $j$, there are an index bijection preserving the numerical index and an invertible finite-adelic matrix $\iota_j$ with $$\iota_j^*G_{Y,0}\iota_j=G_{W,j}.$$ After this index identification, the matrix $\beta_{Y,0}^{-1}\iota_j\beta_{W,j}$ is integral at every $P\in P_g$ and reduces to the identity there.

Finally, for each $j<m$ there is an adelic basis $\beta_{X,j}$ for the fixed integral lattice of $X_j$: a finite-adelic vector lies in its completed lattice exactly when its $\beta_{X,j}$-coordinates are integral. If $C_j$ is the matrix of $X_j\to Y_j$ in the fixed rational bases, require at every $P\in P_g$ $$(\beta_{Y,j})_{\bullet,c}=C_j(\beta_{X,j})_{\bullet,l}$$ whenever either $c<k$ and $l=c$, or $k+(m-1-j)\le c$ and $l=c-(m-1-j)$.
