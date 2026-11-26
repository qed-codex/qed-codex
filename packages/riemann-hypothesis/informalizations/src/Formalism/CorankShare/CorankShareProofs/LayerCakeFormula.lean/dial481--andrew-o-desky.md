---
{
  "module": "src/Formalism/CorankShare/CorankShareProofs/LayerCakeFormula.lean",
  "declarations": [
    "Formalism.CorankShareLayerCake.FR.layer_cake_formula"
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

## Mean bound from counts below a moving threshold

[Theorem ALG.0150](https://andrewodesky.com/rh/lean/Formalism.CorankShareLayerCake.FR.layer_cake_formula/)

Let $m$ be a positive integer, $x_1,\ldots,x_m\in\mathbb R$, $a\in\mathbb R$, and $S\ge0$. Let $w:\mathbb R\to\mathbb R$ be such that $\tau\mapsto\min\{1,w(\tau)\}$ is Lebesgue integrable on $[0,S]$. Suppose that $$x_j\ge a-S\quad(1\le j\le m),\qquad\#\{j:x_j<a-\tau\}\le m\,w(\tau)\quad(0\le\tau\le S).$$ Then $$a-\int_0^S\min\{1,w(\tau)\}\,d\tau\le\frac1m\sum_{j=1}^m x_j.$$
