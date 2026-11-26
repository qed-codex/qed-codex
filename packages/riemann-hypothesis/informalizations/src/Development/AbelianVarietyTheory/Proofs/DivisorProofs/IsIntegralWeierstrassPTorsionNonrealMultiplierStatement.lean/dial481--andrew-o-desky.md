---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsIntegralWeierstrassPTorsionNonrealMultiplierStatement.lean",
  "declarations": [
    "GlobalTheory.T.isIntegral_weierstrassP_torsion_nonreal_multiplier"
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

## Integrality of normalized Weierstrass values at CM torsion points

[Theorem ANT.0189](https://andrewodesky.com/rh/lean/GlobalTheory.T.isIntegral_weierstrassP_torsion_nonreal_multiplier/)

Let $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2\subset\mathbb C$ be a period lattice. Suppose $\beta\in\mathbb C$ satisfies $\beta\Lambda\subseteq\Lambda$ and $\operatorname{Im}\beta\ne0$. Choose $\Omega\in\mathbb C$ with $$\Omega^{12}=g_2(\Lambda)^3-27g_3(\Lambda)^2,$$ and let $M\ge1$ be an integer. For every $P\in\mathbb C$ with $MP\in\Lambda$, both $$\frac{12M^2\wp_\Lambda(P)}{\Omega^2},\qquad \frac{M^3\wp'_\Lambda(P)}{\Omega^3}$$ are algebraic integers. If also $MQ\in\Lambda$ and $P,Q\notin\Lambda$, then $$\frac{M^2(\wp_\Lambda(P)-\wp_\Lambda(Q))}{\Omega^2}$$ is an algebraic integer.
