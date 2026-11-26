---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IteratedDerivScale.lean",
  "declarations": [
    "GlobalTheory.PsCo.PcdSFB.stBlow"
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

## A rescaled integral near an invertible diagonal derivative

[Theorem AG.0479](https://andrewodesky.com/rh/lean/GlobalTheory.PsCo.PcdSFB.stBlow/)

Let $I$ be finite, put $d=|I|$, and let $\beta:\mathbb C^I\to\mathbb C^I$ be continuous, with $\beta(0)=0$ and real Fréchet derivative $$D\beta(0)w=(a_iw_i)_{i\in I},\qquad a_i\ne0.$$ Assume that for every $\delta>0$ there is $\eta>0$ such that $$\sum_i|\beta(B)_i|^2\le\eta\quad\Longrightarrow\quad\|B\|\le\delta.$$ Let $F:\mathbb R\to\mathbb R$ be continuous with $F(x)=0$ for $x\ge1$, and let $\psi:\mathbb C^I\to\mathbb C$ be continuous. For all sufficiently large real $t$, the integrand below is Lebesgue integrable, and $$\lim_{t\to+\infty}t^d\int_{\mathbb C^I}F\!\left(t\sum_i|\beta(B)_i|^2\right)\psi(B)\,dB =\frac{\psi(0)}{\prod_i|a_i|^2}\int_{\mathbb C^I}F\!\left(\sum_i|w_i|^2\right)\,dw.$$
