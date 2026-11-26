---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/PoitouTateDuality/PtfsShaFinal.lean",
  "declarations": [
    "PositivityTheory.Lit1.PTN.shaCmpFS'"
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

## Perfect pairings between finite localization kernels

[Theorem GC.0082](https://andrewodesky.com/rh/lean/PositivityTheory.Lit1.PTN.shaCmpFS'/)

Let $K\subset\overline{\mathbb Q}$ be a number field with the chosen algebraic closure, let $\ell$ be prime, and let $r\ge1$. Assume $\ell\ne2$ or $K$ is totally complex. Fix a primitive $\ell^r$-th root of unity and a family of local invariant maps as in ([A normalized local second-cohomology isomorphism](https://andrewodesky.com/rh/lean/GlobalTheory.T.normalised_local_invariant_exists/)), each bijective at every finite place and normalized by that root. Let $S$ be a finite set of finite places containing every place over $\ell$, and choose a valuation ring of $\overline{\mathbb Q}$ above each place of $S$.

Put $R=\mathbb Z/\ell^r\mathbb Z$, and let $G_{K,S}$ be the Galois group of the maximal extension unramified outside $S$. Choose $\mu:G_{K,S}\to R^\times$ whose pullback to $G_K$ is the cyclotomic character modulo $\ell^r$. Let $M$ be a finite discrete $R$-module with continuous $G_{K,S}$-action. For the twisted dual $M'$ and localization kernels, use the definitions in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), with $F=K$ and $\Omega=\overline{\mathbb Q}$. There are perfect $R$-bilinear pairings $$\operatorname{Sha}^2_S(M)\times\operatorname{Sha}^1_S(M')\longrightarrow R,$$ $$\operatorname{Sha}^2_S(M')\times\operatorname{Sha}^1_S(M)\longrightarrow R.$$ All four groups are finite; perfect means that either argument identifies its group with the $R$-linear dual of the other.
