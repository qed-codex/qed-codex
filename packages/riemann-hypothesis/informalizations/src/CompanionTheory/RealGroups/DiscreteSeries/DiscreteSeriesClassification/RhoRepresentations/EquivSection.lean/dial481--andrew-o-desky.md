---
{
  "module": "src/CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/RhoRepresentations/EquivSection.lean",
  "declarations": [
    "CompanionTheory.RgDs.K.equivariant_section_holds"
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

## Equivariant sections for compact groups

[Theorem REP.1573](https://andrewodesky.com/rh/lean/CompanionTheory.RgDs.K.equivariant_section_holds/)

Let $G$ be a compact Hausdorff topological group, equipped with its Borel measurable structure. Let $A,S$ be finite-dimensional normed complex vector spaces. Suppose $\rho:G\to\mathcal L_{\mathbb C}(A)$ and $\sigma:G\to\mathcal L_{\mathbb C}(S)$ preserve the identity and multiplication, $\rho$ is continuous in operator norm, and every orbit map $g\mapsto\sigma(g)y$ is continuous. Every surjective complex-linear map $f:A\to S$ satisfying $f\rho(g)=\sigma(g)f$ has a complex-linear section $s:S\to A$ with $$fs=1_S,\qquad s\sigma(g)=\rho(g)s\quad(g\in G).$$
