---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/ExistsMinAt.lean",
  "declarations": [
    "GlobalTheory.SiegJoin.BlowAt"
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

## Normalized blow-ups of a compactified Siegel moduli family with prescribed boundary orders

[Definition / hypothesis AV.D256](https://andrewodesky.com/rh/lean/GlobalTheory.Poinc.Trait/)

Fix integers $g\ge0$ and $n\ge1$, put $R_n=\mathbb Z[\zeta_n,1/n]$ with $\zeta_n=e^{2\pi i/n}$, and let $(A,P,\ell)/U$ be a Siegel moduli family of type $(g,n)$ in the sense of ([Siegel moduli families and their level pairing](https://andrewodesky.com/rh/lean/GlobalTheory.ZM.SFam/)). Let $\phi$ be an invariant function over $\mathbb Z$ in the sense of ([Polarizing fan conventions for toroidal compactifications](https://andrewodesky.com/rh/lean/GlobalTheory.LocM.InvFun/)).

**One-parameter degenerations.** A *one-parameter degeneration* of the family consists of the following.

- A complete discrete valuation ring $V$ of characteristic zero, with fraction field $K$ and a chosen uniformizer $\varpi$, and a morphism $y:\operatorname{Spec}K\to U$.
- A semiabelian scheme $G$ over $V$, in the sense of ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)).
- A positive convergent polarized degeneration datum $(C',L',Y,c',\psi)$ over $V$ and a polarized uniformization of it whose group scheme is $G$, both in the sense of ([Siegel compactification with polarized boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.SiegJoin.siegelToroidalPolCharts/)). Write $E$ for the generic abelian scheme of the uniformization and $\mathcal L$ for its polarization line bundle; $E$ is an abelian scheme over $K$ identified with $G_K$.
- A group pullback identification $\alpha:E\simeq y^*A$ such that $$\mathcal B_{\mathcal L}\simeq(\alpha\times\alpha)^*y^*P,$$ where $\mathcal B_{\mathcal L}$ is the associated double-product polarization line of ([Siegel compactification with polarized boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.SiegJoin.siegelToroidalPolCharts/)).
- A symmetric bilinear form $\beta:Y\times Y\to\mathbb Z$ on the character group $Y$ of the datum such that, for every $v\in Y$, the integer $\beta(v,v)$ is even and nonnegative and the period section $\psi(v)$ has coordinate $$u_v\,\varpi^{\beta(v,v)/2},\qquad u_v\in V^\times,$$ relative to a trivialization of the line $(L'_{c'(v)})^{-1}$ over $\operatorname{Spec}V$.

The form $\beta$ is the *period form* of the degeneration.

**Orders along degenerations.** Let $T$ be a scheme, $h:U\to T$ a morphism, $\mathcal J$ an ideal sheaf on $T$ and $d\ge0$ an integer. The ideal sheaf $\mathcal J$ *has orders $d\phi$ along degenerations*, relative to $h$, when the following holds for every one-parameter degeneration, with ring $V$, uniformizer $\varpi$, point $y$ and period form $\beta$, and every morphism $\xi:\operatorname{Spec}V\to T$ whose restriction to $\operatorname{Spec}K$ is $h\circ y$: the real number $d\,\phi(\beta)$ is a nonnegative integer and $$\xi^{-1}\mathcal J\cdot V=\bigl(\varpi^{\,d\phi(\beta)}\bigr).$$

**Normalized blow-ups.** Let $Z$ be an $R_n$-scheme and $i:U\to Z$ a morphism. Let $S$ be a scheme with morphisms $\pi:S\to Z$ and $j:U\to S$, let $B$ be an effective Cartier divisor on $S$ with ideal sheaf $\mathcal I_B$, and let $d\ge0$ be an integer. The quadruple $(S,\pi,j,B)$ is a *normalized blow-up of $(Z,i)$ with boundary orders $d\phi$* when $d\ge1$ and there is an ideal sheaf $\mathcal J$ on $Z$ with the following properties.

1. The closed set where $\mathcal J\ne\mathcal O_Z$ is disjoint from $i(U)$, and $\mathcal J$ has orders $d\phi$ along degenerations, relative to $i$.
2. The scheme $S$ is normal, and $\pi$ factors as $S\xrightarrow{\ \nu\ }S_0\xrightarrow{\ \pi_0\ }Z$, where $\pi_0$ is the blow-up of $Z$ along $\mathcal J$ and $\nu$ is finite. There is a dense open set $S_0^\circ\subseteq S_0$ whose inverse image in $S$ is dense and over which $\nu$ is an isomorphism.
3. The scheme $S$ is projective over $R_n$.
4. The image $j(U)$ is dense in $S$, and $$\pi\circ j=i,\qquad\pi^{-1}\bigl(i(U)\bigr)=j(U).$$
5. $\mathcal I_B=\mathcal J\cdot\mathcal O_S$, and $\mathcal I_B$ has orders $d\phi$ along degenerations, relative to $j$.
