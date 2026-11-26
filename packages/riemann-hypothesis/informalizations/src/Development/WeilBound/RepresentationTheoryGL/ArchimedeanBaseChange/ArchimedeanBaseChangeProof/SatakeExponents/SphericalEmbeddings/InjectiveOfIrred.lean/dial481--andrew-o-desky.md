---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/SphericalEmbeddings/InjectiveOfIrred.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.N3.Psl.satLink"
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

## Spherical parameters of inducing factors

[Theorem REP.1638](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.N3.Psl.satLink/)

Let $E$ be a number field, $w$ a finite place, $c,n\ge0$, and $N_1,\ldots,N_c\ge0$ with $\sum_iN_i=n$. Let $\sigma_i$ be smooth irreducible complex representations of $\operatorname{GL}_{N_i}(E_w)$, and let $P$ be a smooth irreducible complex representation of $\operatorname{GL}_n(E_w)$. Suppose $P$ is a subquotient of the normalized parabolic induction of $\boxtimes_i\sigma_i$ and is spherical. Let $\xi_1,\ldots,\xi_n\in\mathbb C^\times$, and assume a nonzero intertwiner $$P\longrightarrow I(\xi_1,\ldots,\xi_n)$$ exists, where $I(\xi)$ is normalized unramified principal series with uniformizer parameters $\xi$. Then every $\sigma_i$ is spherical and has a Satake multiset $B_i$ such that $$\bigsqcup_{i=1}^{c} B_i=\{\xi_1,\ldots,\xi_n\}.$$
