---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ClassTermEqVolumeMulOrbitalIntegralStatement.lean",
  "declarations": [
    "GlobalTheory.T.classTerm_eq_volume_mul_orbitalIntegral"
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

## A conjugacy-class integral as centralizer volume times an orbital integral

[Theorem REP.0508](https://andrewodesky.com/rh/lean/GlobalTheory.T.classTerm_eq_volume_mul_orbitalIntegral/)

Let $H$ be a locally compact second-countable Hausdorff topological group with its Borel structure, $\Gamma\le H$ a discrete subgroup, and $\gamma\in\Gamma$. Suppose the centralizer $C=C_H(\gamma)$ is commutative. Let $dh$ and $dt$ be Haar measures on $H$ and $C$, and let $\mathcal T\subset C$ be a fundamental domain for $\Gamma\cap C$ with $dt(\mathcal T)<\infty$. Let $f:H\to\mathbb C$ be continuous with compact support and suppose its orbital integral exists absolutely and equals $c$: $$\int_{C\backslash H}f(x^{-1}\gamma x)\,d\dot x=c.$$ For every fundamental domain $\mathcal F\subset H$ for $\Gamma$, the series below is summable for every $x\in H$, its sum is integrable over $\mathcal F$, and $$\int_{\mathcal F}\sum_{\delta\in[\gamma]_\Gamma}f(x^{-1}\delta x)\,dh(x)=dt(\mathcal T)\,c.$$
