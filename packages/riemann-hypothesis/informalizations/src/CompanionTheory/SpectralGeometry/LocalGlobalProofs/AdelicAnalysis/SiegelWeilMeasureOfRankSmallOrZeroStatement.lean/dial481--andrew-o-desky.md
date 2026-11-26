---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/SiegelWeilMeasureOfRankSmallOrZeroStatement.lean",
  "declarations": [
    "GlobalTheory.T.siegel_weil_measure_of_rank_small_or_zero"
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

## Euler factorization of the fixed-Gram theta measure

[Theorem THETA.1359](https://andrewodesky.com/rh/lean/GlobalTheory.T.siegel_weil_measure_of_rank_small_or_zero/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, let $J$ be a nondegenerate Hermitian form on $E^M$, and let $n\ge0$ satisfy $n=0$ or $n+2\le M$. Let $T\in\operatorname{Herm}_n(E)$ have nonzero determinant. Write $H=U(J)$ and $q(X)=(J(X_a,X_b))_{a,b}$ for the Gram map on $n$-tuples.

Choose an $F$-basis $b$ of $E$. Choose additive Haar measures on $F_\infty$ and all $F_v$, normalized so that a fundamental domain for $\mathcal O_F$ at infinity, and $\mathcal O_{F_v}$ at a finite place, have volume one. Use the product coordinate measures on tuple spaces and on Hermitian matrices: diagonal coordinates are half their $E/F$ traces and upper off-diagonal coordinates use $b$. At infinity and every finite place, choose any families of Gram-fibre measures disintegrating these coordinate measures on the invertible-Gram locus; write $m_\infty(T),m_v(T)$ for the measures at $T$.

For any Haar measure $\mu$ on $H(\mathbb A_F)$ and fundamental domain $\mathcal F$ for $H(F)$, put $$\Theta_T=(\mu(\mathcal F))^{-1}\sum_{\substack{X\in(E^M)^n\\q(X)=T}}(h\mapsto h^{-1}X)_*(\mu|_{\mathcal F}).$$ Let $\Lambda_v$ be the integral tuple lattice in $b$-coordinates and $a_v=m_v(T)(\Lambda_v)$. Then $a_v<\infty$ for every $v$ and $\sum_v|a_v-1|<\infty$. There is a finite set $S_0$ of finite places such that, for every finite $S\supseteq S_0$ and all measurable nonnegative extended-real test functions $\phi_\infty,\phi_v$, $$\int\phi_\infty(X_\infty)\prod_{v\in S}\phi_v(X_v)\prod_{v\notin S}1_{\Lambda_v}(X_v)\,d\Theta_T =\left(\int\phi_\infty\,dm_\infty(T)\right)\prod_{v\in S}\int\phi_v\,dm_v(T)\ \prod_{v\notin S}a_v.$$
