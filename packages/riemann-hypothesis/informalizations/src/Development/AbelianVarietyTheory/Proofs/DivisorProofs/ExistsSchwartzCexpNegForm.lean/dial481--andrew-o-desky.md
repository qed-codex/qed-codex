---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSchwartzCexpNegForm.lean",
  "declarations": [
    "GlobalTheory.GaussComplexForm.exists_schwartz_cexp_neg_form"
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

## A coercive complex Gaussian is a Schwartz function

[Theorem THETA.1491](https://andrewodesky.com/rh/lean/GlobalTheory.GaussComplexForm.exists_schwartz_cexp_neg_form/)

Let $V$ be a finite-dimensional real normed vector space, and let $Q:V\times V\to\mathbb C$ be a continuous real-bilinear form. Suppose there is $c>0$ with $$c\|x\|^2\le\operatorname{Re}Q(x,x)\qquad(x\in V).$$ Then $g(x)=\exp(-Q(x,x))$ is a Schwartz function on $V$, and its real derivative is $$dg_x(p)=-\bigl(Q(x,p)+Q(p,x)\bigr)g(x)\qquad(x,p\in V).$$
