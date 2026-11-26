---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/PhSchurConv.lean",
  "declarations": [
    "schur_orthogonality_idempotent"
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

## Convolution identities for a normalized matrix coefficient

[Theorem REP.0949](https://andrewodesky.com/rh/lean/schur_orthogonality_idempotent/)

Let $G$ be a second countable topological group with its Borel measurable structure and a sigma-finite left-invariant measure $\mu$ invariant under inversion. Let $H$ be a complex inner product space and $\sigma:G\to\operatorname{End}_{\mathrm{cont},\mathbb C}(H)$ a strongly continuous unitary representation. Suppose $d>0$ and, for all $v,w,v',w'\in H$, the product below is integrable and $$\int_G\langle w,\sigma(g)v\rangle\overline{\langle w',\sigma(g)v'\rangle}\,d\mu(g)=\frac{\langle v',v\rangle\langle w,w'\rangle}{d}.$$ Choose $w$ of norm one and set $m(g)=\langle w,\sigma(g)w\rangle$ and $p(g)=d\overline{m(g)}$. Then $m(1)=1$, $p(g^{-1})=\overline{p(g)}$, and, for every $x,y\in G$, $$\int_G p(g)p(x^{-1}g^{-1}y)\,d\mu(g)=m(x)p(y).$$ Moreover, for all $u,u'\in H$, $$\int_Gp(g)\langle u',\sigma(g)u\rangle\,d\mu(g)=\langle w,u\rangle\langle u',w\rangle.$$ Both displayed integrands are integrable. Inner products are linear in the second variable.
