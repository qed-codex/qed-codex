---
{
  "module": "src/Formalism/SharpRestriction/GlobalSchurBounds/TaylorLogMetric.lean",
  "declarations": [
    "Formalism.MainNotions.TaylorLogMetric.RelDetPinned"
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

## Ideal characters and period lattices

[Definition / hypothesis THETA.D188](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)

Hypothesis (ideal characters and periods). Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) and ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Write $E_0\subset E$ for the imaginary quadratic field, $\varphi_0:E\hookrightarrow\mathbb C$ for the distinguished embedding, $\mathcal T$ for the selected embedding labels, $e_\tau:E\hookrightarrow\mathbb C$ for their embeddings, $A_0\subset E$ for the prescribed integral module, and $d$ for the positive discriminant parameter. Choose an integral ideal $\mathfrak c\subset\mathcal O_{E_0}$ and $\delta\in\mathbb C$ satisfying $$\mathfrak c\ne0,\qquad (N\mathfrak c,2d)=1,\qquad \delta^{12}=\Delta(\varphi_0(\mathfrak c)).$$ For an additive subgroup $\Lambda\subset\mathbb C$, the normalization here is $$G_{2k}(\Lambda)=\sum_{0\ne w\in\Lambda}w^{-2k},\quad g_2=60G_4,\quad g_3=140G_6,\quad\Delta=g_2^3-27g_3^2.$$ Sums have the total summation convention: a nonconvergent sum has value zero. Put $\Lambda=\langle\delta\varphi_0(c):c\in\mathfrak c\rangle_{\rm add}$, where brackets denote the smallest additive subgroup containing the displayed set.

An ideal label is any $\mathcal O_E$-submodule $\mathfrak a\subset E$. Call it norm one if $\mathfrak a\overline{\mathfrak a}=\mathcal O_E$, with ideal multiplication defined by the integral span of products. For full self-dual integral lattices $L,L'\subset E^N$, define $$[L:L']_{\det}=\operatorname{span}_{\mathcal O_E}\{\det A:A\in M_N(E),\ A L\subseteq L'\}.$$ Here self-dual means that the lattice is finitely generated, spans $E^N$, and equals its dual for $\sum\bar x_i y_i$.

Choose a function $\chi$ from ideal labels to $\mathbb C$. It is multiplicative on pairs of norm-one labels, and for $z\in E$ with $z\bar z=1$ require $$\chi(z\mathcal O_E)=\prod_{\tau\in\mathcal T}e_\tau(z)^{-1}.$$ Let $D/U$ be the determinant quotient and $\chi_D:D\to\mathbb C^\times$ its prescribed character. Choose an injective map $a:D/U\to\{\mathcal O_E\text{-submodules of }E\}$ whose image is exactly the norm-one labels. Require $a(xy)=a(x)a(y)$, $a([e_1(z)])=z\mathcal O_E$ for every norm-one $z$, and $$a(\operatorname{relDet}(L,L'))=[L:L']_{\det}$$ for every rank and every pair of full self-dual lattices. The chosen function is exactly $$\chi(\mathfrak a)=\begin{cases}\chi_D(x),&a([x])=\mathfrak a,\\0,&\mathfrak a\notin\operatorname{im}(a).\end{cases}$$ The value in the first case uses the descended character on $D/U$; it is independent of the representative.
