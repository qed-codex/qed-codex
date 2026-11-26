---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/IsMumfordFamOfSubsingleton.lean",
  "declarations": [
    "GlobalTheory.PolDeg.IsGenFibre",
    "GlobalTheory.PolDeg.IsMumfordFam",
    "GlobalTheory.PolDeg.IsUnifAlong",
    "GlobalTheory.PolDeg.PreChart"
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

## Polarized boundary charts carrying a semiabelian scheme

[Definition / hypothesis AV.D259](https://andrewodesky.com/rh/lean/GlobalTheory.PolDeg.PreChart/)

Fix integers $g\ge0$ and $n\ge1$, put $R_n=\mathbb Z[\zeta_n,1/n]$ with $\zeta_n=e^{2\pi i/n}$, and let $(A,P,\ell)/U$ be a Siegel moduli family of type $(g,n)$ in the sense of ([Siegel moduli families and their level pairing](https://andrewodesky.com/rh/lean/GlobalTheory.ZM.SFam/)). Let $s:S\to\operatorname{Spec}R_n$ be a scheme over $R_n$ and $j:U\to S$ an open immersion. Let $\phi$ be an invariant function over $\mathbb Z$ in the sense of ([Polarizing fan conventions for toroidal compactifications](https://andrewodesky.com/rh/lean/GlobalTheory.LocM.InvFun/)), let $B$ be an effective Cartier divisor on $S$, let $d\ge0$ be an integer, and let $x\in S$.

A *polarized chart with a semiabelian scheme* at $x$ for $(\phi,B,d)$ consists of the data (1)–(3), subject to the condition (4).

1. **Chart data.** A complete regular local domain $R$ of characteristic zero with a map $b:R_n\to R$, a map $\xi:\operatorname{Spec}R\to S$ over $b$ taking the closed point to $x$, and elements $t_1,\ldots,t_m\in\mathfrak m_R$; a smooth abelian scheme $C/R$ with its rigidified cubical line bundle $M$, a finite free abelian group $X_0$ of rank at most $g$, an additive map $c:X_0\to C(R)$ and generators $\tau(v,v')$ over $K=\operatorname{Frac}R$; forms $\delta_1,\ldots,\delta_m$ on $X_0$ forming a cone for $\phi$; and integers $a_1,\ldots,a_m\ge0$. These are the data of a polarized chart at $x$ for $(\phi,B,d)$ in ([Siegel compactification with polarized boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.SiegJoin.siegelToroidalPolCharts/)), where the group $X_0$ is called $X$. They satisfy every condition imposed on a polarized chart there, with one exception: the condition on polarized uniformizations, which is the only one that refers to a semiabelian scheme over $S$, is replaced by (4).
2. **A semiabelian scheme over the chart.** A semiabelian scheme $G_1\to\operatorname{Spec}R$, in the sense of ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)), such that for every prime $\mathfrak p\subset R$ the geometric fibres of $G_1$ over $\mathfrak p$ are proper exactly when $\prod_it_i\notin\mathfrak p$.
3. **Its generic fibre.** A morphism $y:\operatorname{Spec}K\to U$ such that $j\circ y$ is the restriction of $\xi$ to $\operatorname{Spec}K$, and a group pullback identification $\alpha_1:(G_1)_K\simeq y^*A$.
4. **Uniformizations.** Let $\rho:R\to R'$ be a finite injective homomorphism to a complete normal Noetherian local domain of characteristic zero, with $K'=\operatorname{Frac}R'$, and let $y':\operatorname{Spec}K'\to U$ be the composite of $y$ with the map $\operatorname{Spec}K'\to\operatorname{Spec}K$ induced by $\rho$. For every positive convergent polarized degeneration datum over $R'$ and every comparison of it with $(C,M,X_0,c,\tau)$, there is a polarized uniformization of the datum over $R'$ with the following three properties. Write $H$ for its group scheme, $E$ for its generic abelian scheme over $K'$ and $\mathcal L$ for the polarization line bundle of $E$. - $H$ is the pullback of $G_1$ along $\operatorname{Spec}R'\to\operatorname{Spec}R$, by a group pullback identification $\pi:H\simeq G_1\times_RR'$. - There is a group pullback identification $\alpha:E\simeq y'^*A$ with $$\mathcal B_{\mathcal L}\simeq(\alpha\times\alpha)^*y'^*P.$$ - Under the identification $H_{K'}\simeq E$ of the uniformization, $\alpha$ agrees with the base change to $K'$ of $\alpha_1$ composed with $\pi$.
