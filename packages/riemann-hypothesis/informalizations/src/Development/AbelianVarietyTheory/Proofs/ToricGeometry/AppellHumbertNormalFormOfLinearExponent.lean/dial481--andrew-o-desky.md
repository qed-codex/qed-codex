---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ToricGeometry/AppellHumbertNormalFormOfLinearExponent.lean",
  "declarations": [
    "GlobalTheory.appellHumbert_normal_form_of_linear_exponent"
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

## Hermitian normal form for linear factors of automorphy

[Theorem AV.1453](https://andrewodesky.com/rh/lean/GlobalTheory.appellHumbert_normal_form_of_linear_exponent/)

Let $\Lambda\subset\mathbb C^g$ be a discrete $\mathbb Z$-submodule spanning $\mathbb C^g$ over $\mathbb R$. Let $a:\Lambda\to\mathbb C^\times$ and let $B:\Lambda\to\operatorname{Hom}_{\mathbb C}(\mathbb C^g,\mathbb C)$ be additive, with $$a(\lambda+\mu)=a(\lambda)a(\mu)e^{B(\lambda)(\mu)}.$$ There are a Hermitian matrix $M\in M_g(\mathbb C)$, $\chi:\Lambda\to\mathbb C$ with $|\chi(\lambda)|=1$, an integer bilinear form $E$ on $\Lambda$, and an entire function $Q:\mathbb C^g\to\mathbb C$ with $Q(0)=0$, such that, writing $H(z,w)=z^TM\overline w$, $$E(\lambda,\mu)=\operatorname{Im}H(\lambda,\mu),$$ $$a(\lambda)e^{B(\lambda)(z)}e^{Q(z)-Q(z+\lambda)} =\chi(\lambda)e^{\pi H(z,\lambda)+\pi H(\lambda,\lambda)/2}.$$
