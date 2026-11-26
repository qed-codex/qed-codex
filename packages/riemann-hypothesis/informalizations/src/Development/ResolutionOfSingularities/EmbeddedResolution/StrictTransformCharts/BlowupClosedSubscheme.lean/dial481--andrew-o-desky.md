---
{
  "module": "src/Development/ResolutionOfSingularities/EmbeddedResolution/StrictTransformCharts/BlowupClosedSubscheme.lean",
  "declarations": [
    "FunctorialResolution.EmbeddedResolution.strictTransformIsBlowupOfClosedSubscheme"
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

## The strict transform is the blowup of the closed subscheme

[Theorem AG.1515](https://andrewodesky.com/rh/lean/FunctorialResolution.EmbeddedResolution.strictTransformIsBlowupOfClosedSubscheme/)

Let $X$ be a locally noetherian scheme, $j:S\hookrightarrow X$ a closed immersion, and $\pi:X_1\to X$ the blowup of an ideal sheaf $\mathcal I$. Assume that no irreducible component of $S$ has image contained in $\operatorname{Supp}(\mathcal O_X/\mathcal I)$. Let $\widetilde S\subset X_1$ be the strict transform of $S$.

There is a morphism $\psi:\widetilde S\to S$ such that $j\circ\psi=\pi|_{\widetilde S}$ and $\psi$ is the blowup of the pulled-back ideal sheaf $\mathcal I\mathcal O_S$.
