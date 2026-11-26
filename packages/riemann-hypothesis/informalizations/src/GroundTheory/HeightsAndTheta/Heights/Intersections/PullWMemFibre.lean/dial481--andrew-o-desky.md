---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/Intersections/PullWMemFibre.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.Inter.IntersectionWithSection.proof"
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

## A projection formula for logarithmic intersection integrals

[Theorem ARAK.1347](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Inter.IntersectionWithSection.proof/)

Assume the source's four global inputs: existence of analytic logarithmic resolutions, their integration formula, counting of generic fibres by field-intersection multiplicities, and pullback of sheet densities. Let $K,K'$ be finite sets with finite coordinate sets $(I_k),(I'_{k'})$. Let $\kappa:K\to K'$ and $v:\coprod_k I_k\to\coprod_{k'}I'_{k'}$ be a block map, so $v(I_k)\subseteq I'_{\kappa(k)}$. Let $P'\subseteq\mathbb Z[x'_{k',i}]$ and let $P$ be the ideal of its image under the associated coordinate projection. Assume both define relevant horizontal integral arithmetic multiprojective varieties with nonempty block sets of arithmetic dimension $n+1$.

Choose the source's generic-fibre presentation of this projection and a field-intersection multiplicity family on it, and let $d$ be its multiplicity at the generic-fibre ideal with no additional equations. Let $L_1,\ldots,L_n,A$ be smooth Hermitian line data on the image, and let $L'_1,\ldots,L'_n,A'$ be their compatible pullbacks. For any polynomial $s$ representing a section of $A$ along $P$, $$I_{P'}\bigl(\log h'_1,\ldots,\log h'_n;\log\|v^*s\|_{A'}\bigr) =d\,I_P\bigl(\log h_1,\ldots,\log h_n;\log\|s\|_A\bigr).$$ Here $I$ is the projection-independent form of the mixed-curvature sheet integral defined in ([A logarithmic intersection integral on an analytic resolution](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.resBridge/)).
