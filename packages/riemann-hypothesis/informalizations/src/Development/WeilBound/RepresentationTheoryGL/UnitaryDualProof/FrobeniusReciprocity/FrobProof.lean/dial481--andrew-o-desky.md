---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/FrobeniusReciprocity/FrobProof.lean",
  "declarations": [
    "PositivityTheory.PfBern.Frob.frobeniusReciprocity"
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

## Frobenius reciprocity for equivariant distributions

[Theorem REP.0552](https://andrewodesky.com/rh/lean/PositivityTheory.PfBern.Frob.frobeniusReciprocity/)

Let $G$ be a second-countable locally compact totally disconnected Hausdorff unimodular group, and let $H\subseteq G$ be a closed locally compact unimodular subgroup. Use their Borel measurable structures, and choose left Haar measures $dg,dh$. Let $X$ be a locally compact totally disconnected Hausdorff space with a continuous $G$-action, and let $p:X\to G/H$ be continuous and $G$-equivariant. Put $Y=p^{-1}(H)$, and let $\chi:G\to\mathbb C^\times$ be a continuous character. There is a complex-linear isomorphism $$\mathcal D(X)^{G,\chi}\xrightarrow{\ \mathcal R\ }\mathcal D(Y)^{H,\chi|_H}.$$ For every closed $G$-invariant $C\subseteq X$ and every $\xi\in\mathcal D(X)^{G,\chi}$, $$\operatorname{supp}\xi\subseteq C\quad\Longleftrightarrow\quad\operatorname{supp}\mathcal R\xi\subseteq Y\cap C.$$ If $\alpha\in C_c^{\mathrm{lc}}(G)$, $\varphi\in C_c^{\mathrm{lc}}(Y)$, and $f\in C_c^{\mathrm{lc}}(X)$ satisfy $$f(gz)=\int_H\alpha(gh)\varphi(h^{-1}z)\,dh\qquad(g\in G,z\in Y),$$ then $$\xi(f)=\left(\int_G\alpha(g)\chi(g)\,dg\right)(\mathcal R\xi)(\varphi).$$
