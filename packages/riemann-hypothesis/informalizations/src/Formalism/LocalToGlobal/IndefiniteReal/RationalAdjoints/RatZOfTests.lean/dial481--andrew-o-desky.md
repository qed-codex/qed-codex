---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/RationalAdjoints/RatZOfTests.lean",
  "declarations": [
    "Formalism.IndefR.Rat.RowTest"
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

## Rational families of forms, their realisations by theta maps, and the rationality test

[Definition / hypothesis THETA.D073](https://andrewodesky.com/rh/lean/Formalism.IndefR.Rat.RowTest/)

These tests express rationality of the images of class-sum forms under theta maps.

**Rational family.** Let $\mathbb L$ be a number field with involution. Use the class-sum spaces and rational families of ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)), with $K=\mathbb L$, $J=\{0,\ldots,m-1\}$ for a natural number $m$ and $\mathcal A=\mathbb N^{<\omega}$. Write $R_t$ for the right form space, $L_{j,t}$ for the lifted form space, $\mu_0$ for the base tuple and $v_0$ for the distinguished infinite place. The two transfer maps act on the polynomial and inert parts of each spectral label, respectively.

**Realisation.** Let $D$ be a datum of ([Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)), with coefficient field $\mathbb L$ and fixed embedding $\jmath:\mathbb L\hookrightarrow\mathbb C$ inducing $v_0$. A realisation with polynomial and inert Hecke labels consists of the analytic data and the rational forms for the lifts in ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)), for this rational family and with $K=\mathbb L$. Write $H_X(t),H_V(j,t),H_E,H_W(j,\sigma)$ for its complex inner-product spaces, $j_X(t),j_V(j,t)$ for its rational-form maps, $\Theta_t$ and $\theta_{j,t}$ for its theta maps, and $\phi_j$ for its complex lift scalars. Put $H_W(j)=H_W(j,\jmath)$. The compatibility conditions on these data are stated separately in ([Analytic realizations of rational Hecke families](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.BaseW/)).

A face chooses subgroups $P_0,P_1\subset G$ and characters $\psi_i:P_i\to\mathbb L^\times$. For every choice of right and lifted subspaces, it chooses the source-coordinate data $(\mathcal U,a_u,X_{u,v},p_{u,t})$, the complex common period data $(\mathcal H,P_u,R)$, and the numerical data $(F_0,J_0,E_{1,u},l_{3,m},l_{3,u},l_{6,m},l_{6,u},x,b,\lambda,\delta)$ of ([Row-side families of Hermitian spaces](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)). Use the sharp-level coordinate spaces for the pairings $p_{u,t}$.

A geometric core over $D$ is the geometric-core data of ([Adelic frames for unitary moduli](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.Core/)), with the CM field $E$, maximal real subfield $F$, distinguished imaginary quadratic subfield $E_0$, row rank $r$ and coefficient ring $O$ of $D$. Its moduli coefficient field $K_0$ and its isomorphism $\mathcal O_{K_0}\simeq O$ are part of those choices.

**Rationality tests.** Let $\sigma:\mathbb L\hookrightarrow\mathbb C$ be the embedding chosen for $v_0$, and let $\epsilon:\mathbb C\to\mathbb C$ be the identity when $\sigma=\jmath$, and complex conjugation otherwise. Thus $\sigma=\epsilon\circ\jmath$. For a complex inner-product space $H$, write $H^\epsilon$ for its underlying additive group with scalar multiplication $z\cdot_\epsilon h=\epsilon(z)h$ and inner product $\langle h,k\rangle_\epsilon=\epsilon(\langle h,k\rangle)$. Write $\widetilde j_X,\widetilde j_V,\widetilde\Theta_t,\widetilde\theta_{j,t}$ for the same underlying maps with these modified complex structures. The first two maps are $\sigma$-semilinear and the theta maps are complex-linear.

The rationality test for the rows requires finitely many complex-linear functionals $\psi_1,\ldots,\psi_N$ on $H_E^\epsilon$, with common kernel zero, such that $$\psi_i\bigl(\widetilde\Theta_t(\widetilde j_X(t)x)\bigr)\in\sigma(\mathbb L) \qquad(t\in\mathcal T,\ 1\le i\le N,\ x\in R_t).$$ The rationality test for the lifts requires, for every $0\le j<m$, finitely many complex-linear functionals $\psi_{j,1},\ldots,\psi_{j,N_j}$ on $H_W(j)^\epsilon$, with common kernel zero, such that $$\psi_{j,i}\bigl(\phi_j\,\widetilde\theta_{j,t}(\widetilde j_V(j,t)x)\bigr)\in\sigma(\mathbb L) \qquad(t\in\mathcal T,\ 1\le i\le N_j,\ x\in L_{j,t}).$$ Here multiplication by $\phi_j$ is taken in the complex vector space $H_W(j)^\epsilon$.
