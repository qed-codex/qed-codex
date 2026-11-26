---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/NonzeroLocus.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Out.KTriv",
    "ReciprocityTheory.ChartRestriction.G.Out.RelAmple",
    "ReciprocityTheory.ChartRestriction.G.Out.Rigidified",
    "ReciprocityTheory.ChartRestriction.G.Out.Sym"
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

## Relative ampleness by affine section charts

[Definition / hypothesis AV.D078](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.RelAmple/)

Let $p:X\to S$ be a morphism of schemes and $L$ a line bundle on $X$. The following affine-chart condition defines relative ampleness.

For every affine open $U\subseteq S$, put $X_U=p^{-1}(U)$. There are integers $N\ge1$ and $M\ge0$ and sections $$s_0,\ldots,s_M\in H^0(X_U,L^{\otimes N}|_{X_U})$$ such that their nonvanishing loci $X_{U,s_i}$ cover $X_U$, each $X_{U,s_i}$ is affine, and, for every $i$, the ring homomorphism $$\Gamma(U,\mathcal O_S)[T_0,\ldots,T_M]\longrightarrow \Gamma(X_{U,s_i},\mathcal O_X),\qquad T_j\longmapsto s_j/s_i$$ is surjective. On coefficients it is pullback along $p$. The ratios are regular functions on $X_{U,s_i}$: they are characterized by $s_j=(s_j/s_i)s_i$ there. Both the exponent $N$ and the chosen sections may depend on $U$.

## Rigidification, symmetry and translation kernels

[Definition / hypothesis AV.D079](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.Rigidified/)

Let $A\to S$ be an abelian scheme as defined in ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)), with identity section $e:S\to A$, and let $M$ be a line bundle on $A$.

The line bundle *admits a rigidification* if $e^*M$ has a nowhere-zero section, equivalently a trivialization $e^*M\simeq\mathcal O_S$.

It is *locally symmetric over $S$* if every point of $S$ has an open neighborhood $U$ such that $$[-1]^*(M|_{A_U})\simeq M|_{A_U},$$ where $A_U=A\times_S U$ and $[-1]$ is group inversion on $A_U$.

It has *trivial translation kernel* if the following implication holds for every affine scheme $T=\operatorname{Spec}R$ over $S$ and every $x\in A(T)$. Write $M_T$ for the pullback of $M$ to $A_T$, and $t_x:A_T\to A_T$ for translation by $x$. If every point of $T$ has an open neighborhood $V$ on which $$\left(t_x^*M_T\otimes M_T^{-1}\right)|_{A_V}$$ is trivial, then $x=e_T$, the identity point in $A(T)$.
