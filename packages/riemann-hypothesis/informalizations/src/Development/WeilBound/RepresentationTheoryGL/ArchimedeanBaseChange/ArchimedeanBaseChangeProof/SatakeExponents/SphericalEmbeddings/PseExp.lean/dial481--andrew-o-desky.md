---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/SphericalEmbeddings/PseExp.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.N3.PseExp.expSph"
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

## A spherical irreducible representation maps to an unramified principal series

[Theorem REP.1329](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.N3.PseExp.expSph/)

Let $k$ be a nonarchimedean local field, let $n\ge0$, and let $\pi$ be a smooth irreducible representation of $\mathrm{GL}_n(k)$ on a complex vector space. Assume $\pi^{\mathrm{GL}_n(\mathcal O_k)}\ne0$. There are $\eta_1,\ldots,\eta_n\in\mathbb C^\times$ and a nonzero intertwining map $$\pi\longrightarrow\operatorname{Ind}_{B(k)}^{\mathrm{GL}_n(k)}(\chi_{\eta_1}\otimes\cdots\otimes\chi_{\eta_n}),$$ where induction is normalized, $B$ is the upper triangular Borel, and $\chi_{\eta_i}(x)=\eta_i^{\operatorname{ord}_k(x)}$, with $\operatorname{ord}_k(\varpi)=1$ for a uniformizer $\varpi$.
