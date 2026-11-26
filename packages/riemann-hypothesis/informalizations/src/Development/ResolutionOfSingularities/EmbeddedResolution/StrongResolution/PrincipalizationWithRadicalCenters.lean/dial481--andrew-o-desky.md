---
{
  "module": "src/Development/ResolutionOfSingularities/EmbeddedResolution/StrongResolution/PrincipalizationWithRadicalCenters.lean",
  "declarations": [
    "FunctorialResolution.EmbeddedResolution.isFunctorialPrincipalization_principalizationWithRadicalCenters"
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

## Principalization compatible with embeddings and pullbacks

[Theorem AG.1714](https://andrewodesky.com/rh/lean/FunctorialResolution.EmbeddedResolution.isFunctorialPrincipalization_principalizationWithRadicalCenters/)

The source's specified principalization algorithm has the following properties. Its input is a smooth quasi-compact scheme of finite type $X/k$ over a characteristic-zero field, an ideal $\mathcal I$ nonzero on every irreducible component, and a finite ordered list $E$ of ideal sheaves in strict normal-crossing position. It returns a finite blow-up sequence with smooth centers having normal crossings with the successive boundaries, and successive ideals $\mathcal I_i$ satisfying $$\mathcal I_0=\mathcal I,\qquad \mathcal E_i\mathcal I_{i+1}=\mathcal I_i\mathcal O_{X_{i+1}},\qquad\mathcal I_r=\mathcal O_{X_r},$$ where $\mathcal E_i$ is the exceptional ideal. Each center lies in the vanishing locus of $\mathcal I_i$; the boundary is updated by taking strict transforms and appending the exceptional ideal.

For every field homomorphism $k\to K$ of characteristic-zero fields, provided the pulled-back data again satisfy the stated input conditions, the output over $K$ is the termwise cartesian pullback of the output over $k$, with the same length and pulled-back centers. For every smooth $k$-morphism $X'\to X$ between such inputs, the sequences agree by cartesian pullback after omitting precisely the stages whose pulled-back centers are empty; if the morphism is also surjective, they agree term by term with equal lengths.

Finally, let $j:S\hookrightarrow X$ be a closed immersion between smooth quasi-compact finite-type $k$-schemes, of constant positive codimension in étale coordinates. Give both inputs empty boundaries. For an ideal $\mathcal J$ on $S$, assume that both $\mathcal J$ and the ideal on $X$ defining the image of $V(\mathcal J)$ are nonzero on every irreducible component of their respective schemes. The two output sequences have equal lengths and compatible closed immersions at every stage; the ambient centers are the images of the centers on $S$, and the successive embedded schemes are their strict transforms.
