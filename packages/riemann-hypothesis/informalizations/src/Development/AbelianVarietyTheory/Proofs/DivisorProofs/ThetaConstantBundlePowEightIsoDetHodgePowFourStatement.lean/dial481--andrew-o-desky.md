---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaConstantBundlePowEightIsoDetHodgePowFourStatement.lean",
  "declarations": [
    "GlobalTheory.T.thetaConstantBundle_pow_eight_iso_detHodge_pow_four"
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

## An eighth power of the theta-coordinate bundle is a fourth Hodge power

[Theorem AV.1640](https://andrewodesky.com/rh/lean/GlobalTheory.T.thetaConstantBundle_pow_eight_iso_detHodge_pow_four/)

Let $o$ be a Dedekind domain of finite type over $\mathbb Z$, let $\Omega$ be a characteristic-zero field, and let $o\hookrightarrow\Omega$ be injective. Fix the source's theta-system, realization, rational-model, lattice, and semiabelian-extension packages over $(o,\Omega)$, of dimension $g\ge1$. Denote their integral model by $Z$, their nonempty specified open set by $U_0\subseteq Z$, their semiabelian scheme by $G\to Z$, their finite theta index group by $\Gamma$, their theta values by $\theta_a\in\Omega$ for $a\in\Gamma$, and their generic point by $p:\operatorname{Spec}\Omega\to Z$. Assume the source's normal projective base and invertibility conditions on $U_0$, and assume the abelian-fibre locus of $G$ is open.

Let $\delta$ be a line bundle on $Z$, and let $(t_a)_{a\in\Gamma}$ be global sections with no common zero whose projective coordinates at $p$ equal $(\theta_a)_{a\in\Gamma}$. Then $$\delta^{\otimes8}\simeq\left(\det\operatorname{Lie}(G/Z)^\vee\right)^{\otimes4}.$$
