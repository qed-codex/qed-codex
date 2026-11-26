---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/MassOneBase/MassOne.lean",
  "declarations": [
    "PositivityTheory.SiegelWeilFormula.BaseOne.massOne"
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

## Rank-one local Gram masses at almost every finite place

[Theorem THETA.0946](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormula.BaseOne.massOne/)

Let $E/F$ be a CM extension with conjugation $\sigma$, let $J\in E^\times$ satisfy $\sigma(J)=J$, and choose an $F$-basis $b_1,\ldots,b_d$ of $E$. For all but finitely many finite places $v$ of $F$, the following holds for every additive Haar measure $\lambda_v$ on $F_v$ with $\lambda_v(\mathcal O_{F_v})=1$.

Put $E_v=F_v\otimes_FE$ and let $\mu_v$ be the product of $d$ copies of $\lambda_v$ in the basis $b$. Set $$Q_v(x)=\sigma(x)Jx\in F_v,\qquad L_{b,v}=\sum_{i=1}^d\mathcal O_{F_v}b_i.$$ Let $(m_s)_{s\in F_v^\times}$ be any Gram-fibre measure family disintegrating $\mu_v$ along $Q_v$ relative to $\lambda_v$, with the continuity and support conditions specified below. For every $s\in\mathcal O_{F_v}^\times$, $$\left(1-\frac{\epsilon_v}{q_v}\right)^{-1}m_s(L_{b,v})=1,$$ where $q_v=|\mathcal O_F/v|$, and $\epsilon_v=1$ if $E_v\simeq F_v\times F_v$ and $\epsilon_v=-1$ if $E_v$ is a field.
