---
{
  "module": "src/Formalism/SharpRestriction/Divisibility/SlopeExcess/HeightBoundOfComponentBounds.lean",
  "declarations": [
    "Formalism.MainNotions.DIV.Proofs.height_bound_of_component_bounds"
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

## Polynomial slope bound from the component estimates

[Theorem ARAK.0178](https://andrewodesky.com/rh/lean/Formalism.MainNotions.DIV.Proofs.height_bound_of_component_bounds/)

Fix the full arithmetic-family datum of ([Integral maps with height and target bounds](https://andrewodesky.com/rh/lean/Formalism.MainNotions.LinkDIV_at/)), with its explicit heights $h_u$, starting scale $x_1$, and constant $C_t$. Let $L_u^{(0)}$ be its base-level source lattice, $N_u$ its shifted source lattice, $R$ its target, and $G,F,E_u$ its supplied total gain, finite correction and error. Let $\bar\kappa$ be the mean logarithm of the target normalization at the complex embeddings. Supply three functions of the family's fixed output-constant list, and write $E_b,E_c,E_0$ for their values on that list.

Assume the full family source-slope comparison, positive source ranks, and eventual finite generation and fullness of every $N_u$. Also assume the source-prime condition $$b^{m/2}\le T_u,\qquad \log T_u\le C_Tm x^\varepsilon$$ eventually, with $C_T$ the family's specified source-prime constant. Require the three uniform eventual estimates $$\mu_{\max}(L_u^{(0)})\le x^{E_b}b,\qquad G+F-E_u\le x^{E_c}b,\qquad \mu_{\max}(R)+\bar\kappa\le x^{E_0}b.$$ Finally assume the full threshold condition: every initial and final construction constant is nonnegative, and every intermediate construction constant, including $C_H$, is at least $$\max\{E_b,E_c,E_0,9(\max(C_t,5)+3)+1\}+1.$$ Then there exists $x_0\in\mathbb R$ such that, for every $x\ge x_0$ with $x>x_1$ and every family member at $x$, $$\frac{\sum_ud_u(\mu(N_u)-h_u)}{\sum_ud_u}+\mu_{\max}(R)\le x^{C_H}b,\qquad d_u=\dim_K(KN_u).$$
