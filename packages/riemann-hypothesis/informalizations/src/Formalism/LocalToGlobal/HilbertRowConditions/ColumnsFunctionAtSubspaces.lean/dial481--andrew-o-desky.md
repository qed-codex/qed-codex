---
{
  "module": "src/Formalism/LocalToGlobal/HilbertRowConditions/ColumnsFunctionAtSubspaces.lean",
  "declarations": [
    "Formalism.L2.Rows.RowSideFamily"
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

## Row-side families of Hermitian spaces

[Definition / hypothesis ARAK.D208](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)

Use ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)), with coefficient field $K$, finite group $G$, twist set $T$, place sets $\mathcal P,\mathcal I$ and $m$ stages. Choose subgroups $P_0,P_1\subset G$ and characters $\psi_0:P_0\to K^\times$, $\psi_1:P_1\to K^\times$. Write $b=0,1$ for the base and sharp levels. Choose subspaces $Z_t^R\subset\mathcal F_t^R$ and $Z_{i,t}^L\subset\mathcal F_{i,t}^L$.

The following coordinate construction fixes all spaces used in the hypothesis. In the group algebra use $e_{\mathcal X}$ from ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)), and put $$e_{P,\psi}=\frac1{|P|}\sum_{h\in P}\psi(h^{-1})[h].$$ Use the image of $e_{\mathcal X}e_{P,\psi}$ on each class-sum forms space. A basis for any image or selected subspace is chosen with coordinates in $K_{\rm c}$ whenever possible, and arbitrarily otherwise. If $E$ is its inclusion matrix in class-sum coordinates, the ambient Gram matrix and integral module are $H_V=|P|^{-1}E^*HE$ and $M=E^{-1}(N)$. If $Z$ is the inverse image of the selected subspace and $C$ its chosen basis matrix, set $$P_Z=(C^*H_VC)^{-1}C^*H_V,\qquad H_Z=C^*H_VC.$$ At an infinite place $v$, the quotient frame is the inverse of the matrix square root of $$\bigl(v(P_Z)v(H_V)^{-1}v(P_Z)^*\bigr)^{-1}.$$ Here the matrix square root is the nonnegative continuous-functional-calculus square root. The selected integral quotient module is $P_ZM$. For a lifted space its integral module is instead the image of the full $\psi^{-1}$-subgroup-character numerator module under $P_Z$ composed with the projection from that full character space to the selected finite-group image. Right spaces use $\psi$ and lifted spaces use $\psi^{-1}$.

The quotient spectral subspaces are the inverse images under $C$ of the residual spectral sums from ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)). A full label includes both its residual Hecke polynomial and its inert eigenvalue function; lifted labels use the prescribed polynomial and inert transports. Let $\Pi$ be the finite set of full labels occurring at the distinguished right twist, with the same empty-set convention when the underlying occurrence set is infinite. Thus the construction gives, for every $b,t$, a right coordinate dimension $n_{b,t}$, matrix $H_{b,t}$, integral module $M_{b,t}$, quotient dimension $q_{b,t}$, projection $P_{b,t}$, frames $X_{Q,b,t,v}$ and spectral subspaces $Q_{b,t,\pi}$; and, for every $b,i,t$, lifted dimensions $z_{b,i,t}$, matrices $H_{T,b,i,t}$, frames $X_{T,b,i,t,v}$, modules $T_{b,i,t}$ and subspaces $Z_{b,i,t,\pi}$.

Hypothesis (row-side coordinates). For each $b$ choose a map $\mu_b$ from finite $K$-places to $T$, a finite set $\mathrm{Tw}_b$ of such places, a common dimension $d_b$, complex frame matrices $X_{E,b,v}$ at every infinite place, spectral subspaces $E_{b,\pi}\subset K^{d_b}$, and matrices $$\iota_{b,t}:K^{q_{b,t}}\to K^{d_b}.$$ For every $b,i$ choose a common lifted dimension $d_{W,b,i}$, complex frame matrices $X_{W,b,i,v}$, subspaces $W_{b,i,\pi}\subset K^{d_{W,b,i}}$, an $\mathcal O_K$-submodule $M_{W,b,i}$, and matrices $$\Theta_{b,i,t}:K^{z_{b,i,t}}\to K^{d_{W,b,i}}.$$ Choose real scalars $\kappa_{b,v}$, $\lambda_{b,i,t,\pi,v}$ and $\operatorname{err}_{b,w,i}$ on all their displayed index ranges. None of these choices alone asserts injectivity, isometry, positivity or a lattice property.

Choose a source set $\mathcal U$, dimensions $a_u$, complex square source frames $X_{u,v}$ at every infinite $K$-place, and pairings $$p_{u,t}:K^{a_u}\times K^{n_{1,t}}\to K.$$ Choose a complex inner-product space $\mathcal H$, complex-linear maps $P_u:\mathbb C^{a_u}\to\mathcal H$, and a subspace $R\subset\mathcal H$. Choose pairings $B_u:K^{a_u}\times K^{d_1}\to K$, scalars $\zeta_{u,t}\in K$, a conjugate-linear map $s:\mathbb C^{d_1}\to\mathcal H$, and $\mathcal O_K$-submodules $N_u\subset K^{a_u}$.

Require the identifications and the division, lattice, ambient and central-action comparisons in ([Divisor rows and additive-character comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DivisionCompatibilityDataThreeSided/)). In addition choose, for every twist whose member label is the distinguished label or is selected at some coefficient place, a $K$-linear isomorphism from its full base subgroup-character coordinates to the prescribed rational Hermitian ambient space. At every stage choose a $K$-linear isomorphism from the common base lifted coordinates to the prescribed rational Hermitian theta-output space. Their complex embeddings, integral modules and metrics satisfy the ambient and lifted comparisons in ([Divisor rows and additive-character comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DivisionCompatibilityDataThreeSided/)).

For constructions varying the chosen subspaces, choose a source-coordinate datum and a complex common period datum of exactly the preceding kinds for every choice $(Z^R,Z^L)$. Choose also real functions $F_0(w,i)$, $J_0(t,w,i)$, $l_{3,m}(i)$, $l_{6,m}(i)$ and real constants $E_{1,u},l_{3,u},l_{6,u},x,b,\lambda,\delta$ for every such choice. For constants $C,C_H$ they give the numerical data $$E_1(i)=CE_{1,u},\quad l_3(i)=l_{3,m}(i)+Cl_{3,u},\quad l_6(i)=l_{6,m}(i)-Cl_{6,u},\quad h=x^{C_H}b,$$ with $F_0,J_0,\lambda,\delta$ unchanged.
