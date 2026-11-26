---
{
  "module": "src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LipschitzWeightAndMinimum.lean",
  "declarations": [
    "Formalism.LFunctionChainParameters.ThickSetMeanBounds.derivative_integral_all",
    "Formalism.LFunctionChainParameters.ThickSetMeanBounds.lipschitz_weight_all",
    "Formalism.LFunctionChainParameters.ThickSetMeanBounds.proposition_size_bound"
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

## Variation of smoothed prime sums

[Theorem ANT.0156](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.ThickSetMeanBounds.lipschitz_weight_all/)

Let $H$ be any finite abelian group and $G=(\mathbb Z/2\mathbb Z)^2\times H$. Choose arbitrary natural numbers $q,d$, subgroups $I_p\le G$ and elements $F_p\in G$ for each natural number $p$, and a complex function $\kappa$ on $\widehat G$. Define $a_\gamma(n)$ and $g_\gamma(y)$ by the formulas in ([Prime-power Fourier identity](https://andrewodesky.com/rh/lean/Deduction.ch_balance/)). No ramification or primality conditions on these data are needed here. For the trivial character use the real function $g_1$ in that formula, independent of $\kappa(1)$.

For every $\gamma\in\widehat G$ and $A,v,v'>0$, $$|v g_\gamma(A/v)-v'g_\gamma(A/v')|\le\frac{3A}{\min(v,v')}|v-v'|.$$ There is an absolute constant $C_d\ge0$, chosen before $H$ and all the preceding data, such that, for $y,z\ge1$ and every nontrivial $\gamma$, $$|g_\gamma(y)-g_\gamma(z)|\le |y-z|\{\log\max(y,z)+C_d+|\kappa(\gamma)|\},$$ while $$|g_1(y)-g_1(z)|\le C_d|y-z|.$$

## Normalizing the numerical error bracket

[Theorem ALG.0157](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.ThickSetMeanBounds.proposition_size_bound/)

Let $n,t,s,m$ be nonnegative integers and let $C,\varepsilon,x,b,k,a_0,E,Z$ be real numbers. Assume all the following conditions: $$x\ge3,\quad \varepsilon>0,\quad C\ge0,\quad n>0,\quad b>0,\quad 0\le a_0\le2xb,$$ $$\tfrac12nx^{-\varepsilon/8}\le t,\qquad x^{-\varepsilon}\le s/n,\qquad s\le n,$$ $$x^{1/2-\varepsilon}\le m\le x^{1/2+\varepsilon/2},\qquad xm\le k\le n^2x^{1/2-\varepsilon},\qquad26\le x^{3\varepsilon/8}.$$ Define $$B=t a_0(1+m^2/k)+m\left(2nmbx^\varepsilon+\frac{skb x^\varepsilon}{n(nx^{-\varepsilon})}\right).$$ Suppose $$E\le x^{C\varepsilon}B,\qquad tmb\frac{s/n}{2}\left(Z-4x^{1/2+\varepsilon}\right)\le E+\frac{2tmb}{x}.$$ Then $$Z\le x^{1/2+(C+3)\varepsilon}.$$
