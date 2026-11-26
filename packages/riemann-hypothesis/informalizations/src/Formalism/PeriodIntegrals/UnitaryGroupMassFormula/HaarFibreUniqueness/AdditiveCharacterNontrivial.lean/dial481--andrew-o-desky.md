---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/HaarFibreUniqueness/AdditiveCharacterNontrivial.lean",
  "declarations": [
    "PI.OmFibreUniq.W.Sd.additive_character_nontrivial"
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

## Nontriviality of every finite component of a standard adelic character

[Theorem ANT.0823](https://andrewodesky.com/rh/lean/PI.OmFibreUniq.W.Sd.additive_character_nontrivial/)

Let $F$ be a totally real number field and let $\psi:\mathbb A_F\to\mathbb C^\times$ be a continuous nontrivial unitary additive character trivial on $F$. Assume its infinite component is $$\psi_\infty((x_\tau)_\tau)=\exp\left(2\pi i\sum_{\tau:F\hookrightarrow\mathbb R}x_\tau\right).$$ For every finite place $v$ of $F$, the local component $\psi_v:F_v\to\mathbb C^\times$ is nontrivial: there is $y\in F_v$ with $\psi_v(y)\ne1$.
