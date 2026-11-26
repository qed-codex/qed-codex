---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/BridgeTie.lean",
  "declarations": [
    "Formalism.IndefR.Bridge.CoefMapTie",
    "Formalism.IndefR.Bridge.CoefTie"
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

## Polynomial coefficient representations and integral lattices

[Definition / hypothesis ARAK.D161](https://andrewodesky.com/rh/lean/Formalism.IndefR.Bridge.CoefMapTie/)

Use the number field $K$ with involution, embedding $\jmath:K\hookrightarrow\mathbb C$, CM extension $E/F$, and CM labels $\tau$ of ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)). Choose embeddings $\ell_\tau:E\hookrightarrow K$ with $\jmath\ell_\tau=\tau$. A dominant integral weight is a nonincreasing integer list $\lambda_\tau\in\mathbb Z^n$.

Use the block polynomial space $V(\lambda)$, representation $\rho$, two transported integral lattices $\mathcal N(M),\mathcal D(M)$ and normalized Fock pairing $B_G$ defined in ([Hermitian duality of transported Weyl lattices](https://andrewodesky.com/rh/lean/GlobalTheory.T.transported_weylLattice_hermitianDuality/)). These definitions apply to arbitrary $\mathcal O_K$-submodules $M_\tau\subset K^n$ by the displayed intersection over every prime and every local basis, whether or not a local basis exists. No assertion of fullness is added here. For an $\mathcal O_E$-submodule $L\subset E^n$ put $$L_\tau=\operatorname{span}_{\mathcal O_K}\ell_\tau(L),\qquad L_\tau^\vee=\{x\in K^n:\sum_a x_ay_a\in\mathcal O_K\ (y\in L_\tau)\}.$$ The ordinary construction uses $\rho((\ell_\tau(g))_\tau)$, $B_{(\ell_\tau(G))_\tau}$ and the lattices $\mathcal N((L_\tau)_\tau),\mathcal D((L_\tau)_\tau)$. The inverse-transpose construction uses $$\rho((\ell_\tau(g)^{-T})_\tau),\quad B_{(\ell_\tau(G)^{-T})_\tau},\quad\mathcal N((L_\tau^\vee)_\tau),\quad\mathcal D((L_\tau^\vee)_\tau).$$

Fix the following polynomial basis once for each field and weight. For $\nu_a=\lambda_a-\lambda_n$ (and the empty list when $n=0$), index one-block basis vectors by nonnegative exponent matrices $m_{a,b}$ satisfying $$\sum_a m_{a,b}=\nu_b,\qquad\sum_{a\le c}m_{a,b+1}\le\sum_{a<c}m_{a,b}\quad\text{for every }b,c.$$ Choose a basis of the column-invariant polynomial space, indexed by these matrices, whose indexed vector is row-homogeneous of degree $(\sum_bm_{a,b})_a$, has leading exponent $m$ and leading coefficient one for lexicographic order after listing variables column by column, and is a product of initial-column minors with strictly increasing row lists and column multidegree $\nu$. Take products of these bases across all $\tau$ to obtain the basis $(b_\alpha)$ of $V(\lambda)$. This is a fixed choice, not an assertion that the displayed properties specify a unique basis. Put $$K^\dagger=\{a\in K:\sigma(\bar a)=\overline{\sigma(a)}\text{ for every }\sigma:K\hookrightarrow\mathbb C\}.$$

Hypothesis (coefficient comparison). For a Hermitian space $U$ with Gram matrix $G_U$, complex coefficient representation $C_U$, and rational class presentation in ([Rational class presentations and Hecke comparison](https://andrewodesky.com/rh/lean/Formalism.IndefR.Bridge.FamReal/)), choose a $\jmath$-semilinear map $c_0:V(\lambda)\to C_U$. Its basis values $c_0(b_\alpha)$ are complex linearly independent and span $C_U$. If $\gamma\in U(U)(F)$ has matrix $\gamma_E\in\mathrm{GL}_n(E)$, require $$c_0(\rho_U(\gamma_E)v)=\rho_{C_U}(\gamma)c_0(v),$$ using the ordinary or inverse-transpose action specified above.

For each tuple there is a $K$-linear isomorphism $e:V_K\simeq V(\lambda)$ from its rational class coefficient space such that every coefficient of $e(b_a)$ in $(b_\alpha)$ belongs to $K^\dagger$. Its class-presentation coefficient map is exactly $c_0e$, and $e$ preserves the rational Hermitian pairing and the appropriate normalized Fock pairing. If $y_c$ is the finite-adelic class representative, set $$L(y_c)=\operatorname{span}_{\mathcal O_E}\{v\in E^n:y_c^{-1}\widehat v\in\widehat L_{0,U}\}.$$ Require $e(N_c)$ and $e(D_c)$ to equal respectively the two appropriate transported lattices at $L(y_c)$. Here $L_{0,U}$ is the recorded reference lattice, and hats mean finite-adelic images.

On the right family use the ordinary construction, with $G=G_{X'}$ or $-G_{X'}$ chosen once for all tuples. On the input family $V_j$ use the inverse-transpose construction and the Gram matrix $-G_{V_j}$ when its recorded sign is negative, and $G_{V_j}$ otherwise. These coefficient comparisons hold at every tuple, and at every $1\le j\le m$ on the input side.
