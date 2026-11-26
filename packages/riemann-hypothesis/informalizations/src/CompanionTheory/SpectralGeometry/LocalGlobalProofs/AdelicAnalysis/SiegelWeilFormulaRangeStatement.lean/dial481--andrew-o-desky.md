---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/SiegelWeilFormulaRangeStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_isEulerProd_of_invariant_of_fiber_supported"
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

## An invariant measure on a nonsingular Gram fibre is an Euler product

[Theorem THETA.0384](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_isEulerProd_of_invariant_of_fiber_supported/)

Let $E/F$ be a CM extension of number fields with involution $\sigma$, let $J$ be a nondegenerate Hermitian $M\times M$ matrix over $E$, and let $n\ge0$ satisfy $n=0$ or $n+2\le M$. Fix an invertible Hermitian $T\in\operatorname{Mat}_n(E)$ and an $F$-basis $b$ of $E$. For $u=\infty$ or a finite place $v$, put $$A_u=F_u\otimes_FE,\quad W_u=A_u^{M\times n},\quad p_u(X)=X^*JX.$$ Choose additive Haar measures $\lambda_\infty$ on $F_\infty$ and $\lambda_v$ on $F_v$, normalized so that an $\mathcal O_F$ fundamental domain has archimedean volume one and $\lambda_v(\mathcal O_{F_v})=1$. Choose continuous fibre-measure families $m_u(S)$ for $p_u$ with the coordinate normalizations below. Let $I$ be a locally finite measure on $W_{\mathbb A}=(\mathbb A_F\otimes_FE)^{M\times n}$, invariant under the natural action of $U(J)(\mathbb A_F)$ and supported on $X^*JX=T$. Put $\mu_u=m_u(T)$ and let $L_v\subset W_v$ be the lattice with all $b$-coordinates in $\mathcal O_{F_v}$. Then $a_v=\mu_v(L_v)<\infty$, $\sum_v|a_v-1|<\infty$, and there are $c\ge0$ and a finite set $S_0$ of finite places such that for every finite $S\supseteq S_0$ and every family of nonnegative measurable functions $\phi_\infty,\phi_v$, $$\int\mathbf1_{X_v\in L_v\ (v\notin S)}\phi_\infty(X_\infty)\prod_{v\in S}\phi_v(X_v)\,dI(X) =c\left(\int\phi_\infty\,d\mu_\infty\right)\prod_{v\in S}\left(\int\phi_v\,d\mu_v\right)\prod_{v\notin S}a_v.$$
