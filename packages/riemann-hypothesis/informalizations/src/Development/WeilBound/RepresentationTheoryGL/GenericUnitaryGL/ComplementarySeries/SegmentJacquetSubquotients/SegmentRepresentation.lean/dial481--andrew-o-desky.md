---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/SegmentJacquetSubquotients/SegmentRepresentation.lean",
  "declarations": [
    "PositivityTheory.RgGu.segmentRepresentation"
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

## Unique irreducible subrepresentation of a segment

[Theorem REP.0061](https://andrewodesky.com/rh/lean/PositivityTheory.RgGu.segmentRepresentation/)

Let $k$ be a nonarchimedean local field, and let $\sigma$ be an irreducible smooth cuspidal complex representation of $\operatorname{GL}_d(k)$, where $d\ge1$. For $l\ge1$, form the normalized parabolic induction $$I=\sigma\times(\sigma\otimes|\det|_k)\times\cdots\times(\sigma\otimes|\det|_k^{l-1})$$ for the standard ordered blocks of sizes $d,\ldots,d$. There is a unique irreducible subrepresentation $S\subseteq I$. Its normalized Jacquet module for these same blocks satisfies $$r_{(d,\ldots,d)}S\simeq\bigotimes_{j=0}^{l-1}(\sigma\otimes|\det|_k^j).$$
