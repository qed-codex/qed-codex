---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/ExistsUnitScalingSelfdualAdelicMeasuresStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_unit_scaling_selfdual_adelic_measures"
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

## Self-dual adelic measures with product-one scaling

[Theorem THETA.1635](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_unit_scaling_selfdual_adelic_measures/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, and let $J$ be a nondegenerate $\sigma$-Hermitian matrix of size $M\ge0$. Choose an $F$-basis $b$ of $E$. Let $\lambda_\infty$ be an additive Haar measure on $F_\infty=F\otimes_\mathbb Q\mathbb R$ for which a fundamental domain of $\mathcal O_F$ has volume one, and let $\lambda_v$ be additive Haar measures on $F_v$ with $\lambda_v(\mathcal O_{F_v})=1$. Let $\psi$ be a continuous unitary nontrivial additive character of $\mathbb A_F/F$.

For every $n\ge0$, there are $c_\infty,c_v\ge0$, with $c_v=1$ for all but finitely many $v$ and $$c_\infty\prod_v c_v=1,$$ such that the self-dual measure on $(F_u\otimes_F E)^{nM}$ is exactly $c_u\lambda_u^{\otimes nM[E:F]}$ in the coordinates defined by $b$, for $u=\infty$ and every finite place $u=v$. Self-duality refers to the pairing $$\psi_u\!\left(\sum_{a=1}^n\operatorname{Tr}_{(F_u\otimes E)/F_u}J(X_a,Y_a)\right).$$
