---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/RealSeparation/FramesOKg2.lean",
  "declarations": [
    "Formalism.IndefR.Mi.FramesOKg2"
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
